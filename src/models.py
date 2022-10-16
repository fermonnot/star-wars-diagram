import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er



Base = declarative_base()

# intente con el enum pero me apreció que no era valido asi que lo hice de la primera manera aprendida
# class Nature(Enum):
#     character = "__Character__",
#     # planets = "Planets"


class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    hair_color = Column(String(250))

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    password = Column(String(100), nullable=False)

    def __init__(self, user_name, user_password):
        self.name = user_name
        self.password = user_password

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(50), nullable=False)
    gravity = Column(String(40), nullable=False)
     
    def to_dict(self):
        return {}
    
class Favorites(Base):
    __tablename__="favorites"
    
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("character.id"))
    character = relationship("Character")
    planet_id = Column(Integer, ForeignKey("planets.id"))
    planet = relationship("Planets")
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")
     
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')