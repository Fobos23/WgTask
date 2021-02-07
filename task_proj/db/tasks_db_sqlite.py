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


def sql_db_backup(db_connection, backup_connection):
    try:
        print('Try backup...')
        with backup_connection:
            db_connection.backup(backup_connection)
        print('Backup success!')
    except Error:
        print(Error)


def sql_delete_table(connection, table_name: str):
    try:
        print(f'Try delete table: {table_name}')
        cursor_obj = connection.cursor()
        cursor_obj.execute(f'DROP table if exists {table_name}')
        print('Success!')
    except Error:
        print(Error)


def sql_select(connection, select_request: str):
    try:
        cursor_obj = connection.cursor()
        print(f'Try execute request: {select_request}')
        cursor_obj.execute(select_request)
        print('Success!')
        return tuple(cursor_obj.fetchall())
    except Error:
        print(Error)


def sql_update(connection, update_request):
    try:
        cursor_obj = connection.cursor()
        print(f'Try execute request: {update_request}')
        cursor_obj.execute(update_request)
        print('Success!')
    except Error:
        print(Error)
