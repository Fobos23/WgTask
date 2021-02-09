import pytest
from task_proj.mydata.taskObjects.ship import Ship
from dbHelper import DbHelper


def ships_test_data():
    select_request = 'SELECT ship, weapon, hull, engine FROM ships'
    db_helper = DbHelper()
    ships = db_helper.select_tests_data(select_request)
    actual_ships = []
    for a_ship in ships:
        actual_ships.append(Ship(a_ship[0], a_ship[1], a_ship[2], a_ship[3]))
    return actual_ships


@pytest.fixture(scope='session', autouse=True)
def session_scope():
    db_helper = DbHelper()
    db_helper.copy_prod_db()
    yield
    db_helper.clear_test_db()


@pytest.fixture(params=ships_test_data())
def get_actual_ship(request):
    return request.param
