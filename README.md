# Basic-Unity3D-Python-server
A Python 3.6 client with `asyncio` for asynchronous execution, that can send to and receive JSON messages from a Unity3D server.

# Test usage Unity 3D - Python client
1) Start Unity 3D & press play (you should see in Unity: Server is listening)
2) Open terminal in this folder and run: `python client_asyncio.py` (you should see in Unity: `"Hello World"` / Python terminal: Send: `{'welcome': 'Hello World!'}`)
3) In Unity: press `spacebar`, Unity console: `Server sent his message - should be received by client` / Python terminal:

    Received:
    {'unity': 'Unity sends its regards'}
    Close the socket

# Test usage Python server - Python client
1) Open terminal in this folder and run: `python server_asyncio.py`
2) Open another terminal here and run: `python client_asyncio.py`


# To setup in your own project
- Get JSON object addon in your Unity project: https://assetstore.unity.com/packages/tools/input-management/json-object-710
- Add TCPTestServer.cs to your project from this Github if you want JSON support, or: https://gist.github.com/danielbierwirth/0636650b005834204cb19ef5ae6ccedb

# Notes
Originally inspired by tawnkramer/sdsandbox (https://github.com/tawnkramer/sdsandbox/tree/master).
However SocketIO (both the original with FLASK and modified with aiohttp) was found to be way slower (unmeasured: more than 100x times slower).

