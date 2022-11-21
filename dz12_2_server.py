import asyncio
import socket


async def simple_calculation(client):
    loop = asyncio.get_event_loop()
    request = None
    while request != "quit":
        request = (await loop.sock_recv(client, 1024)).decode('utf8')
        global s
        s = request.split(" ")
        await res1()
        await res2()
        await res3()
        answer = f"A + B = {res1}; A - B = {res2}; A * B = {res3}"
        await loop.sock_sendall(client, answer.encode('utf8'))
        break
    client.close()


async def res1():
    global res1
    res1 = int(s[0]) + int(s[1])
    await asyncio.sleep(1)
    print(f'A + B = {res1}')


async def res2():
    global res2
    res2 = int(s[0]) - int(s[1])
    await asyncio.sleep(1)
    print(f'A - B = {res2}')


async def res3():
    global res3
    res3 = int(s[0]) * int(s[1])
    await asyncio.sleep(1)
    print(f'A * B = {res3}')


async def my_server():

    sock_com = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_com.bind(("127.0.0.1", 55000))
    sock_com.listen(10)
    print("I am waiting for your message:")
    loop = asyncio.get_event_loop()
    while True:
        client, _ = await loop.sock_accept(sock_com)
        loop.create_task(simple_calculation(client))


asyncio.run(my_server())