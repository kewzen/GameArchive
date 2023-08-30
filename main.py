import os
import sys
import aiosqlite
from asyncio import run
from colorama import init, Fore
from DataBase import DataBase
from commands import Commands


# Метод инициализации colorama
init(autoreset=True)


# Определение вызова классов чтоб не прописывать аргумент self
db = DataBase()
# Тоже самое чтобы не прописывать self
commands = Commands()


# Главное меню
async def menu():
    # Очистка консоли
    os.system("clear")
    await db.init() # - без этой функции не вызывается курсор и коннект с бд,простая инициализация
    # Вывод пунктом меню для пользователя
    print(Fore.YELLOW + """
    Выберите действие:
    [1] Список игр
    [2] Поиск игр
    [3] Добавить игру
    [4] Удалить игру
    [5] Редактирование информации об играх
    [6] Выход
    """)
    # Инпут для выбора действия
    try:
        choose_user = int(input(""))
    # Если введенно не число
    except ValueError:
        print(Fore.RED + "Несуществующие действие! Попробуйте еще раз")
        # Этот кусок выполняет перезапуск скрипта, он по всему коду. В дальнейщем его комментить смысла не вижу
        python = sys.executable
        os.execl(python, python, * sys.argv)
    match choose_user:
        # Вызов списка игр
        case 1: 
            await commands.list_of_games()
        # Вызов поиска игр
        case 2:
            await commands.search_game()
         # Вызов добавления игр
        case 3:
            await commands.add_game()
         # Вызов удаления игр
        case 4:
            await commands.delete_game()
         # Вызов редактирования игр
        case 5:
            await commands.edit_game()
         # Вызов выхода
        case 6:
            os.system("clear")
            os.abort()
        # Если не сработал не один из случаев
        case _:
            print(Fore.RED + "Произошлка ошибка! Нажмите ENTER чтоб вернуться назад") 
            input("")
            # Рестарт скрипта
            python = sys.executable
            os.execl(python, python, * sys.argv)
# Старт скрипта
if __name__ == "__main__":
    try:
        run(menu())
    # Если нет базы данных - создаем
    except aiosqlite.OperationalError:
       run(db.create_db())
       run(menu())
