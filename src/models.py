from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, DateTime, Integer, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime
from typing import List

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    create_date: Mapped[datetime.datetime] = mapped_column(DateTime(), default=datetime.datetime.utcnow)
    is_active: Mapped[bool] = mapped_column(Boolean(), default=True)
    favorites_people: Mapped[List["Favorite_people"]] = relationship(back_populates="user_rel")
    favorites_planets: Mapped[List["Favorite_planets"]] = relationship(back_populates="user_rel")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "is_active": self.is_active,
            "create_date": self.create_date
        }


class Favorite_people(db.Model):
    __tablename__ = "favorite_people"
    """ id: Mapped[int] = mapped_column(primary_key=True) """
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"),  primary_key=True)
    people_id: Mapped[int] = mapped_column(ForeignKey("people.id"),  primary_key=True)
    added_date: Mapped[datetime.datetime] = mapped_column(DateTime(), default=datetime.datetime.utcnow)
    user_rel: Mapped["User"] = relationship(back_populates="favorites_people")
    person_rel: Mapped["People"] = relationship(back_populates="favorited_by")

    def serialize(self):
        return {
            
            "user_id": self.user_id,
            "people_id": self.people_id,
            "added_date": self.added_date
        }

class Favorite_planets(db.Model):
    __tablename__ = "favorite_planets"
    """ id: Mapped[int] = mapped_column(primary_key=True) """
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"), primary_key=True)
    added_date: Mapped[datetime.datetime] = mapped_column(DateTime(), default=datetime.datetime.utcnow)
    user_rel: Mapped["User"] = relationship(back_populates="favorites_planets")
    planet_rel: Mapped["Planets"] = relationship(back_populates="favorited_by")

    def serialize(self):
        return {
            
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "added_date": self.added_date
        }


class People(db.Model):
    __tablename__ = "people"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=True)
    mass: Mapped[int] = mapped_column(Integer, nullable=True)
    hair_color: Mapped[str] = mapped_column(String(30), nullable=True)
    skin_color: Mapped[str] = mapped_column(String(30), nullable=True)
    eye_color: Mapped[str] = mapped_column(String(30), nullable=True)
    birth_year: Mapped[str] = mapped_column(String(30), nullable=True) 
    gender: Mapped[str] = mapped_column(String(30), nullable=True)
    favorited_by: Mapped[List["Favorite_people"]] = relationship(back_populates="person_rel")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "gender": self.gender
        }

class Planets(db.Model):
    __tablename__ = "planet"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    rotation_period: Mapped[int] = mapped_column(Integer, nullable=True)
    orbital_period: Mapped[int] = mapped_column(Integer, nullable=True)
    diameter: Mapped[int] = mapped_column(Integer, nullable=True)
    climate: Mapped[str] = mapped_column(String(120), nullable=True)
    gravity: Mapped[str] = mapped_column(String(120), nullable=True) 
    terrain: Mapped[str] = mapped_column(String(120), nullable=True)
    surface_water: Mapped[int] = mapped_column(Integer, nullable=True)
    population: Mapped[int] = mapped_column(Integer, nullable=True)
    favorited_by: Mapped[List["Favorite_planets"]] = relationship(back_populates="planet_rel")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "terrain": self.terrain
        }