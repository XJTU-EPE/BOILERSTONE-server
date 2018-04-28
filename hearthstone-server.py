from sanic import Sanic
from sanic.response import json
from controller.test_controller import test_bp

app = Sanic()
app.blueprint(test_bp)


@app.websocket('/socket/test')
async def socket_test(request, ws):
    while True:
        data = 'helloasd!'
        print('Sending: ' + data)
        await ws.send(data)
        data = await ws.recv()
        print('Received: ' + data)
        await ws.send('error')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

