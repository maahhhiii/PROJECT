from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(String, default="student")

class Announcement(Base):
    __tablename__ = 'announcements'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
    posted_by = Column(String)

class LostItem(Base):
    __tablename__ = 'lost_found'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    owner = Column(String)