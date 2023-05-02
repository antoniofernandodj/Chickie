from src.infra.database import session
from src.infra.database import entities as e

class BaseRepositoryClass:

    @classmethod
    def find_one(cls, **kwargs):
        with session.get() as db:
            item = db.query(cls.model_class) \
                .filter_by(**kwargs) \
                .first()

            return item

    @classmethod
    def find_all(cls, **kwargs):

        with session.get() as db:
            items = db.query(cls.model_class) \
                .filter_by(**kwargs) \
                .all()

            return items

    @classmethod
    def remove_one(cls, **kwargs):
        with session.get() as db:
            item = db.query(cls.model_class) \
                .filter_by(**kwargs) \
                .first()
            
            db.delete(item)
            db.commit()
        
            return item

    @classmethod
    def create(cls, **kwargs):

        item = cls.model_class(**kwargs)
        item.save()

        return item

    @classmethod
    def update_one(cls, db_item: e.BaseEntityClass, data: dict):
        with session.get() as db:
            item = db.query(cls.model_class).filter_by(uuid=db_item.uuid).first()
            if not item:
                return None

            for key, value in data.items():
                setattr(item, key, value)

            db.commit()
            db.refresh(item)
            return item