import asyncio
# https://docs.python.org/3/library/asyncio-stream.html
import json


# asyncio server: https://asyncio.readthedocs.io/en/latest/tcp_echo.html
# Test purpose: receive JSON message from client_asyncio and send JSON message back
async def handle_echo(reader, writer):
    # wait for message from client_asyncio
    data = await reader.read(400)
    #print("Data: ", data)

    # decode message to string and then read it as JSON
    message = json.loads(data.decode())
    addr = writer.get_extra_info('peername')
    print("Received %r from %r" % (message, addr))

    print("Send: %r" % json.dumps(message))  # message
    # encode message as UTF8 byte code
    json_mess_en = json.dumps(message).encode()
    writer.write(json_mess_en)

    # Yielding from drain() gives the opportunity for the loop to schedule the write operation
    # and flush the buffer. It should especially be used when a possibly large amount of data
    # is written to the transport, and the coroutine does not yield-from between calls to write().
    # Note: somewhere was written it was 10x slower if not done in Python 3.6 (should not be needed in 3.7)
    await writer.drain()

    print("Close the client socket")
    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, '0.0.0.0', 8080, loop=loop)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
