from aiopg import Connection
import logging
import uuid
from typing import List, Optional, Any, Sequence, Protocol
from pydantic import BaseModel
from asyncio import Lock
from src.misc import ConsoleColors
import enum


class Entity(Protocol):
    uuid: str | None
    __tablename__: str

    def model_dump(self):
        raise NotImplementedError


class CommandTypes(enum.Enum):
    """Enumeration to represent command types.

    Attributes:
        save: Command type for 'save' operations.
        update: Command type for 'update' operations.
        delete: Command type for 'delete' operations.
    """
    save = 'save'
    update = 'update'
    delete = 'delete'


class CommandGroup(BaseModel):
    """Type definition for a dictionary representing a command.

    Attributes:
        command: The SQL command to be executed.
        command_type: The type of command being represented.
        values: The values to be used with the SQL command.
        uuid: A unique identifier for the command.
    """
    command: str
    command_type: CommandTypes
    values: Sequence[Any]
    uuid: str


class CommandResult(BaseModel):
    """Type definition for a dictionary representing a command result.

    Attributes:
        uuid: A unique identifier for the command.
        command_type: The type of command that was executed.
    """
    uuid: str
    command_type: CommandTypes


class QueryHandler:
    """Handles database queries for a specific model.

    Attributes:
        lock: An asyncio Lock object to ensure thread-safe database access.
        model: The model class associated with this query handler.
        connection: The aiopg Connection object for database interaction.
        columns: A list of column names for the model.
        tablename: The table name for the model.
    """

    def __init__(self, model: Any, connection: Connection):
        """Initializes the QueryHandler with a model and database connection.

        Args:
            model: The model class associated with this query handler.
            connection: The aiopg Connection object for database interaction.
        """

        self.lock = Lock()
        self.model = model
        self.connection = connection
        self.columns = list(model.model_fields.keys())  # type: ignore
        self.tablename: str = model.__tablename__  # type: ignore

    async def find_one(self, **kwargs) -> Optional[Any]:
        """Retrieves a single record from the database matching the criteria.

        Args:
            **kwargs: Field-value pairs to filter the query.

        Returns:
            An instance of the model with the retrieved data,
            or None if no match is found.
        """
        values = None
        result = None
        if kwargs:
            columns = list(kwargs.keys())
            values = list(kwargs.values())
            where_clause = " AND ".join([f"{c} = %s" for c in columns])
            query = f"SELECT * FROM {self.tablename} WHERE {where_clause};"

        else:
            query = f"SELECT * FROM {self.tablename}"

        async with self.lock:
            cursor = await self.connection.cursor()
            await cursor.execute(query, values)
            result = await cursor.fetchone()

        logging.debug(
            ConsoleColors.okblue(
                f"\n\nQuery: {query} Values: {values}\n\n"
            )
        )

        if result:
            column_names = []
            if cursor.description is not None:
                for item in cursor.description:
                    column_names.append(item[0])

            dict_result = dict(list(zip(column_names, result)))
            cursor.close()

            return self.model(**dict_result)  # type: ignore

        cursor.close()
        return None

    async def find_all(self, **kwargs) -> List[Any]:
        """Retrieves all records from the database matching the criteria.

        Args:
            **kwargs: Field-value pairs to filter the query.

        Returns:
            A list of model instances with the retrieved data.
        """
        values = None
        if kwargs:
            columns = list(kwargs.keys())
            values = list(kwargs.values())
            where_clause = " AND ".join([f"{c} = %s" for c in columns])
            query = "SELECT * FROM {} WHERE {};".format(
                self.tablename, where_clause
            )
        else:
            query = f"SELECT * FROM {self.tablename}"

        async with self.lock:
            cursor = await self.connection.cursor()
            await cursor.execute(query, values)
            results = await cursor.fetchall()

        logging.debug(
            ConsoleColors.okblue(
                f"\n\nQuery: {query} Values: {values}\n\n"
            )
        )

        column_names = []
        if cursor.description is not None:
            for item in cursor.description:
                column_names.append(item[0])

        response_dicts = [
            {key: value for key, value in zip(column_names, list(result))}
            for result in results
        ]

        response = [self.model(**item) for item in response_dicts if item]

        cursor.close()
        return response

    async def find_all_cointaining(self, **kwargs) -> List[Any]:
        """Retrieves all records containing the specified values in
        their fields.

        Args:
            **kwargs: Field-value pairs to filter the query
            using LIKE operator.

        Returns:
            A list of model instances with the retrieved data.

        Raises:
            KeyError: If no search keys are provided.
        """
        if kwargs == {}:
            raise KeyError("Method must have at least one key to search")

        columns = list(kwargs.keys())
        values = list(kwargs.values())

        where_clause = " AND ".join([f"{c} LIKE %s" for c in columns])

        query = f"SELECT * FROM {self.tablename} WHERE {where_clause};"
        async with self.lock:
            cursor = await self.connection.cursor()
            await cursor.execute(query, [f"%{value}%" for value in values])
            results = await cursor.fetchall()

        logging.debug(
            ConsoleColors.okblue(
                f"\n\nQuery: {query} Values: {values}\n\n"
            )
        )

        column_names = []
        if cursor.description is not None:
            for item in cursor.description:
                column_names.append(item[0])

        response_dicts = [
            {key: value for key, value in zip(column_names, list(result))}
            for result in results
        ]
        response = [self.model(**item) for item in response_dicts if item]

        cursor.close()
        return response

    async def execute_and_fetch_one(self, query: str, params: tuple):
        """Executes a given SQL query and fetches a single result.

        Args:
            query: The SQL query to execute.
            params: A tuple of parameters to use with the query.

        Returns:
            A dictionary representing the fetched row, or None if
            no row is fetched.
        """
        logging.debug(
            ConsoleColors.okblue(
                f"\n\nCommand: {query}\n\n"
            )
        )

        async with self.lock:
            cursor = await self.connection.cursor()
            await cursor.execute(query, params)

        column_names = []
        if cursor.description is not None:
            for item in cursor.description:
                column_names.append(item[0])

        result = await cursor.fetchone()

        if result:
            column_names = []
            if cursor.description is not None:
                for item in cursor.description:
                    column_names.append(item[0])

            dict_result = dict(list(zip(column_names, result)))
            cursor.close()
            return dict_result

        cursor.close()
        return None

    async def execute_and_fetch_all(self, query: str, params: tuple):
        """Executes a given SQL query and fetches all results.

        Args:
            query: The SQL query to execute.
            params: A tuple of parameters to use with the query.

        Returns:
            A list of dictionaries representing the fetched rows.
        """
        logging.debug(
            ConsoleColors.okblue(
                f"Query: {query}"
            )
        )

        async with self.lock:
            cursor = await self.connection.cursor()
            await cursor.execute(query, params)

        column_names = []
        if cursor.description is not None:
            for item in cursor.description:
                column_names.append(item[0])

        results = await cursor.fetchall()

        response_dicts = [
            {key: value for key, value in zip(column_names, list(result))}
            for result in results
        ]

        cursor.close()
        return response_dicts


class CommandHandler:
    """Handles database commands for a specific model.

    Attributes:
        lock: An asyncio Lock object to ensure thread-safe database access.
        model: The model class associated with this command handler.
        connection: The aiopg Connection object for database interaction.
        tablename: The table name for the model.
        commands: A list of CommandDict representing pending database commands.
    """
    def __init__(self, model: Any, connection: Connection):
        """Initializes the CommandHandler with a model and database connection.

        Args:
            model: The model class associated with this command handler.
            connection: The aiopg Connection object for database interaction.
        """
        self.lock = Lock()
        self.model = model
        self.connection = connection
        self.tablename: str = model.__tablename__
        self.commands: List[CommandGroup] = []

    def save(
        self, data: Entity | List[Entity],
        uuid_str: Optional[str] = None
    ) -> None:

        """Prepares a 'save' command to insert data into the database.

        Args:
            data: The data to be saved, can be a single model instance or
            a list of instances.
            uuid_str: An optional UUID string to use for the record(s).
        """
        def save_one(model: Entity, uuid_str: Optional[str] = None):

            kwargs = model.model_dump()

            if uuid_str is None:
                kwargs["uuid"] = str(uuid.uuid1())
            else:
                kwargs["uuid"] = uuid_str

            columns = list(kwargs.keys())
            values = list(kwargs.values())
            column_clause = ", ".join(columns)
            value_placeholder = ", ".join(["%s"] * len(columns))
            command = "INSERT INTO {} ({}) VALUES ({})".format(
                self.tablename, column_clause, value_placeholder
            )

            self.commands.append(CommandGroup(
                command=command,
                command_type=CommandTypes.save,
                values=values,
                uuid=kwargs["uuid"]
            ))

        if isinstance(data, list):
            for model in data:
                save_one(model, uuid_str)
        else:
            save_one(data, uuid_str)

    def update(
        self, item: Entity,
        data: dict = {}
    ) -> None:

        """Prepares an 'update' command to update data in the database.

        Args:
            item: The model instance to be updated.
            data: A dictionary of field-value pairs to update.
        """
        values = list(data.values())

        set_clause = ", ".join(
            [f"{column} = %s" for column in data.keys()]
        )

        command = "UPDATE {} SET {} WHERE uuid = '{}';".format(
            self.tablename, set_clause, item.uuid
        )

        if item.uuid is None:
            raise

        self.commands.append(CommandGroup(
            command=command,
            command_type=CommandTypes.update,
            values=values,
            uuid=item.uuid
        ))

    def delete(self, data: Entity | List[Entity]) -> None:
        """Prepares a 'delete' command to remove data from the database.

        Args:
            data: The data to be deleted, can be a single model
            instance or a list of instances.
        """

        def delete_one(item: Entity):
            uuid = item.uuid
            if uuid is None:
                raise

            command = f"DELETE FROM {self.tablename} WHERE uuid = %s;"
            self.commands.append(CommandGroup(
                command=command,
                command_type=CommandTypes.delete,
                values=[uuid],
                uuid=uuid
            ))

        if isinstance(data, list):
            for item in data:
                delete_one(item)
        else:
            delete_one(data)

    def delete_from_uuid(self, uuid: str) -> None:
        """Prepares a 'delete' command to remove a record from the
        database by UUID.

        Args:
            uuid: The UUID string of the record to be deleted.
        """

        command = f"DELETE FROM {self.tablename} WHERE uuid = %s;"

        self.commands.append(CommandGroup(
            command=command,
            command_type=CommandTypes.delete,
            values=[uuid],
            uuid=uuid
        ))

    async def commit(self) -> List[CommandResult]:
        """Executes all pending database commands and commits the transaction.

        Returns:
            A list of CommandResult indicating the results of the executed
            commands.
        """

        results: List[CommandResult] = []
        try:
            async with self.lock:
                async with self.connection.cursor() as cursor:
                    async with cursor.begin():

                        for command_dict in self.commands:

                            uuid = command_dict.uuid
                            command = command_dict.command
                            values = command_dict.values
                            command_type = command_dict.command_type

                            await cursor.execute(command, values)

                            results.append(CommandResult(
                                command_type=command_type,
                                uuid=uuid
                            ))

                        return results
        finally:
            self.commands = []
