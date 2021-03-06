#!/usr/bin/python3
""" model_city.py improved """
from sqlalchemy import Column, Integer, String
from relationship_state import Base
from sqlalchemy import ForeignKey


class City(Base):
    """Class city"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
