from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    email: str
    avatar: Optional[str]
    password: str
    description: Optional[str]
    website: Optional[str]
    stickyProjects: Optional[str]
    nickname: Optional[str]
    isBanned: bool
    isVerified: bool
    isOp: bool
    followers: int
    following: int
    regDate: int
    lastLoginDate: int
    settings: int