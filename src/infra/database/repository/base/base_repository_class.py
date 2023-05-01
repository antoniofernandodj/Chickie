from src.infra.database import session


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
    def create(cls, **kwargs):

        item = cls.model_class(**kwargs)
        item.save()

        return item