import time

import allure
import pytest
from common_methods.auth import Auth
from Moneybox.methods.payloads import Payloads
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking
from common_methods.variables import MoneyboxVariables, AuthVariables
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
from Auth.methods.auth_methods import AuthMethods
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
is_archived = MoneyboxVariables.is_archived
amount = MoneyboxVariables.amount


@pytest.mark.patch_moneybox
@pytest.mark.Moneybox
@allure.epic('Patch_moneybox /api/v1/moneybox/{moneybox_id}/ Редактирование копилок, общие проверки')
class TestMoneyboxCommonPatch:

    @allure.description('С существующим ID и валидными значениями в полях (авторизованный пользователь')
    def test_01(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка наличия обязательных полей"""
        MoneyboxMethods.post_check_exist_req_fields(result_patch, Payloads.required_fields())

    @allure.description('С существующим ID и валидными значениями в полях (неавторизованный пользователь')
    def test_02(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox_without_auth(
            moneybox_id, to_date, goal, name, currency_id, is_archived
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 401)

    @allure.description('C пустым body')
    def test_03(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox_without_body(moneybox_id, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Несуществующий id')
    def test_04(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            '1', to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 404)

    @allure.description('id = 0')
    def test_05(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            '0', to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('id = вещественное число (1,5)')
    def test_06(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            '1.5', to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('id = -1')
    def test_07(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            '-1', to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('id = -1')
    def test_08(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            '-1', to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('id = string ("строка")')
    def test_09(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            'string', to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Отсутствует id')
    def test_10(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox_without_moneybox_id(
            to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 405)

    @allure.description('Null')
    def test_11(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            None, to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Попытка внести изменения в копилку после достижения цели')
    def test_12(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_create = MoneyboxMethods.create_moneybox(
            to_date, 1000, 'name', 2, 0, access_token
        )

        """Получение moneybox_id и wallet_id"""
        data = Checking.get_data(result_create)
        moneybox_id = data['data']['id']
        wallet_id = data['data']['wallet']['id']
        try:
            """Создание транзакции"""
            result_income = PersonalTransactionMethods.create_personal_transaction(
                1000, 'description', 'Income', '2024-12-12',
                None, wallet_id, 30, None, access_token
            )
            Checking.check_statuscode(result_income, 201)
            result_get = MoneyboxMethods.get_one_moneybox(moneybox_id, access_token)
            Checking.check_statuscode(result_get, 200)

            """Запрос на изменение копилки"""
            result_change = MoneyboxMethods.change_moneybox(
                moneybox_id, to_date, 2000, name, currency_id, False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 400)
        finally:
            """Удаление копилки"""
            with allure.step('удаление копилки после теста'):
                MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('Редактирование чужой копилки')
    def test_13(self, create_moneybox_and_delete):

        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Создание второго пользователя"""
        result_create_second_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_second_user, 201)
        data, user_id = AuthMethods.get_id(result_create_second_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Авторизация второго пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token_2 = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Запрос на редактирование чужой копилки"""
            result_change = MoneyboxMethods.change_moneybox(
                moneybox_id, '2030-12-12', 1000, 'name_2', 2, False, access_token_2
            )
            Checking.check_statuscode(result_change, 200)

        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)
