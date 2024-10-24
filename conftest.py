import pytest
from common_methods.auth import Auth
from common_methods.checking import Checking
from Moneybox.methods.moneybox_methods import MoneyboxMethods

to_date = '2024-12-30'
goal = 1000
name = 'name'
currency_id = 2
amount = 0


@pytest.fixture()
def auth_fixture():
    result = Auth.auth()
    Checking.check_statuscode(result, 200)
    check = result.json()
    access_token = check.get('access_token')
    return access_token


@pytest.fixture()
def auth_fixture_2():
    result = Auth.auth_2()
    Checking.check_statuscode(result, 200)
    check = result.json()
    access_token = check.get('access_token')
    return access_token


@pytest.fixture()
def create_moneybox_and_delete():
    result = Auth.auth()
    Checking.check_statuscode(result, 200)
    check = result.json()
    access_token = check.get('access_token')
    create_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, amount, access_token)
    Checking.check_statuscode(create_result, 201)
    data = Checking.get_data(create_result)
    moneybox_id = data['data']['moneybox_id']
    yield moneybox_id
    MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

@pytest.fixture()
def create_moneybox():
    result = Auth.auth()
    Checking.check_statuscode(result, 200)
    check = result.json()
    access_token = check.get('access_token')
    create_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, amount, access_token)
    Checking.check_statuscode(create_result, 201)
    data = Checking.get_data(create_result)
    moneybox_id = data['data']['moneybox_id']
    return moneybox_id
