from src.infra.database.interfaces.interfaces import CommandInterface
from typing import Any
from src.event import Event


class CreateCommand(CommandInterface):
    def __init__(self, item: Any):
        self.item = item
        self.user_id = item.uuid  # type: ignore
        self.attributes = item.model_dump()  # type: ignore

    def __repr__(self):
        return f'<Command: {{ {self.sql()} }}>'

    def event(self):
        return Event(type='ItemCreatedEvent', kwargs=self.attributes)

    def sql(self):
        columns = ', '.join(self.attributes.keys())
        values = ', '.join(f"'{value}'" for value in self.attributes.values())
        return 'INSERT INTO {} ({}) VALUES ({});'.format(
            self.item.__tablename__,
            columns,
            values
        )


class UpdateCommand(CommandInterface):
    def __init__(self, item: Any):
        self.item = item
        self.user_id = item.uuid  # type: ignore
        self.attributes = item.model_dump()  # type: ignore

    def __repr__(self):
        return f'<Command {{ {self.sql()} }}>'

    def event(self):
        from src.event import Event
        return Event(
            type='ItemUpdatedEvent',
            id=self.user_id,
            kwargs=self.attributes
        )

    def sql(self):
        updates = ', '.join(
            f"{col} = '{val}'" for col, val in self.attributes.items()
        )
        return 'UPDATE {} SET {} WHERE id = {};'.format(
            self.item.__tablename__,
            updates,
            self.user_id
        )


class DeleteCommand(CommandInterface):
    def __init__(self, item: Any):
        self.item = item
        self.user_id = item.uuid  # type: ignore
        self.attributes = item.model_dump()  # type: ignore

    def __repr__(self):
        return f'<Command {{ {self.sql()} }}>'

    def event(self):
        from src.event import Event
        return Event(
            type='ItemDeletedEvent',
            id=self.user_id
        )

    def sql(self):
        return 'DELETE FROM {} WHERE id = {};'.format(
            self.item.__tablename__,
            self.user_id
        )
