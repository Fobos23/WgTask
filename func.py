from dbHelper import DbHelper


def test_check_weapon(get_actual_ship):
    actual_ship = get_actual_ship
    select_req = f'SELECT ship, weapon FROM ships where ship="{actual_ship.name}"'
    db_helper = DbHelper()
    expect = db_helper.select_prod_data(select_req)
    assert expect[0][0] == actual_ship.name
    assert expect[0][1] == actual_ship.weapon_name

    db_helper.random_update_weapon(actual_ship.weapon_name)
    sql_request = 'SELECT weapon, reloadSpeed, rotationalSpeed, ' \
                  f'diameter, powerVolley, count FROM weapons where weapon="{actual_ship.weapon_name}"'
    actual_weapon = db_helper.select_tests_data(sql_request)
    expect_weapon = db_helper.select_prod_data(sql_request)
    assert expect_weapon[0][0] == actual_weapon[0][0]
    assert expect_weapon[0][1] == actual_weapon[0][1]
    assert expect_weapon[0][2] == actual_weapon[0][2]
    assert expect_weapon[0][3] == actual_weapon[0][3]
    assert expect_weapon[0][4] == actual_weapon[0][4]
    assert expect_weapon[0][5] == actual_weapon[0][5]


def test_check_hull(get_actual_ship):
    actual_ship = get_actual_ship
    select_req = f'SELECT ship, hull FROM ships where ship="{actual_ship.name}"'
    db_helper = DbHelper()
    expect = db_helper.select_prod_data(select_req)
    assert expect[0][0] == actual_ship.name
    assert expect[0][1] == actual_ship.hull_name


def test_check_engine(get_actual_ship):
    actual_ship = get_actual_ship
    select_req = f'SELECT ship, engine FROM ships where ship="{actual_ship.name}"'
    db_helper = DbHelper()
    expect = db_helper.select_prod_data(select_req)
    assert expect[0][0] == actual_ship.name
    assert expect[0][1] == actual_ship.engine_name
