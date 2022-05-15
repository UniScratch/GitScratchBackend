from pydantic import BaseModel
from typing import Optional

class RegUser(BaseModel):
    username: str
    email: str
    password: str
    class Config:
        orm_mode = True

class LoginUser(BaseModel):
    email: str
    password: str
    captchaId: str
    captchaAnswer: int
    class Config:
        orm_mode = True

class GetUserInfoById(BaseModel):
    id: str
    class Config:
        orm_mode = True

class GetUserInfoByName(BaseModel):
    username: str
    class Config:
        orm_mode = True

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
    class Config:
        orm_mode = True

class CaptchaById(BaseModel):
    id: str
    class Config:
        orm_mode = True
    
class CaptchaInfo(BaseModel):
    year: int
    month: int
    day: int
    class Config:
        orm_mode = True

class VerifyCaptchaByYear(BaseModel):
    id: str
    year: int
    class Config:
        orm_mode = True