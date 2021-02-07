from task_proj.environment import prod_db
from task_proj.environment import test_db
from task_proj.environment import tables_name
from task_proj.db.tasks_db_sqlite import sql_connection
from task_proj.db.tasks_db_sqlite import sql_db_backup
from task_proj.db.tasks_db_sqlite import sql_delete_table
from task_proj.db.tasks_db_sqlite import sql_update
from task_proj.db.tasks_db_sqlite import sql_select
from random import randint


class DbHelper:

    def __init__(self):
        self.prod_connection = sql_connection(prod_db)
        self.test_connection = sql_connection(test_db)

    def copy_prod_db(self):
        sql_db_backup(self.prod_connection, self.test_connection)

    def clear_test_db(self):
        for table in tables_name:
            sql_delete_table(self.test_connection, table)

    def random_update_ships(self):
        select_request = f'SELECT ship, weapon, hull, engine FROM {tables_name[0]}'
        ships = sql_select(self.test_connection, select_request)

        for ship in ships:
            i = randint(1, 3)
            if i == 1:
                update_req = f'UPDATE ships SET weapon = "weapon-{randint(1, 20)}" where ship = "{ship[0]}"'
                sql_update(self.test_connection, update_req)
            elif i == 2:
                update_req = f'UPDATE ships SET hull = "hull-{randint(1, 5)}" where ship = "{ship[0]}"'
                sql_update(self.test_connection, update_req)
            else:
                update_req = f'UPDATE ships SET engine = "engine-{randint(1, 6)}" where ship = "{ship[0]}"'
                sql_update(self.test_connection, update_req)

    def random_update_weapon(self, weapon_name: str):
        i = randint(1, 5)
        if i == 1:
            update_req = f'UPDATE weapons SET reloadSpeed = {randint(1, 20)} where weapon = "{weapon_name}"'
            sql_update(self.test_connection, update_req)
        elif i == 2:
            update_req = f'UPDATE weapons SET rotationalSpeed = {randint(1, 20)} where weapon = "{weapon_name}"'
            sql_update(self.test_connection, update_req)
        elif i == 2:
            update_req = f'UPDATE weapons SET diameter = {randint(1, 20)} where weapon = "{weapon_name}"'
            sql_update(self.test_connection, update_req)
        elif i == 2:
            update_req = f'UPDATE weapons SET powerVolley = {randint(1, 20)} where weapon = "{weapon_name}"'
            sql_update(self.test_connection, update_req)
        else:
            update_req = f'UPDATE weapons SET count = {randint(1, 20)} where weapon = "{weapon_name}"'
            sql_update(self.test_connection, update_req)

    def random_update_hull(self, hull_name):
        i = randint(1, 3)
        if i == 1:
            update_req = f'UPDATE hulls SET armor = {randint(1, 20)} where hull = "{hull_name}"'
            sql_update(self.test_connection, update_req)
        elif i == 2:
            update_req = f'UPDATE hulls SET type = {randint(1, 20)} where hull = "{hull_name}"'
            sql_update(self.test_connection, update_req)
        else:
            update_req = f'UPDATE hulls SET capacity = {randint(1, 20)} where hull = "{hull_name}"'
            sql_update(self.test_connection, update_req)

    def random_update_engine(self, engine_name):
        i = randint(1, 2)
        if i == 1:
            update_req = f'UPDATE hulls SET power = {randint(1, 20)} where engine = "{engine_name}"'
            sql_update(self.test_connection, update_req)
        else:
            update_req = f'UPDATE hulls SET type = {randint(1, 20)} where engine = "{engine_name}"'
            sql_update(self.test_connection, update_req)
