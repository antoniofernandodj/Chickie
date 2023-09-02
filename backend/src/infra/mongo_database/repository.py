import logging
from uuid import uuid4
from typing import List, Optional, Any
from asyncio import Lock
from motor.motor_asyncio import AsyncIOMotorClient

class Repository:
    """A generic repository class to interact with a MongoDB collection
    for a Pydantic model."""

    def __init__(self, model: Any, db_client: AsyncIOMotorClient):
        """Initialize the repository.

        Args:
            model (Any): The Pydantic model representing the MongoDB collection.
            db_client (AsyncIOMotorClient): The MongoDB database client.

        Example:
            db_client = AsyncIOMotorClient("mongodb://localhost:27017")
            repository = Repository(Endereco, db_client=db_client)
        """
        self.lock = Lock()
        self.model = model
        self.db_client = db_client
        self.collection = db_client[model.__tablename__]

    async def find_one(self, **kwargs) -> Optional[Any]:
        """Find a single document in the MongoDB collection based on given criteria.

        Args:
            **kwargs: Keyword arguments representing the filtering criteria.

        Returns:
            Optional[Any]: The Pydantic model instance representing the document if found, None otherwise.
        """
        result = await self.collection.find_one(kwargs)

        if result:
            return self.model(**result)

        return None

    async def find_all(self, **kwargs) -> List[Any]:
        """Find all documents in the MongoDB collection based on given criteria.

        Args:
            **kwargs: Keyword arguments representing the filtering criteria.

        Returns:
            List[Any]: A list of Pydantic model instances representing the documents.
        """
        cursor = self.collection.find(kwargs)
        results = await cursor.to_list(None)

        response = [self.model(**item) for item in results]

        return response

    async def find_all_containing(self, **kwargs) -> List[Any]:
        """Find all documents in the MongoDB collection containing the given values.

        Args:
            **kwargs: Keyword arguments representing the values to be searched.

        Returns:
            List[Any]: A list of Pydantic model instances representing the documents.
        """
        if not kwargs:
            raise KeyError("Method must have at least one key to search")

        query = {key: {"$regex": value, "$options": "i"} for key, value in kwargs.items()}
        results = await self.collection.find(query).to_list(None)

        response = [self.model(**item) for item in results]

        return response

    async def save(self, model: Any) -> str:
        """Save a new document in the MongoDB collection.

        Args:
            model (Any): The Pydantic model instance representing the document to be saved.

        Returns:
            str: The UUID of the saved document.
        """
        kwargs = model.dict()  # Convert Pydantic model to a dictionary
        kwargs["_id"] = str(uuid4())

        result = await self.collection.insert_one(kwargs)

        return kwargs["_id"]

    async def update(self, item: Any, data: dict = {}) -> int:
        """Update an existing document in the MongoDB collection.

        Args:
            item (Any): The Pydantic model instance representing the document to be updated.
            data (dict, optional): The data to be updated. Defaults to an empty dictionary.

        Returns:
            int: The number of documents affected by the update operation.
        """
        query = {"_id": item._id}
        update_query = {"$set": data}

        result = await self.collection.update_one(query, update_query)

        return result.modified_count

    async def delete(self, item: Any) -> int:
        """Delete an existing document from the MongoDB collection.

        Args:
            item (Any): The Pydantic model instance representing the document to be deleted.

        Returns:
            int: The number of documents affected by the delete operation.
        """
        query = {"_id": item._id}

        result = await self.collection.delete_one(query)

        return result.deleted_count

    async def delete_from_uuid(self, uuid) -> int:
        """Delete an existing document from the MongoDB collection based on its UUID.

        Args:
            uuid: The UUID of the document to be deleted.

        Returns:
            int: The number of documents affected by the delete operation.
        """
        query = {"_id": uuid}

        result = await self.collection.delete_one(query)

        return result.deleted_count
