from peewee import CharField, ForeignKeyField, IntegerField
from .baseModel import BaseModel
from model.base_user import BaseUser
from model.base_card import BaseCard


class BaseCardGroup(BaseModel):
    class Meta:
        db_table = 'base_card_group'

    name = CharField()
    cards = CharField()


class BaseUserCardGroupRel(BaseModel):
    class Meta:
        db_table = 'base_user_card_group_rel'
    user = ForeignKeyField(BaseUser)
    card_group = ForeignKeyField(BaseCardGroup)


class BaseCardGroupCardRel(BaseModel):
    class Meta:
        db_table = 'base_card_group_card_rel'

    group = ForeignKeyField(BaseCardGroup)
    card = ForeignKeyField(BaseCard)
    qty = IntegerField()
