from sanic import Blueprint
from sanic.response import json

from redis_driver.redis_driver import rd

test_bp = Blueprint('test_bp')


@test_bp.route('/api/test')
async def test(request):
    print(rd)
    rd.set('ggg', '2222')
    print(rd.get('ggg'))
    return json(['hello world'])
