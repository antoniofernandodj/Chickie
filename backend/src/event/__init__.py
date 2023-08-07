from pymongo import MongoClient
from pymongo.results import InsertOneResult
from pymongo.collection import Collection
from src.event.models import User
from config import settings


MONGODB_URI = '{protocol}://{user}:{password}@{host}:{port}/'.format(
    protocol=settings.MONGODB_PROTOCOL,
    user=settings.MONGODB_USERNAME,
    password=settings.MONGODB_PASSWORD,
    host=settings.MONGODB_HOST_NAME,
    port=settings.MONGODB_PORT,
)


client: MongoClient = MongoClient(MONGODB_URI)
db = client[settings.MONGODB_DATABASENAME]


class Event:
    def __init__(self, type, id=None, **kwargs):
        self.type = type
        self.id = id
        self.kwargs = kwargs

    def __str__(self):
        string = f'<Event ({self.type}): '
        if self.id:
            string += f'id={self.id} '
        if self.kwargs != {}:
            string += f'kwargs={str(self.kwargs["kwargs"])} '
        string = string[:-1] + '>'
        return string


class EventStore:
    def __init__(self, collection: Collection, model: type):
        self.collection = collection
        self.model = model

    def register(self, event) -> InsertOneResult:
        item = self.model(type=event.type, data=event.kwargs)
        post_data = item.dict()
        result = self.collection.insert_one(post_data)
        print('Event registered!')
        print(f'Result: {result.inserted_id}')
        return result


store = EventStore(collection=db.loja, model=User)
