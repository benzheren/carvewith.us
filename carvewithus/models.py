from sqlalchemy import Column, Integer, String, Unicode
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

DBSession = scoped_session(sessionmaker())

Base = declarative_base()

class User(Base):
    """Mapping class for User"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(Unicode(255), unique=True)
    name = Column(Unicode(255))
    email = Column(String(255), unique=True)
    password = Column(String(40))

    def __init__(self):
        pass

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    try:
        session = DBSession()
    except IntegrityError:
        # already exist
        pass
