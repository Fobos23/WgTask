from environment import prod_db
from dbPreparer import DbPreparer
from task_proj.mydata.dataSetter import get_ships
from task_proj.mydata.dataSetter import get_weapons
from task_proj.mydata.dataSetter import get_hulls
from task_proj.mydata.dataSetter import get_engines
from dbHelper import DbHelper


def create_and_fill_db():
    db_preparer = DbPreparer(prod_db)
    db_preparer.create_all_table()
    db_preparer.fill_all_table(get_ships(), get_weapons(), get_hulls(), get_engines())
    db_preparer.connection_close()

    db_helper = DbHelper()
    db_helper.copy_prod_db()


if __name__ == '__main__':
    create_and_fill_db()
