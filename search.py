from DataBase import DataBase
from colorama import init, Fore
from os import system, execl
import sys

# Объяснял в main.py
db = DataBase()


# Инициализация библиотеки colorama
init(autoreset=True)

class Search:
# Поиск игры в бд по имени
    async def search_by_name():
        await db.init()
        system("clear")
        counter = 1 # Счетчик игр
        # Входнные данные
        title = str(input(Fore.YELLOW + "Введите название игры для поиска: ")) 
        games = await db.search_by_title(title)
        print(Fore.YELLOW + f"Кол-во совпадений: {len(games)}")
        # Перебор всех игр и вывод их
        for i in games:
            print(Fore.YELLOW + f"{str(counter)}.\nНазвание: {i[0]}\nИздатель: {i[1]}\nГод издания: {i[2]}")
            counter = counter + 1
        print(Fore.LIGHTYELLOW_EX +"Чтобы вернуться назад нажмите ENTER!")
        input("")
        python = sys.executable
        execl(python, python, * sys.argv)
    # Все тоже самое что в функции выше только поиск по издателю
    async def search_by_author():
        await db.init()
        system("clear")
        counter = 1
        author = str(input(Fore.YELLOW + "Введите издателя для поиска: ")) 
        games = await db.search_by_author(author)
        print(Fore.YELLOW + f"Кол-во совпадений: {len(games)}")
        for i in games:
            print(Fore.YELLOW + f"{str(counter)}.\nНазвание: {i[0]}\nИздатель: {i[1]}\nГод издания: {i[2]}")
            counter = counter + 1
        print(Fore.LIGHTYELLOW_EX +"Чтобы вернуться назад нажмите ENTER!")
        input("")
        python = sys.executable
        execl(python, python, * sys.argv)

    # Все тоже самое что в функции выше только поиск по году издания
    async def search_by_year():
        await db.init()
        system("clear")
        counter = 1
        try:
            year = int(input(Fore.YELLOW + "Введите год для поиска: ")) 
        except:
            print(Fore.RED + "Произошла ошибка! Чтобы вернуться назад нажмите ENTER!")
            input("")
            python = sys.executable
            execl(python, python, * sys.argv)
        games = await db.search_by_year(year)
        for i in games:
            print(Fore.YELLOW + f"{str(counter)}.\nНазвание: {i[0]}\nИздатель: {i[1]}\nГод издания: {i[2]}")
            counter = counter + 1
        print(Fore.LIGHTYELLOW_EX +"Чтобы вернуться назад нажмите ENTER!")
        input("")
        python = sys.executable
        execl(python, python, * sys.argv) 

    # Все тоже самое что в функции выше только поиск по всему сразу
    async def search_by_all():
        await db.init()
        system("clear")
        counter = 1
        title = str(input(Fore.YELLOW + "Введите название игры для поиска: "))
        author = str(input(Fore.YELLOW + "Введите издателя для поиска: "))
        try:
            year = int(input(Fore.YELLOW + "Введите год для поиска: ")) 
        except:
            print(Fore.RED + "Произошла ошибка! Чтобы вернуться назад нажмите ENTER!")
            input("")
            python = sys.executable
            execl(python, python, * sys.argv)
        games = await db.search_by_all(title,author,year)
        for i in games:
            print(Fore.YELLOW + f"{str(counter)}.\nНазвание: {i[0]}\nИздатель: {i[1]}\nГод издания: {i[2]}")
            counter = counter + 1
        print(Fore.LIGHTYELLOW_EX +"Чтобы вернуться назад нажмите ENTER!")
        input("")
        python = sys.executable
        execl(python, python, * sys.argv) 

  
