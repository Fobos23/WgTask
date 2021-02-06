import sqlite3
from sqlite3 import Error


def sql_connection(db_name: str):
    try:
        print(f'Try connect to db: {db_name}')
        connection = sqlite3.Connection(db_name)
        print('Connection success!')
        return connection
    except Error:
        print(Error)


def sql_add_table(connection, sql_request: str):
    try:
        cursor_obj = connection.cursor()
        print(f'Try execute request: {sql_request}')
        cursor_obj.execute(sql_request)
        print('Success!')
        connection.commit()
    except Error:
        print('Table already exist')


def sql_add_data(connection, sql_request: str):
    try:
        cursor_obj = connection.cursor()
        print(f'Try execute request: {sql_request}')
        cursor_obj.execute(sql_request)
        print('Success!')
    except Error:
        print(Error)
