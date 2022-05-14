from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True) # 设置主键和索引
    username = Column(String(32))
    password = Column(String(32))
    email = Column(String(32))
    avatar = Column(String(128))
    description = Column(String(2048))
    stickyProjects = Column(String(2048))
    website = Column(String(32))
    nickname = Column(String(32))
    isBanned = Column(Boolean)
    isVerified = Column(Boolean)
    isOp = Column(Boolean)
    followers = Column(Integer)
    following = Column(Integer)
    regDate = Column(Integer)
    lastLoginDate = Column(Integer)
    settings = Column(String(1024))