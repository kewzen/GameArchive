from colorama import init, Fore
import aiosqlite
from asyncio import run
# Инициализация библиотеки colorama
init(autoreset=True)
# Методы базы данных
class DataBase:
    # Только создание параметров кусора и коннекта 
    # Есть функция init т.к в __init__ нельзя вернуть корутину
    def __init__(self):
        self.conn = None
        self.cursor = None
# Иницализация
    async def init(self):
        self.conn = await aiosqlite.connect("base.db")
        self.cursor = await self.conn.cursor()
# Создание таблицы
    async def create_db(self):
        await self.cursor.execute("CREATE TABLE IF NOT EXISTS games(gamesTitle TEXT, authorName TEXT, yearOfCreate INTEGER)")
# Получение всех игр
    async def all_games(self):
        await self.cursor.execute("SELECT * from games")
        games = await self.cursor.fetchall()
        return games
# Добавление игры в базу
    async def add_games(self, title: str, author: str, year: int):
        await self.cursor.execute("INSERT INTO games VALUES (?,?,?)", (title, author, year))
        await self.conn.commit()
# Поиск по названию игры
    async def search_by_title(self, title: str):
        await self.cursor.execute("SELECT * FROM games WHERE gamesTitle = ?",(title,))
        games = await self.cursor.fetchall()
        return games
# Поиск по издателю игры
    async def search_by_author(self,author: str):
        await self.cursor.execute("SELECT * FROM games WHERE authorName = ?",(author,))
        games = await self.cursor.fetchall()
        return games
# Поиск по году издания игры
    async def search_by_year(self,year: int):
        await self.cursor.execute("SELECT * FROM games WHERE yearOfCreate = ?",(year,))
        games = await self.cursor.fetchall()
        return games
# Поиск по всему сразу
    async def search_by_all(self, title:str,author:str,year:int):
        await self.cursor.execute("SELECT * FROM games WHERE gamesTitle = ? AND authorName = ? AND yearOfCreate = ?",(title,author,year))
        games = await self.cursor.fetchall()
        return games
# Удаление игры
    async def delete_game(self,title:str,author:str,year:int):
        await self.cursor.execute("DELETE FROM games WHERE gamesTitle = ? AND authorName = ? AND yearOfCreate = ?", (title,author,year))
        await self.conn.commit()
# Редактирование названия
    async def edit_title(self, title:str,author: str, year: int, change: str):
        await self.cursor.execute("UPDATE games SET gamesTitle = ? WHERE gamesTitle = ? AND authorName = ? AND yearOfCreate = ?",(change,title,author,year))
        await self.conn.commit()
# Редактирование издателя
    async def edit_author(self, title:str,author: str, year: int, change: str):
        await self.cursor.execute("UPDATE games SET authorName = ? WHERE gamesTitle = ? AND authorName = ? AND yearOfCreate = ?",(change,title,author,year))
        await self.conn.commit()
# Редактирование года издания
    async def edit_year(self, title:str,author: str, year: int, change: int):
        await self.cursor.execute("UPDATE games SET yearOfCreate = ? WHERE gamesTitle = ? AND authorName = ? AND yearOfCreate = ?",(change,title,author,year))
        await self.conn.commit()


# Блок инициализации
db = DataBase()
async def main():
    await db.init()
if __name__ == "__main__":
    run(main())
    
