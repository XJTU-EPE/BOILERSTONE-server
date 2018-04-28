"""
table of a room
"""
from peewee import CharField, IntegerField, DateTimeField, ForeignKeyField
from model.baseModel import BaseModel
from model.base_user import BaseUser


class BaseRoom(BaseModel):
    start_time = DateTimeField()
    user_left = ForeignKeyField(BaseUser)
    user_right = ForeignKeyField(BaseUser)
