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
    name = Column(Unicode(255))
    email = Column(String(255), unique=True)
    password = Column(String(32))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    try:
        session = DBSession()
        user = User(u'Ben Hu', 'bhu@carvewith.us', func.md5('5mad_cows'))
        session.add(user)
        session.commit()
    except IntegrityError:
        # already exist
        pass
