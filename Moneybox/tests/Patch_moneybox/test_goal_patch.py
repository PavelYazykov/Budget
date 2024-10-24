import json

import allure

from common_methods.auth import Auth
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking
from common_methods.variables import MoneyboxVariables
# moneybox_id = 410
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
is_archived = MoneyboxVariables.is_archived
amount = MoneyboxVariables.amount


@allure.epic('Patch_moneybox /api/v1/moneybox/{moneybox_id}/ Проверка поля goal')
class TestGoalPatch:

    @allure.description('Значение вещественное число = "400.5"')
    def test_01(self, auth_fixture, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id = create_moneybox_and_delete

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, 400.5, name, currency_id, is_archived, access_token
        )

        """Проверкра статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        data = Checking.get_data(result_patch)
        assert data['data']['goal'] == '400.50'
        print('Значение соответствует введенному')

    @allure.description('Увеличение цели')
    def test_02(self, auth_fixture, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id = create_moneybox_and_delete

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, 600, name, currency_id, is_archived, access_token
        )

        """Проверкра статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        data = Checking.get_data(result_patch)
        assert data['data']['goal'] == '600.00'
        print('Значение соответствует введенному')

    @allure.description('Уменьшение цели')
    def test_03(self, auth_fixture, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id = create_moneybox_and_delete

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, 500, name, currency_id, is_archived, access_token
        )

        """Проверкра статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        data = Checking.get_data(result_patch)
        assert data['data']['goal'] == '500.00'
        print('Значение соответствует введенному')

    @allure.description('Поле отсутствует')
    def test_04(self, auth_fixture, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id = create_moneybox_and_delete

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox_without_goal(
            moneybox_id, to_date, name, currency_id, is_archived, access_token
        )

        """Проверкра статус кода"""
        Checking.check_statuscode(result_patch, 200)

    @allure.description('Уменьшение цели ниже текущего баланса копилки')
    def test_05(self, auth_fixture, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id = create_moneybox_and_delete

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, 1, name, currency_id, is_archived, access_token
        )

        """Проверкра статус кода"""
        Checking.check_statuscode(result_patch, 400)

    @allure.description('Значение = 0')
    def test_06(self, auth_fixture, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id = create_moneybox_and_delete

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, 0, name, currency_id, is_archived, access_token
        )

        """Проверкра статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Null')
    def test_07(self, auth_fixture, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id = create_moneybox_and_delete

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, None, name, currency_id, is_archived, access_token
        )

        """Проверкра статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Отрицательное значение')
    def test_07(self, auth_fixture, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id = create_moneybox_and_delete

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, -1, name, currency_id, is_archived, access_token
        )

        """Проверкра статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Неверный тип данных (string: "цель")')
    def test_07(self, auth_fixture, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id = create_moneybox_and_delete

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, 'string', name, currency_id, is_archived, access_token
        )

        """Проверкра статус кода"""
        Checking.check_statuscode(result_patch, 422)

