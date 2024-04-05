#!/usr/bin/python3
"""
This module defines the City class that represents a table in the database.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Represents the 'cities' table in the database.

    Attributes:
        id (int): The city's id.
        name (str): (sqlalchemy.Integer): The city's name.
        state_id (int): (sqlalchemy.String): The city's state id.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
