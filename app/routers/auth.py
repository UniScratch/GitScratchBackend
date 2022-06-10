from sqlalchemy.orm import Session
from ..database import get_db
from .. import crud, schemas
from ..imglib import getimg as imglib

from fastapi import Depends, APIRouter, HTTPException

router = APIRouter()


@router.get("/auth/getCaptcha", tags=["auth"])
async def getCaptcha(db: Session=Depends(get_db)):
    captcha=crud.getCaptcha(db)
    imglib.getimg(captcha.data, '../../static/tmp/' + captcha.sessionId + '.png')
    # 返回验证码ID，前端需要根据ID访问验证码路径
    # http://后端地址/static/tmp/验证码ID.png
    return {
        'status': 200,
        'message': '验证码获取成功',
        'data': {
            'captchaId':captcha.captchaId
        }
    }

@router.post("/auth/login", tags=["auth"])
async def login(body: schemas.LoginUser, db: Session=Depends(get_db)):
    captchaAnswer = {
        "id": body.captchaId,
        "year": body.captchaAnswer
    }
    if crud.verifyCaptcha(db, captchaAnswer)==1:
        return {
            'status': 200,
            'message': '验证码填写不正确'
        }
    # 以下为登录部分
    user = crud.getUserByName(db, body.username)
    if user is None:
        return {
            'status': 401,
            'message': '用户不存在'
        }
    if user.password != body.password:
        return {
            'status': 401,
            'message': '密码错误'
        }
    return {
        'status': 200,
        'message': '登录成功'
    }
