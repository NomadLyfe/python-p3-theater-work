from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///theater_work.db')
Session = sessionmaker(bind=engine)
session = Session()

class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer(), primary_key=True)
    actor = Column(String())
    location = Column(String())
    hired = Column(String())

    role_id = Column(Integer(), ForeignKey('roles.id'))

    def __repr__(self):
        return f'<Audition(id={self.id}, actor={self.actor}, location={self.location}, hired={self.hired})>'
    
    def call_back(self):
        if self.hired == 'False':
            session.query(Audition).filter(Audition.id == self.id).update({Audition.hired: 'True'})
            session.commit()
        else:
            print(f'{self.actor} was already hired to play as {self.role.character_name}.')
    
class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer(), primary_key=True)
    character_name = Column(String())

    auditions = relationship('Audition', backref=backref('role'))

    def __repr__(self):
        return f'<Role(id={self.id}, character_name={self.character_name})>'
    
    @property
    def actors(self):
        return [audition.actor for audition in self.auditions]
    
    @property
    def locations(self):
        return [audition.location for audition in self.auditions]
