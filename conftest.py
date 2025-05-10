import json
import psycopg2
from Wallet.methods.wallet_methods import WalletMethods
import pytest
from common_methods.auth import Auth
from common_methods.checking import Checking
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.variables import MoneyboxVariables, DataBase
# from Users.methods.users_methods import UsersMethods
# from common_methods.variables import AuthVariables
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
def create_and_delete_users():
    result = AuthMethods.registration(
        'my_email@mail.ru', 'Ohranatruda@11', 'Иванов', 'Иван',
        'Иванович', '80000000000', '2000-10-10'
    )
    result_text = result.text
    data = json.loads(result_text)
    user_id = data['id']
    yield user_id
    with psycopg2.connect(
            host=DataBase.host,
            user=DataBase.user,
            password=DataBase.password,
            dbname=DataBase.dbname,
            port=DataBase.port
    ) as connection:
        cursor = connection.cursor()
        cursor.execute(f"""DELETE FROM settings WHERE user_id='{user_id}'""")
        connection.commit()
        cursor.execute(f"""DELETE FROM users WHERE id='{user_id}'""")
        connection.commit()
        print(f'Пользователь с id: {user_id} - удален')


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
    create_result = MoneyboxMethods.create_moneybox_without_amount(to_date, goal, name, 2, access_token)
    Checking.check_statuscode(create_result, 201)
    data = Checking.get_data(create_result)
    moneybox_id = data['data']['id']
    wallet_id = data['data']['wallet']['id']
    yield moneybox_id, access_token
    with psycopg2.connect(
            host=DataBase.host,
            user=DataBase.user,
            password=DataBase.password,
            dbname=DataBase.dbname,
            port=DataBase.port
    ) as connection:
        cursor = connection.cursor()
        cursor.execute(f"""DELETE FROM moneyboxies WHERE id={moneybox_id}""")
        cursor.execute(f"""DELETE FROM wallets WHERE id={wallet_id}""")
        connection.commit()
        print(f'Копилка с id: {moneybox_id} и wallet c {wallet_id} удалены')


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
    with psycopg2.connect(
            host=DataBase.host,
            user=DataBase.user,
            password=DataBase.password,
            dbname=DataBase.dbname,
            port=DataBase.port
    ) as connection:
        cursor = connection.cursor()
        cursor.execute(f"""DELETE FROM moneyboxies WHERE id={moneybox_id}""")
        cursor.execute(f"""DELETE FROM wallets WHERE id={wallet_id}""")
        connection.commit()
        print(f'Копилка с id: {moneybox_id} и wallet c {wallet_id} удалены')


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
    with psycopg2.connect(
            host=DataBase.host,
            user=DataBase.user,
            password=DataBase.password,
            dbname=DataBase.dbname,
            port=DataBase.port
    ) as connection:
        cursor = connection.cursor()
        cursor.execute(f"""DELETE FROM moneyboxies WHERE id={moneybox_id}""")
        cursor.execute(f"""DELETE FROM wallets WHERE id={wallet_id}""")
        connection.commit()
        print(f'Копилка с id: {moneybox_id} и wallet c {wallet_id} удалены')



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
    result_text = result_create.text
    data = json.loads(result_text)
    wallet_id = data['data']['id']
    yield access_token, wallet_id
    WalletMethods.delete_wallet_by_id(wallet_id, access_token)

