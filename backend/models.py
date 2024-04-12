from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from backend.db_config import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    content = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
