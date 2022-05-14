from pydantic import BaseModel
from typing import Optional

class RegUser(BaseModel):
    username: str
    email: str
    password: str

class LoginUser(BaseModel):
    email: str
    password: str

class GetUserInfoById(BaseModel):
    id: str

class GetUserInfoByName(BaseModel):
    username: str

class UserInfo(BaseModel):
    id: str
    username: str
    avatar: Optional[str]
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

class CaptchaById(BaseModel):
    id: str
    
class CaptchaInfo(BaseModel):
    year: int
    month: int
    day: int

class VerifyCaptchaByYear(BaseModel):
    id: str
    year: str