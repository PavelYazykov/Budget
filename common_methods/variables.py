import datetime


class CommonVariables:
    base_url = 'https://budget-test.god-it.ru/api'


class AuthVariables:
    """Авторизация"""
    auth_payloads = 'username=y.pawel_test1@mail.ru&password=Ohranatruda@1'
    auth_payloads_2 = 'username=zx5@mail.ru&password=Samsung@9@9@9'
    auth_payloads_3 = 'username=pawel_test_1@rambler.ru&password=Ohranatruda@2'

    """Верифицированный пользователь_1"""
    email = 'y.pawel_test1@mail.ru'
    password = 'Ohranatruda@1'
    phone = '89260000002'
    user_id_verify = '942ffa16-1790-453c-8663-92a2559a8654'
    verify_user_phone = '7741e39b-a66a-45f3-a465-f7ca8e7c7eab'  # id верифицированного пользователя

    """Верифицированный пользователь_2"""
    email_2 = 'pawel_test_1@rambler.ru'
    password_2 = 'Ohranatruda@2'
    phone_2 = '89260000004'
    user_id_verify_2 = '9e7f47bc-f3f0-43eb-aa83-090406e4480d'

    """Неверифицированный пользователь"""
    not_verify_email = 'bmk20284@nowni.com'
    not_verify_phone = '89260000004'
    user_id_not_verify = '590faefa-472e-448a-a608-dd0c63a23458'
    not_verify_phone_user_id = '590faefa-472e-448a-a608-dd0c63a23458'  # id неверифицированного пользователя

    """Данные для регистрации пользователя"""
    email_for_create_user = 'qa-a@mail.ru'
    password_for_create_user = 'Samsung@9@9@9'
    last_name = 'Иванов'
    first_name = 'Иван'
    middle_name = 'Иванович'
    phone_for_create_user = '89280000000'
    date_of_birth = '2000-01-01'

    user_id_exist = '590faefa-472e-448a-a608-dd0c63a23458'
    user_id_not_exist = '590faefa-472e-448a-a608-dd0c63a99999'


class MoneyboxVariables:
    to_date = '2030-12-30'
    goal = 1000
    name = 'name'
    currency_id = 2
    is_archived = False
    amount = 0


class PersonalTransactionVariables:
    transaction_date = datetime.date.today().isoformat()
    amount = 0
    description = 'transaction'
    transaction_type_income = 'Income'
    transaction_type_consume = 'Consumption'
    transaction_type_tbw = 'Transfer between wallets'
    transaction_date = transaction_date
    category_id_income = 156
    category_id_consume = 136
