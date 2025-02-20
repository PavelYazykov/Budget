import json
from Wallet.methods.wallet_methods import WalletMethods
import pytest
from common_methods.auth import Auth
from common_methods.checking import Checking
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.variables import MoneyboxVariables
from Users.methods.users_methods import UsersMethods
from common_methods.variables import AuthVariables
from Auth.methods.auth_methods import AuthMethods
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
amount = MoneyboxVariables.amount


@pytest.fixture()
def auth_fixture():
    result = Auth.auth()
    Checking.check_statuscode(result, 200)
    check = result.json()
    access_token = check.get('access_token')
    return access_token


@pytest.fixture()
def auth_fixture_for_users_check_email():
    result = Auth.auth()
    Checking.check_statuscode(result, 200)
    check = result.json()
    access_token = check.get('access_token')
    yield access_token
    UsersMethods.change_user_email(
        'y.pawel_test1@mail.ru',
        access_token
    )
    result_get_code = AuthMethods.request_verify_code(AuthVariables.user_id_verify)
    Checking.check_statuscode(result_get_code, 200)
    code = AuthMethods.get_verify_code(result_get_code)
    result_verify = AuthMethods.verify(AuthVariables.user_id_verify, code)
    Checking.check_statuscode(result_verify, 200)


@pytest.fixture()
def create_and_delete_users():
    result = AuthMethods.registration(
        'my_email@mail.ru', 'Ohranatruda@11', 'Иванов', 'Иван',
        'Иванович', '80000000000', '2000-10-10'
    )
    result_text = result.text
    data = json.loads(result_text)
    user_id = data['id']
    yield user_id
    AuthMethods.delete_user('my_email@mail.ru')


@pytest.fixture()
def create_users():
    result = AuthMethods.registration(
        'm_email@mail.ru', 'Ohranatruda@11', 'Иванов', 'Иван',
        'Иванович', '81000000000', '2000-10-10'
    )
    result_text = result.text
    data = json.loads(result_text)
    user_id = data['id']
    return user_id


@pytest.fixture()
def create_moneybox_and_delete():
    result = Auth.auth()
    Checking.check_statuscode(result, 200)
    check = result.json()
    access_token = check.get('access_token')
    create_result = MoneyboxMethods.create_moneybox(to_date, goal, name, 2, amount, access_token)
    Checking.check_statuscode(create_result, 201)
    data = Checking.get_data(create_result)
    moneybox_id = data['data']['id']
    yield moneybox_id, access_token
    MoneyboxMethods.delete_moneybox(moneybox_id, access_token)


@pytest.fixture()
def create_moneybox_and_delete_for_personal_transaction():
    result = Auth.auth()
    Checking.check_statuscode(result, 200)
    check = result.json()
    access_token = check.get('access_token')
    create_result = MoneyboxMethods.create_moneybox(to_date, goal, name, 2, amount, access_token)
    Checking.check_statuscode(create_result, 201)
    data = Checking.get_data(create_result)
    moneybox_id = data['data']['id']
    wallet_id = data['data']['wallet']['id']
    yield moneybox_id, wallet_id, access_token
    MoneyboxMethods.delete_moneybox(moneybox_id, access_token)


@pytest.fixture()
def create_moneybox_and_delete_for_analytics():
    result = Auth.auth()
    Checking.check_statuscode(result, 200)
    check = result.json()
    access_token = check.get('access_token')
    create_result = MoneyboxMethods.create_moneybox(to_date, goal, name, 2, 100, access_token)
    Checking.check_statuscode(create_result, 201)
    data = Checking.get_data(create_result)
    moneybox_id = data['data']['id']
    wallet_id = data['data']['wallet']['id']
    yield moneybox_id, wallet_id, access_token
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
    moneybox_id = data['data']['id']
    return moneybox_id, access_token


@pytest.fixture()
def create_and_delete_wallet():
    result_auth = Auth.auth()
    access_token = result_auth.json().get('access_token')
    result_create = WalletMethods.create_wallet(
        'wallet_Pavel', 2, 0, access_token
    )
    print(result_create.text)
    result_text = result_create.text
    data = json.loads(result_text)
    wallet_id = data['data']['id']
    print(wallet_id)
    yield access_token, wallet_id
    WalletMethods.delete_wallet_by_id(wallet_id, access_token)

