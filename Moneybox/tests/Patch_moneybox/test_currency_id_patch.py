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


@allure.epic('Patch_moneybox /api/v1/moneybox/{moneybox_id}/ Проверка поля currency_id')
class TestCurrencyPatch:

    @allure.description('Существующий id')
    def test_01(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле"'):
            data = MoneyboxMethods.get_data(result_patch)
            assert data['data']['wallet']['currency_id'] == currency_id
            print('Значение поля currency_id сответствует введенному значению')

    @allure.description('Поле отсутствует')
    def test_02(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox_without_currency_id(
            moneybox_id, to_date, goal, name, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

    @allure.description('Null')
    def test_03(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, name, None, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Несуществующий id')
    def test_04(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, name, 5555, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 404)

    @allure.description('id = 0')
    def test_05(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, name, 0, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Неверный тип данных (string: "строка")')
    def test_06(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, name, 'string', is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Вещественное число (id = 2,3)')
    def test_07(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, name, 2.5, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Отрицательный id')
    def test_08(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, name, -2, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Пустое поле')
    def test_09(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, name, '', is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

