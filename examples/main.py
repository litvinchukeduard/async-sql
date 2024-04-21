import asyncio
import random
'''
-Чи може код бути частково асинхронним? Наприклад, лише одна або декілька функцій в коді.
-Як написати код, щоб один тип логів записувався в файл, а інший виводився в консоль?
-Як обнулити змінна в асинхронному коді?
'''

# https://docs.python.org/3/library/logging.handlers.html

async def get_info_from_api(number):
    wait_seconds = random.randint(1, 10)
    await asyncio.sleep(wait_seconds) # Async request
    print(f"Function number {number} finished")

async def api_calls():
    calls = []
    for i in range(10):
        calls.append(get_info_from_api(i))
    await asyncio.gather(*calls)

def main():
    print("Hello, world!")
    #...
    while True:
        user_input = input(">>> ")
        if user_input == 'exit':
            break
        elif user_input == 'call api':
            asyncio.run(api_calls())

if __name__ == '__main__':
    main()