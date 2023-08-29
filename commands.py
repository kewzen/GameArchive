from types import coroutine
from DataBase import DataBase
from colorama import init, Fore
from os import system, execl
import sys
from collections.abc import Coroutine
from search import search


# Инициализация библиотеки colorama 
init(autoreset=True)


# Объяснение этого прописано в main.py
db = DataBase()



class Commands:
    # Добавление игры
    async def add_game(self):
        system("clear")
        await db.init()
        # Входные данные
        title = input(Fore.YELLOW + "Введите название игры: ")
        author = input(Fore.YELLOW + "Введите издателя игры: ")
        try:
            year = int(input(Fore.YELLOW + "Введите год издания игры: "))
            print(Fore.LIGHTYELLOW_EX + "Игра добавлена!\n" + Fore.YELLOW + f"Название: {title}\nИздатель: {author}\nГод издания: {year}")
            await db.add_games(title,author,year)
            print(Fore.LIGHTYELLOW_EX +"Чтобы вернуться назад нажмите ENTER!")
            input("")
            python = sys.executable
            execl(python, python, * sys.argv) 
        # Если введено не число
        except:
            print(Fore.RED + "Введите правильный год издания! Нажмите ENTER чтоб вернуться назад") 
            input("")
            python = sys.executable
            execl(python, python, * sys.argv)
    # Список игр
    async def list_of_games(self):
        system("clear")
        await db.init()
        counter = 1 # Счетчик для вывода игр
        games = await db.all_games()
        # Проверка есть ли вообще игры в базе
        if len(games) == 0:
            print(Fore.RED + "Вы еще не добавили ни одной игры! Чтобы вернуться назад нажмите ENTER")
            input("")
            python = sys.executable
            execl(python, python, * sys.argv)
        for i in games:
            print(Fore.YELLOW + f"{str(counter)}.\nНазвание: {i[0]}\nИздатель: {i[1]}\nГод издания: {i[2]}")
            counter = counter + 1
        print(Fore.LIGHTMAGENTA_EX + f"Всего игр в базе:{len(games)}")
        print(Fore.LIGHTYELLOW_EX +"Чтобы вернуться назад нажмите ENTER!")
        input("")
        python = sys.executable
        execl(python, python, * sys.argv) 
     # Поиск игр
    async def search_game(self):
        system("clear")
        await db.init()
        print(Fore.YELLOW + """
    Выберите критерии поиска:
    [1] Поиск по названию
    [2] Поиск по издателю
    [3] Поиск по году издания
    [4] Поиск по всем параметрам
    [5] Выход
         """)
        # Выбор юзера по каким критериям будет идти поиск
        choose_of_search = int(input(""))
        match choose_of_search:
            # По названию
            case 1:
                await search.search_by_name()
            # По издателю
            case 2:
                await search.search_by_author() 
            # По году издания
            case 3:
                await search.search_by_year() 
            # По всему сразу
            case 4:
                await search.search_by_all()
            # Вызов выхода
            case 5:
                python = sys.executable
                execl(python, python, * sys.argv)
            # Если не сработал не один случай
            case _:
                print(Fore.RED + "Произошлка ошибка! Нажмите ENTER чтоб вернуться назад") 
                input("")
                python = sys.executable
                execl(python, python, * sys.argv)
    # Удаление игр
    async def delete_game(self):
        await db.init()
        system("clear")
        # Входные данные
        title = str(input(Fore.YELLOW +"Введите название игры для удаления: "))
        author = str(input(Fore.YELLOW + "Введите издателя игры для удаления: "))
        try:
            year = int(input(Fore.YELLOW + "Введите год издания игры для поиска: "))
        # Если введенно не число
        except:
            print(Fore.RED + "Введите правильный год издания! Нажмите ENTER чтоб вернуться назад") 
            input("")
            python = sys.executable
            execl(python, python, * sys.argv)
        games = await db.search_by_all(title,author,year)
        # Проверка есть ли игра на удаление
        if len(games) > 0: 
            await db.delete_game(title,author,year)
            print (Fore.YELLOW + f"Игра {title} удалена!")
            print(Fore.LIGHTYELLOW_EX +"Чтобы вернуться назад нажмите ENTER!")
            input("")
            python = sys.executable
            execl(python, python, * sys.argv) 
        else:
            print(Fore.RED +"Игра не найдена,чтобы вернуться назад нажмите ENTER!")
            input("")
            python = sys.executable
            execl(python, python, * sys.argv)
# Редактирование игр
    async def edit_game(self):
        await db.init()
        system("clear")
        # Входные данные для поиска игры которую редактируем
        title = str(input(Fore.YELLOW +"Введите название игры для редактирования: "))
        author = str(input(Fore.YELLOW + "Введите издателя игры для редактирования: "))
        try:
            year = int(input(Fore.YELLOW + "Введите год издания игры для редактирования: "))
        # Если введенно не число
        except:
            print(Fore.RED + "Введите правильный год издания! Нажмите ENTER чтоб вернуться назад") 
            input("")
            python = sys.executable
            execl(python, python, * sys.argv)
        # Ищем игру для проверки есть ли она в базе
        games = await db.search_by_all(title,author,year)
        # Если все таки игра есть
        if len(games) > 0: 
            print(Fore.YELLOW + f"""
        Название: {games[0][0]}
        Издатель: {games[0][1]}
        Год издания:{games[0][2]}
                  """)
            print(Fore.LIGHTYELLOW_EX +"Чтобы перейти к редактированию игры нажмите ENTER!")
            input("")
            system("clear") 
            print (Fore.YELLOW + f"""
        Выберите параметр для редактирования:
        [1] Название 
        [2] Издатель
        [3] Год издания
                   """)
            # Выбор пользователя параметра для изменения
            choose_of_edit = int(input(""))
            system("clear")
            match choose_of_edit:
            # Изменить название
                case 1:
                    change = input(Fore.YELLOW + "Введите новое название: ")
                    await db.edit_title(title,author,year,change)
            # Изменить издателя                                                               # - change - это то на что меняем
                case 2:
                    change = input(Fore.YELLOW + "Введите нового издателя: ")
                    await db.edit_author(title,author,year,change)
            # Изменить год издания
                case 3:
                    try:
                        change = int(input(Fore.YELLOW + "Введите новый год издания: "))
                        await db.edit_year(title,author,year,change)
                    # Если введено не число
                    except:
                        print(Fore.RED + "Введите правильный год издания! Нажмите ENTER чтоб вернуться назад") 
                        input("")
                        python = sys.executable
                        execl(python, python, * sys.argv)
            # Если не сработал не один из случаев
                case _:
                    print(Fore.RED + "Произошлка ошибка! Нажмите ENTER чтоб вернуться назад") 
                    input("")
                    python = sys.executable
                    execl(python, python, * sys.argv)
            print(Fore.LIGHTYELLOW_EX +"Чтобы вернуться назад нажмите ENTER!")
            input("")
            python = sys.executable
            execl(python, python, * sys.argv) 
        # Если игры все же нет в базе
        else:
            print(Fore.RED +"Игра не найдена,чтобы вернуться назад нажмите ENTER!")
            input("")
            python = sys.executable
            execl(python, python, * sys.argv) 
