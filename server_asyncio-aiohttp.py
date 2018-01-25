# from aiohttp import web
# import socketio
# import asyncio
# # https://docs.python.org/3/library/asyncio-stream.html
# import json
# #from io import StringIO
# #io = StringIO()
# # json.dump(['streaming API'], io)
# # io.getvalue()


# async def handle_echo(reader, writer):
#     data = await reader.read(100)
#     print("Data: ", data)
#
#     message = json.loads(data.decode())
#     addr = writer.get_extra_info('peername')
#     print("Received %r from %r" % (message, addr))
#     #json_mess = {'welcome': "Hello Unity world"}
#     #print(json.dumps(json_mess))
#     print("Send: %r" % json.dumps(message))  # message
#     #writer.write(json_mess)
#     #json.dump(json_mess, io)
#     #print(io.getvalue())
#
#     json_mess_en = json.dumps(message).encode()
#     writer.write(json_mess_en)
#     #writer.write(json_mess_en)
#     #writer.write(json.dumps(json_mess))  # data
#
#     # Yielding from drain() gives the opportunity for the loop to schedule the write operation
#     # and flush the buffer. It should especially be used when a possibly large amount of data
#     # is written to the transport, and the coroutine does not yield-from between calls to write().
#     #await writer.drain()
#
#     #print("Close the client socket")
#     writer.close()
#
# loop = asyncio.get_event_loop()
# # '0.0.0.0', 9090
# # '127.0.0.1', 8888
# coro = asyncio.start_server(handle_echo, '0.0.0.0', 9090, loop=loop)
# server = loop.run_until_complete(coro)
#
# # Serve requests until Ctrl+C is pressed
# print('Serving on {}'.format(server.sockets[0].getsockname()))
# try:
#     loop.run_forever()
# except KeyboardInterrupt:
#     pass
#
# # Close the server
# server.close()
# loop.run_until_complete(server.wait_closed())
# loop.close()



from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

global counter
counter = 0.0

async def index(request):
    """Serve the client-side application."""
    pass

    # with open('index.html') as f:
    #     return web.Response(text=f.read(), content_type='text/html')

@sio.on('connect')  # , namespace='/chat'
def connect(sid, environ):
    print("connect ", sid)
    sio.emit(
        "srv_message",
        data={
            'welcome': "Connection initiated",
        },
        skip_sid=True)

@sio.on('telemetry')  # , namespace='/chat'
async def message(sid, data):
    if data:
        print("message: ", data)
        global counter
        counter += 0.05
        await sio.emit(
            "srv_message",
            #data=blend_dict,
            data={'Expressions_browOutVertR_min': counter},  # , "blabla": 'sdf'
            #data={
                #'welcome': "Hello Unity world",
                #'blend_dict': json.dumps(blend_dict)  # json.dump(['streaming API'], io)  # self.blend_val.__str__()
            #},
            # "steer",
            # data={
            #     'steering_angle': steering_angle.__str__(),
            #     'throttle': throttle.__str__()
            # },
            skip_sid=True)
    else:
        # NOTE: DON'T EDIT THIS.
        sio.emit('manual', data={}, skip_sid=True)

@sio.on('disconnect')  # , namespace='/chat'
def disconnect(sid):
    print('disconnect ', sid)

#app.router.add_static('/static', 'static')
#app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)
