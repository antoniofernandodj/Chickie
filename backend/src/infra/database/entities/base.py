from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column as Col, DateTime


class Base(DeclarativeBase):
    time_created = Col(DateTime(timezone=True), server_default=func.now())
    time_updated = Col(DateTime(timezone=True), onupdate=func.now())
