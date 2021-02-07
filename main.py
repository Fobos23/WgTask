from task_proj.environment import prod_db
from task_proj.db.dbPreparer import DbPreparer
from task_proj.data.dataSetter import get_ships
from task_proj.data.dataSetter import get_weapons
from task_proj.data.dataSetter import get_hulls
from task_proj.data.dataSetter import get_engines


def create_and_fill_db():
    db_preparer = DbPreparer(prod_db)
    db_preparer.create_all_table()
    db_preparer.fill_all_table(get_ships(), get_weapons(), get_hulls(), get_engines())
    db_preparer.connection_close()


if __name__ == '__main__':
    create_and_fill_db()
