#!/usr/bin/python3
"""
Defines State class
"""
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """State ORM class"""

    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
