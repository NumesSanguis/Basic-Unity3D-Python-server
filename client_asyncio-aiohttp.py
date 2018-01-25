import asyncio
import json


async def tcp_echo_client(message, loop):
    # '127.0.0.1', 8888,
    reader, writer = await asyncio.open_connection('0.0.0.0', 9090,
                                                   loop=loop)

    print('Send: %r' % message)
    writer.write(json.dumps(message).encode())

    data = await reader.read(100)
    print("Data: ", data)
    data_json = json.loads(data.decode())
    print('Received: %r' % data_json)
    print(data_json['welcome'])

    print('Close the socket')
    writer.close()


message = {'welcome': 'Hello World!'}
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()
