from sqlalchemy import Column, Integer, String, Unicode, TIMESTAMP
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
    fb_id = Column(String(255))
    fb_profile_url = Column(String(255))
    fb_access_token = Column(String(255))
    created = Column(TIMESTAMP, default=func.current_timestamp())
    updated = Column(TIMESTAMP, default=func.current_timestamp(),
                     onupdate=func.current_timestamp())

    def __init__(self, username=None, name=None, email=None, password=None,
                 fb_id=None, fb_profile_url=None, fb_access_token=None):
        self.username = username
        self.name = name
        self.email = email
        self.password = password
        self.fb_id = fb_id
        self.fb_profile_url = fb_profile_url
        self.fb_access_token = fb_access_token
        pass

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
