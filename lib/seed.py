from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from random import choice as rc

from models import Audition, Role, session

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

actors = ['Ben Affleck', 'Dwayne Johnson', 'Robert Downey Jr.', 'Leonardo DiCaprio', 'Vin Diesel', 'Chris Evans', 'Chris Hemsworth', 'Will Smith', 'Jackie Chan', 'Keanu Reeves', 'Benedict Cumberbatch']
locations = ['Los Angeles', 'NYC', 'Houston', 'Chicago', 'Miami', 'Atlanta', 'San Francisco', 'Dallas', 'San Antonio']
char_roles = ['Peter Pan', 'Wolverine', 'Spider Man', 'Joker', 'James Bond', 'John Wick', 'Rambo', 'Han Solo', 'Nick Fury', 'Sherlock Holmes', 'Dr. Strange', 'The Hulk', 'Thor']

def insert_data():
    auditions = [Audition(actor=rc(actors), location=rc(locations), hired=rc(['True', 'False'])) for i in range(1000)]
    roles = [Role(character_name=rc(char_roles)) for i in range(100)]
    session.add_all(auditions + roles)
    session.commit()
    return auditions, roles

def delete_data():
    session.query(Audition).delete()
    session.query(Role).delete()
    session.commit()

def relate_one_to_many(auditions, roles):
    for audition in auditions:
        audition.role_id = rc([role.id for role in roles])
    session.add_all(auditions)
    session.commit()

if __name__ == '__main__':
    delete_data()
    auditions, roles = insert_data()
    relate_one_to_many(auditions, roles)
