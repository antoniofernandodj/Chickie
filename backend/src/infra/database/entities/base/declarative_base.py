import time
from sqlalchemy.orm import DeclarativeBase, object_session
from uuid import uuid4
from sqlalchemy import Column as Col, Float, String, Integer, DateTime
from datetime import datetime
import logging
from sqlalchemy import event


class Base(DeclarativeBase):
    timestamp = Col(Float, default=float(time.time()))
    uuid = Col(String(36), unique=True, default=str(uuid4()))

    @staticmethod
    def after_insert(mapper, connection, target):
        logging.info(f"Novo registro inserido: {target}")

        session = object_session(target)
        audit_log = AuditLog(
            table_name=target.__tablename__,
            record_id=target.id,
            action="insert",
        )
        session.add(audit_log)

    @staticmethod
    def after_update(mapper, connection, target):
        logging.info(f"Registro atualizado: {target}")
        session = object_session(target)
        audit_log = AuditLog(
            table_name=target.__tablename__,
            record_id=target.id,
            action="update",
        )
        session.add(audit_log)

    @staticmethod
    def after_delete(mapper, connection, target):
        logging.info(f"Registro excluído: {target}")
        session = object_session(target)
        audit_log = AuditLog(
            table_name=target.__tablename__,
            record_id=target.id,
            action="delete",
        )
        session.add(audit_log)


class AuditLog(Base):
    id = Col(Integer, primary_key=True)
    table_name = Col(String)
    record_id = Col(Integer)
    action = Col(String)
    timestamp = Col(DateTime, default=datetime.now)  # type: ignore


event.listen(Base, "after_insert", Base.after_insert)
event.listen(Base, "after_update", Base.after_update)
event.listen(Base, "after_delete", Base.after_delete)
