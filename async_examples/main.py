import asyncio
import aiofiles

folder_path = "async_examples/"

# Читаемо рядки у файлі
async def read_lines(filename: str):
    lines = []
    async with aiofiles.open(folder_path + filename, mode='r') as f:
        async for line in f:
            lines.append(line)
    return lines

# Сортуємо рядки
def sort_lines(lines_list: list[str]):
    # ['1. The cat jumped over the lazy dog.\n', '2. Tomorrow never dies.\n', '3. Life is like a box of chocolates.\n']
    # [30, 20, 40]
    # [20, 30, 40]
    # ['2. Tomorrow never dies.\n', '1. The cat jumped over the lazy dog.\n', '3. Life is like a box of chocolates.\n']
    return sorted(lines_list, key=len)

# Записуємо рядки у посортованому вигляді
async def write_lines(filename: str, lines_list: list[str]):
    async with aiofiles.open(folder_path + filename, mode='w') as f:
        for line in lines_list:
            if line.endswith('\n'):
                await f.write(line)
            else:
                await f.write(line + '\n')

# async def sort_lines_in_file(filename):
#     result = await read_lines(filename)
#     result = await sort_lines(result)
#     await write_lines(filename, result)

# 1 file -> read, sort, write

async def read_lines_in_files():
    calls = []
    for i in range(1, 6):
        filename = f'file-{i}.txt'
        calls.append(read_lines(filename))

    return await asyncio.gather(*calls)

async def sort_lines_in_files(lines_lists):
    all_sorted_lines = []
    for file_lines in lines_lists:
        sorted_lines = sort_lines(file_lines)
        all_sorted_lines.append(sorted_lines)
    return all_sorted_lines

async def write_lines_in_files(lines_lists):
    calls = []
    for i in range(1, len(lines_lists) + 1):
        filename = f'file-{i}.txt'
        calls.append(write_lines(filename, lines_lists[i - 1]))

    return await asyncio.gather(*calls)

async def sort_lines_in_all_files():
    file_lines = await read_lines_in_files()
    sorted_file_lines = await sort_lines_in_files(file_lines)
    await write_lines_in_files(sorted_file_lines)

tasks = {
    "read_files": read_lines_in_files,
    "write_files": write_lines_in_files,
    "sort files": sort_lines_in_files
}


if __name__ == '__main__':
    print(asyncio.run(sort_lines_in_all_files()))
