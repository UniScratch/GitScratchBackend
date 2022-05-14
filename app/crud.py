from sqlalchemy.orm import Session
import models
import schemas

# 获取Captcha
def getCaptcha(db: Session, captcha_id: int):
    return db.query(models.Captcha).filter(models.Captcha.id == captcha_id).first()