from sqlalchemy.orm import Session
from random import randint
from time import time
import hashlib
import models
import schemas


# 获取Captcha
def getCaptcha(db: Session):
    captcha=db.query(models.Captcha)
    captchaRow=captcha[randint(0,len(captcha)-1)]
    hashId=hashlib.md5(randint(0,10000)+time()).md5hash.hexdigest()
    createCaptchaSession=models.CaptchaSession(data=captchaRow.data,year=captchaRow.year,sessionId=hashId)
    db.add(createCaptchaSession)
    db.commit()
    db.refresh(createCaptchaSession)
    return createCaptchaSession

def VerifyCaptcha(db: Session,captchaAnswer: schemas.VerifyCaptchaByYear):
    answerRow=db.query(models.CaptchaSession).filter(models.CaptchaSession.sessionId=captchaAnswer.id).first()
    if answerRow.year==captchaAnswer.year:
        return 0
    else:
        return 1