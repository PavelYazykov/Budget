import time

import allure
import pytest

from Moneybox.methods.payloads import Payloads
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking
from common_methods.variables import MoneyboxVariables
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
amount = MoneyboxVariables.amount


@pytest.mark.post_moneybox
@allure.epic('Post_moneybox /api/v1/moneybox/ Создание копилок общие проверки')
class TestCommon:

    @allure.description('Создание новой копилки с валидными значениями (авторизованный пользователь)')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, name, currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        try:
            """Проверка наличия обязательных полей"""
            MoneyboxMethods.post_check_exist_req_fields(post_result, Payloads.required_fields())

        except AssertionError:
            print(post_result.text)
            raise AssertionError
        finally:
            """Удаление копилки"""
            with allure.step('Удаление копилки'):
                moneybox_id = MoneyboxMethods.get_moneybox_id(post_result)
                MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

    @allure.description('Создание новой копилки со значением goal меньше amount')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, 1000, name, currency_id, 2000, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 400)

    @allure.description('Создание новой копилки с валидными значениями (неавторизованный пользователь)')
    def test_03(self):
        """Запрос на создание копилки"""
        post_result = MoneyboxMethods.create_moneybox_without_auth(to_date, goal, name, currency_id, amount)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 401)

    @allure.description('Создание новой копилки без body')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox_without_body(access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Автоматическое архивирование после достижения цели и выводе средств')
    def test_05(self, auth_fixture):
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
            time.sleep(5)

            """Списание средств с копилки"""
            result_consumption = PersonalTransactionMethods.create_personal_transaction(
                1000, 'name', 'Consumption', '2024-12-12',
                None, wallet_id, 20, None, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_consumption, 201)

            """Проверка значения поля is_archived"""
            result_get = MoneyboxMethods.get_one_moneybox(moneybox_id, access_token)
            Checking.check_statuscode(result_get, 200)
            print('ЗНАЧЕНИЕ: ', result_get.text)
            print(data['data']['wallet']['is_archived'])
            data = Checking.get_data(result_get)
            assert data['data']['wallet']['is_archived'] is True

        except AssertionError:
            raise AssertionError
        finally:
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)





