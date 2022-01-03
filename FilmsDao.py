import mysql.connector

class FilmsDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'datarep'
        )
        # print("connection made")

    def create(self, films):
        cursor = self.db.cursor()
        sql = "insert into films (ISBN, title, director, year) values (%s,%s,%s,%s)"
        values = [
            films['ISBN'],
            films['title'],
            films['director'],
            films['year']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid


    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from films'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray= []
        print(results)
        for result in results:
            resultAsDict = self.conertToDict(result)            
            returnArray.append(resultAsDict)
        return returnArray


    def findById(self, ISBN):
        cursor = self.db.cursor()
        sql = 'select * from films where ISBN = %s'
        values = [ ISBN ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.conertToDict(result)

    def update(self, films):
        cursor = self.db.cursor()
        sql = "update films set title = %s, director = %s, year = %s where ISBN = %s"
        values = [
            films['title'],
            films['director'],
            films['year'],
            films['ISBN']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return films

    def delete(self, ISBN):
        cursor = self.db.cursor()
        sql = 'delete from films where ISBN = %s'
        values = [ISBN]
        cursor.execute(sql, values)
        return {}

    def conertToDict(self, result):
        colnames = ['ISBN','title','director','year']
        film = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                film[colName] = value
        return film


filmsDao = FilmsDao()