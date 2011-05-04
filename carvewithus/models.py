from sqlalchemy import Column, Integer, String, Enum, Unicode, TIMESTAMP, \
        ForeignKey, Boolean, Date, Time, DateTime, UnicodeText
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy import func

DBSession = scoped_session(sessionmaker())

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(Unicode(255), unique=True)
    name = Column(Unicode(255))
    email = Column(String(255), unique=True)
    password = Column(String(40))
    city = Column(String(255), ForeignKey('cities.short_name'))
    fb_id = Column(String(255))
    fb_profile_url = Column(String(255))
    fb_access_token = Column(String(255))
    created = Column(TIMESTAMP, default=func.current_timestamp())
    updated = Column(TIMESTAMP, default=func.current_timestamp(),
                     onupdate=func.current_timestamp())
    picture = Column(String(255))
    activity = Column(Enum('SNOWBOARD', 'SKI', 'BOTH'))
    skill_level = Column(Enum('NEWBIE', 'INTERMEDIATE', 'ADVANCED', 'EXPERT'))

    def __init__(self, username=None, name=None, email=None, password=None,
                 city=None, fb_id=None, fb_profile_url=None, 
                 fb_access_token=None):
        self.username = username
        self.name = name
        self.email = email
        self.password = password
        self.city = city
        self.fb_id = fb_id
        self.fb_profile_url = fb_profile_url
        self.fb_access_token = fb_access_token
        pass


class City(Base):
    __tablename__ = "cities"

    short_name = Column(String(255), primary_key=True)
    full_name = Column(String(255))
    state = Column(String(255))

    def __init__(self):
        pass


class Trip(Base):
    __tablename__ = 'trips'

    id = Column(Integer, primary_key=True)
    picture = Column(UnicodeText)
    name = Column(UnicodeText)
    summary = Column(UnicodeText)
    spots_available = Column(Integer)
    transportation = Column(Enum('DRIVE', 'BUS'))
    has_lodge = Column(Boolean)
    lodge_desc = Column(UnicodeText)
    itineraries = relationship('Itinerary', backref='trip')
    members = relationship('TripMember', backref='trip')
    invitations = relationship('TripInvitation', backref='trip')
    
    def __init__(self, picture=None, name=None, summary=None, spots_available=0,
                 transportation=None, has_lodge=False, lodge_desc=None,
                 organizer=None):
        self.picture = picture
        self.name = name
        self.summary = summary
        self.spots_available = spots_available
        self.transportation = transportation
        self.has_lodge = has_lodge
        self.lodge_desc = lodge_desc
        self.organizer = organizer


class Itinerary(Base):
    __tablename__ = 'itineraries'

    id = Column(Integer, primary_key=True)
    trip = Column(Integer, ForeignKey('trips.id'))
    location = Column(UnicodeText)
    date = Column(Date)
    time = Column(Time)

    def __init__(self, trip=None, location=None, date=None, time=None):
        self.trip = trip
        self.location = location
        self.date = date
        self.time = time
    

class TripMember(Base):
    __tablename__ = 'trip_member'

    trip_id = Column(Integer, ForeignKey('trips.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    join_date = Column(DateTime)
    admin = Column(Boolean, default=False)
    user = relationship('User', backref='trip_member')

class TripInvitation(Base):
    __tablename__ = 'trip_invitation'

    id = Column(Integer, primary_key=True)
    trip_id = Column(Integer, ForeignKey('trips.id'))
    inviter = Column(Integer, ForeignKey('users.id'))
    invitee = Column(Integer, ForeignKey('users.id'))
    invite_date = Column(DateTime)
    status = Column(Enum('PENDING', 'ACCEPTED', 'REJECTED'))


def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
