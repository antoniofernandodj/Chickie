import uuid
from dataclasses import dataclass
import datetime


@dataclass
class User:
    id = 'ef4f7012-8332-4c08-b430-dbf9dde8b981'
    type: str
    data: dict

    def dict(self):
        data = {}
        for _, x_item in self.data.items():
            for y_key, y_item in x_item.items():
                data[y_key] = y_item

        payload = {
            "eventId": str(uuid.uuid4()),
            "eventType": self.type,
            "eventTime": datetime.datetime.now().isoformat(),
            "aggregateId": User.id,
            "aggregateType": "User",
            "eventData": data,
        }

        return payload
