"""
here come the models for cards...
When one card is shengwu, it should have attack, hp, mana
When one card is fashu, it should hava mana, cast_target
"""
from peewee import CharField, IntegerField, ForeignKeyField
from .baseModel import BaseModel


class BaseCastTarget(BaseModel):
    """
    table of card's cast_target
    cast_target: 1-self_hero 2-self_minion 3-enemy_hero 4-enemy_minion  [1,2,3]
    """
    class Meta:
        db_table = 'base_card_target'
    name = CharField()


class BaseCardEffect(BaseModel):
    """
    effects usually includes
    1. change target's hp
    2. change target's attack
    """
    class Meta:
        db_table = 'base_card_effect'
    name = CharField()


class BaseCard(BaseModel):
    """
    table of card's attribute
    type: 1-shengwu 2-fashu 3-wuqi
    """
    class Meta:
        db_table = 'base_card'

    name = CharField()
    base_attack = IntegerField(null=True)
    base_hp = IntegerField(null=True)
    base_mana = IntegerField()
    type = IntegerField(default=1)


class BaseCardCastTargetRel(BaseModel):
    class Meta:
        db_table = 'base_card_cast_target_rel'
    card = ForeignKeyField(BaseCard)
    cast_target = ForeignKeyField(BaseCastTarget)


class BaseCardCardEffectRel(BaseModel):
    class Meta:
        db_table = 'base_card_card_effect_rel'
    card = ForeignKeyField(BaseCard)
    card_effect = ForeignKeyField(BaseCardEffect)
