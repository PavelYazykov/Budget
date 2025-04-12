import json

import allure
import pytest

from common_methods.auth import Auth
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking


from common_methods.variables import MoneyboxVariables
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
amount = MoneyboxVariables.amount


@pytest.mark.post_moneybox
@allure.epic('Post_moneybox /api/v1/moneybox/ Проверка поля goal')
class TestPostMoneyboxGoal:

    @allure.description('Проверка поля goal - Значение целое число = 1')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, 1, name, currency_id, amount, access_token)
        moneybox_id = MoneyboxMethods.get_moneybox_id(post_result)
        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        try:
            """Проверка значения поля goal"""
            with allure.step('Проверка значения поля goal'):
                data = Checking.get_data(post_result)
                assert data['data']['goal'] == '1.00'
                print('Значение поля соответствует введенному')
        finally:
            """Удаление копилки"""
            with allure.step('Удаление копилки'):
                MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('Проверка поля goal - Значение вещественное число = 0.01')
    def test_02(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, 0.01, name, currency_id, amount, access_token)
        moneybox_id = MoneyboxMethods.get_moneybox_id(post_result)
        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        try:
            """Проверка значения поля goal"""
            with allure.step('Проверка значения поля goal'):
                data = Checking.get_data(post_result)
                assert data['data']['goal'] == '0.01'
                print('Значение поля соответствует введенному')
        finally:
            """Удаление копилки"""
            with allure.step('Удаление копилки'):
                MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('Проверка поля goal - Значение = 0')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, 0, name, currency_id, amount, access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Проверка поля goal - Поле отсутствует')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox_without_goal(to_date, name, currency_id, amount, access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Проверка поля goal - Пустое поле')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, '', name, currency_id, amount, access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Проверка поля goal - Null')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, None, name, currency_id, amount, access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Проверка поля goal  - Отрицательное значение')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, -1, name, currency_id, amount, access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Проверка поля goal - Неверный тип данных (string)')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, 'цель', name, currency_id, amount, access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)
