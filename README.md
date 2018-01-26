# Basic-Unity3D-Python-server
A Python 3.6 client with `asyncio` for asynchronous execution, that can send to and receive JSON messages from a Unity3D server (Unity 2017.2.0f3).

# Test usage Unity 3D - Python client
1) Start Unity 3D from `BasicUnityPython` & press play (you should see in Unity: Server is listening)
2) Open terminal in this folder and run: `python client_asyncio.py`, you should see in Unity: `"Hello World x"` / Python terminal:

    Send: {'welcome': 'Hello World x!'}
    Received:
    {'unity': 'Unity sends its regards x'}
    Close the socket

# Test usage Python server - Python client
1) Open terminal in this folder and run: `python server_asyncio.py`
2) Open another terminal here and run: `python client_asyncio.py`


# Test usage Unity 3D - Python with SocketIO
1) Start Unity 3D from `BasicUnityPython_aiohttp` & press play
2) Open terminal in this folder and run: `python client_asyncio_aiohttp.py` (you should see in Unity: `"data_stuff": x` / Python terminal: `message:  {'receive': 'received x'}`)


# To setup in your own project (asyncio, not SocketIO)
- Get JSON object addon in your Unity project: https://assetstore.unity.com/packages/tools/input-management/json-object-710
- Add TCPTestServer.cs to your project from this Github if you want JSON support, or: https://gist.github.com/danielbierwirth/0636650b005834204cb19ef5ae6ccedb

# Notes
Communication over SocketIO is inspired by tawnkramer/sdsandbox (https://github.com/tawnkramer/sdsandbox/tree/master).
However SocketIO (both the original with FLASK and modified with aiohttp) was found to be way slower.

Measured with a phone stopwatch for 10 seconds:

- Just asyncio: 7738 messages received from Unity
- asyncio with SocketIO and aiohttp: 97 messages received from Unity (seems to be faster than no asyncio with FLASK)

Therefore simple asyncio about 80 times as fast with this unprofessional measurement.

