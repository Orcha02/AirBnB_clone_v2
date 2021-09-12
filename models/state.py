#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import os
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

if os.getenv("HBNB_TYPE_STORAGE") != "db":
    @property
    def cities(self):
        """ Getter of cities"""
        cities = models.storage.all(City)
        list_cities = []

        for i in cities.values():
            if self.id == i.place_id:
                list_cities.append(i)
            return list_cities
