from tasks_db_sqlite import sql_connection
from tasks_db_sqlite import sql_add_table
from tasks_db_sqlite import sql_add_data


class DbPreparer:

    def __init__(self, db_name: str):
        self.connection = sql_connection(db_name)

    def create_all_table(self):
        ships_request = 'CREATE TABLE ships(ship text PRIMARY KEY, weapon text, hull text, engine text)'
        sql_add_table(self.connection, ships_request)

        weapons_request = 'CREATE TABLE weapons(weapon text PRIMARY KEY, reloadSpeed integer, rotationalSpeed integer, ' \
                          'diameter integer, powerVolley integer, count integer) '
        sql_add_table(self.connection, weapons_request)

        hulls_request = 'CREATE TABLE hulls(hull text PRIMARY KEY, armor integer, type integer, capacity integer)'
        sql_add_table(self.connection, hulls_request)

        engines_request = 'CREATE TABLE engines(engine text PRIMARY KEY, power integer, type integer)'
        sql_add_table(self.connection, engines_request)

    def fill_all_table(self, ships, weapons, hulls, engines):
        for ship in ships:
            ship_request = f'INSERT INTO ships VALUES("{ship.name}", "{ship.weapon_name}", "{ship.hull_name}", "{ship.engine_name}")'
            sql_add_data(self.connection, ship_request)

        for weapon in weapons:
            weapon_request = f'INSERT INTO weapons VALUES("{weapon.name}", {weapon.rel_speed}, {weapon.rot_speed}, {weapon.diam}, {weapon.power_vol}, {weapon.count})'
            sql_add_data(self.connection, weapon_request)

        for hull in hulls:
            hull_request = f'INSERT INTO hulls VALUES("{hull.name}", {hull.armor}, {hull.hull_type}, {hull.capacity})'
            sql_add_data(self.connection, hull_request)

        for engine in engines:
            engine_request = f'INSERT INTO engines VALUES("{engine.name}", {engine.power}, {engine.eng_type})'
            sql_add_data(self.connection, engine_request)

    def connection_close(self):
        self.connection.close()
