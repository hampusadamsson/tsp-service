import json
import sqlite3
import datetime

from src.Configuration import Configuration


db_name = Configuration().path_to_db


def query(q):
    records = ''
    try:
        sqliteConnection = sqlite3.connect(db_name)
        cursor = sqliteConnection.cursor()
        cursor.execute(q)
        records = cursor.fetchall()
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
        return records


def insert_new_highscore(name, score, solution):
    solution = [int(s) for s in solution]
    dateandtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    sqlite_insert_query = """INSERT INTO highscore (name, score, dateandtime, solution) VALUES ('{}', {}, '{}', '{}');""".format(name, score, dateandtime, solution)
    query(sqlite_insert_query )


def create_database():
    sqlite_create_table_query = '''CREATE TABLE highscore (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                dateandtime TEXT,
                                score DOUBLE,
                                solution TEXT);'''
    query(sqlite_create_table_query)


def drop_table():
    drop_query = '''DROP TABLE highscore;'''
    query(drop_query)


def get_highscore():
    sqlite_select_query = """SELECT name, score, dateandtime from highscore ORDER BY score LIMIT 100;"""
    records = query(sqlite_select_query)
    return json.dumps(records)

"""
drop_table()
create_database()
insert_new_highscore("Gösta", 14, "12341231")
insert_new_highscore("Rasmus", 4, "123412")
insert_new_highscore("Adam", 13, "1231")
insert_new_highscore("hampus", 9, "213123")
get_highscore()
drop_table()
create_database()
"""
