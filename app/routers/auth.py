from typing import List
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from fastapi import Depends, APIRouter, HTTPException
import ..imglib.getimg as imglib

router = APIRouter()


@router.get("/auth/getCaptcha", tags=["auth"])
async def getCaptcha(db:Session=Depends(get_db)):
    captcha=crud.getCaptcha(db)
    imglib.getimg(captcha.data, '../../static/tmp/'+captcha.sessionId+'.png')
    #返回验证码ID，前端需要根据ID访问验证码路径
    #http://后端地址/static/tmp/验证码ID.png
    return {
        'status':200,
        'message':'验证码获取成功',
        'data':{
            'captchaId':captcha.captchaId
        }
    }
@router.post("/auth/login",tags=["auth"])
async def login(db:Session=Depends(get_db),body: schemas.LoginUser):
    captchaAnswer={
        id=body.captchaId,
        year=body.captchaAnswer
    }
    if crud.VerifyCaptcha(db,captchaAnswer)==1:
        return {
            'status':200,
            'message':'验证码填写不正确！'
        }
    #以下为登录部分