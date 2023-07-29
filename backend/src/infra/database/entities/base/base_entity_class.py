from uuid import uuid4
from copy import deepcopy

class BaseEntityClass:

    uuid: str
    
    def __repr__(self):
        cls = type(self)
        attrs = vars(self)
        attrs_str = ', '.join(
            f"{k}={v!r}" for k, v in attrs.items()
            if k != '_sa_instance_state'
        )
        
        return f"EntityClass::{cls.__name__}({attrs_str})"
    
    def save(self):
        from src.infra import database
        cls = type(self)
        
        with database.session.get() as db:
            try:
                data = deepcopy(self.__dict__)
                data.pop('_sa_instance_state', None)
                object = cls(uuid=uuid4(), **data)
                db.add(object)
                db.commit()
                db.refresh(object)
            except:
                db.rollback()
                raise
            
    
    def update(self, **kwargs: dict):
        from src.infra import database
        cls = type(self)
        
        with database.session.get() as db:
            try:
                item = db.query(cls).filter_by(uuid=self.uuid).first()
                for key, value in kwargs.items():
                    if key != '_sa_instance_state':
                        setattr(item, key, value)
                    
                db.commit()
            except:
                db.rollback()
                raise
            
    def delete(self):
        from src.infra import database
        cls = type(self)
        
        with database.session.get() as db:
            try:
                item = db.query(cls).filter_by(uuid=self.uuid).first()
                db.delete(item)
                db.commit()
            except:
                db.rollback()
                raise