from peewee import CharField
from .baseModel import BaseModel


class BaseUser(BaseModel):
    """用户表"""
    class Meta:
        db_table = 'base_user'
    name = CharField(unique=True)
    password = CharField()
    password_encrypt = CharField()
    salt = CharField()
    
