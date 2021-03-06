import asyncio
import json

counter = 0

# Asynchronous communication with Unity 3D over TCP
async def tcp_echo_client(message, loop):
    # open connection with Unity 3D
    reader, writer = await asyncio.open_connection('0.0.0.0', 8080,
                                                   loop=loop)
    print('Send: %r' % message)

    # test purposes
    global counter
    message['welcome'] = f'Hello World {counter}!'

    # convert JSON to bytes
    message_json = json.dumps(message).encode()
    # send message
    writer.write(message_json)
    counter += 1

    # wait for data from Unity 3D
    data = await reader.read(100)
    # we expect data to be JSON formatted
    data_json = json.loads(data.decode())
    print('Received:\n%r' % data_json)

    print('Close the socket')
    writer.close()


message = {'welcome': 'Hello World!'}
loop = asyncio.get_event_loop()
while True:
    loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()
