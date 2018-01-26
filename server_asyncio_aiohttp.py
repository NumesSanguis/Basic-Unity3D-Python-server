from aiohttp import web
import socketio

# code simplified from (AI controlled driving): https://github.com/tawnkramer/sdsandbox

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

# async def index(request):
#     """Serve the client-side application."""
#     pass

    # with open('index.html') as f:
    #     return web.Response(text=f.read(), content_type='text/html')

@sio.on('connect')  # , namespace='/chat'
async def connect(sid, environ):
    print("connect ", sid)
    await sio.emit(
        "srv_message",
        data={
            'welcome': "Connection initiated",
        },
        skip_sid=True)

@sio.on('telemetry')  # , namespace='/chat'
async def message(sid, data):
    global counter
    counter += 1.0
    data_message = {'data_stuff': counter}

    if data:
        print("message: ", data)
        await sio.emit(
            "srv_message",
            #data=blend_dict,
            data=data_message,
            # "steer",
            # data={
            #     'steering_angle': steering_angle.__str__(),
            #     'throttle': throttle.__str__()
            # },
            skip_sid=True)
    else:
        # NOTE: DON'T EDIT THIS.
        await sio.emit('manual', data={}, skip_sid=True)

@sio.on('disconnect')  # , namespace='/chat'
def disconnect(sid):
    print('disconnect ', sid)

#app.router.add_static('/static', 'static')
#app.router.add_get('/', index)


if __name__ == '__main__':
    global counter
    counter = 0.0
    web.run_app(app)
