import time

import allure
import pytest

from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking
from common_methods.variables import MoneyboxVariables
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
from common_methods.variables import PersonalTransactionVariables
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
amount = MoneyboxVariables.amount


@pytest.mark.delete_moneybox
@pytest.mark.Moneybox
@allure.epic("DELETE /api/v1/moneybox/{moneybox_id}/ Удаление копилок")
class TestDeleteMoneybox:

    @allure.description("Удаление копилки авторизованный пользователь")
    def test_01(self, create_moneybox):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox

        """Delete запрос"""
        result_delete = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 204)

        """Подтверждение удаления"""
        with allure.step('Подтверждение удаления'):
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            Checking.check_statuscode(result_delete, 404)

    @allure.description("Удаление копилки неавторизованный пользователь")
    def test_02(self, create_moneybox):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox
        try:
            """Delete запрос"""
            result_delete = MoneyboxMethods.delete_moneybox_wo_access_token(moneybox_id)

            """Проверка статус кода"""
            Checking.check_statuscode(result_delete, 401)
        finally:

            """Удаление"""
            with allure.step('удаление копилки после теста'):
                result_delete = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
                Checking.check_statuscode(result_delete, 204)

    @allure.description("Удаление копилки - Несуществующий id")
    def test_03(self, auth_fixture):
        """Создание копилки"""
        access_token = auth_fixture

        """Delete запрос"""
        result_delete = MoneyboxMethods.delete_moneybox(300, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 404)

    @allure.description("Удаление копилки - id = 0")
    def test_04(self, auth_fixture):
        """Создание копилки"""
        access_token = auth_fixture

        """Delete запрос"""
        result_delete = MoneyboxMethods.delete_moneybox(0, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description("Удаление копилки - id = вещественное число")
    def test_05(self, auth_fixture):
        """Создание копилки"""
        access_token = auth_fixture

        """Delete запрос"""
        result_delete = MoneyboxMethods.delete_moneybox(1.1, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description("Удаление копилки - id = отрицательное число число")
    def test_06(self, auth_fixture):
        """Создание копилки"""
        access_token = auth_fixture

        """Delete запрос"""
        result_delete = MoneyboxMethods.delete_moneybox(-30, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description("Удаление копилки -id = string")
    def test_07(self, auth_fixture):
        """Создание копилки"""
        access_token = auth_fixture

        """Delete запрос"""
        result_delete = MoneyboxMethods.delete_moneybox('string', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description("Удаление копилки - id = Null")
    def test_08(self, auth_fixture):
        """Создание копилки"""
        access_token = auth_fixture

        """Delete запрос"""
        result_delete = MoneyboxMethods.delete_moneybox(None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description("Удаление копилки - id = Спецсимволы")
    def test_09(self, auth_fixture):
        """Создание копилки"""
        access_token = auth_fixture

        """Delete запрос"""
        result_delete = MoneyboxMethods.delete_moneybox('!@#$%^', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description("Удаление копилки с положительным балансом")
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        create_result = MoneyboxMethods.create_moneybox(
            to_date, goal, name, currency_id, 10, access_token
        )
        Checking.check_statuscode(create_result, 201)
        data = Checking.get_data(create_result)
        moneybox_id = data['data']['id']
        try:
            """Delete запрос"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result_delete, 400)
        finally:
            """Удаление"""
            with allure.step('удаление копилки после теста'):
                MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

