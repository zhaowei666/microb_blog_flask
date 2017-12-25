from base import Base
from sqlalchemy import Column, String, Integer, ForeignKey
import datetime


class Post(Base):
    __tablename__ = 'posts'
    author_pk = Column(Integer, ForeignKey('users.pk', nullable=True))
    title = Column(String(128), nullable=False)
    text = Column(String)

