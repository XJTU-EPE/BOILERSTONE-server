from model.dbcommon import Pgdb as db

from model.base_card import BaseCard, BaseCardEffect, BaseCastTarget, BaseCardCardEffectRel, BaseCardCastTargetRel

db.connect()

db.create_tables([BaseCard, BaseCardEffect, BaseCastTarget, BaseCardCardEffectRel, BaseCardCastTargetRel])
