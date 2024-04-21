import asyncio

users = {}
id = 1

lock = asyncio.Lock()

async def add():
    async with lock:
        global id
        users.update({f'name-{id}': 'value'})
        id += 1

async def print_users():
    return str(users)

async def delete():
    async with lock:
        global users
        users = {}

while True:
    user_input = input(">>> ")
    if user_input == 'exit':
        break
    elif user_input == 'add':
        asyncio.run(add())
    elif user_input == 'print':
        print(asyncio.run(print_users()))
    elif user_input == 'delete':
        asyncio.run(delete())
