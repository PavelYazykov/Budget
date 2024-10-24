import json

import allure

from common_methods.auth import Auth
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking

moneybox_id = 410
to_date = '2024-12-30'
goal = 1000
name = 'name'
currency_id = 2
is_archived = False


@allure.epic('Patch_moneybox /api/v1/moneybox/{moneybox_id}/ Проверка поля name')
class TestNamePatch:

    @allure.description('1 символ')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, "М", currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)
        print(result_patch.text)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            result_text = result_patch.text
            data = json.loads(result_text)
            assert data['data']['wallet']['name'] == 'М'
            print('Значение поля name соответствует введенному')

    @allure.description('19 символов')
    def test_02(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, 'Нунунунунунунунунун', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)
        print(result_patch.text)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            result_text = result_patch.text
            data = json.loads(result_text)
            assert data['data']['wallet']['name'] == 'Нунунунунунунунунун'
            print('Значение поля name соответствует введенному')

    @allure.description('20 символов')
    def test_03(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, 'Нунунунунунунунунуну', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)
        print(result_patch.text)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            result_text = result_patch.text
            data = json.loads(result_text)
            assert data['data']['wallet']['name'] == 'Нунунунунунунунунуну'
            print('Значение поля name соответствует введенному')

    @allure.description('Цифры (0123456789)')
    def test_04(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, '0123456789', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)
        print(result_patch.text)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            result_text = result_patch.text
            data = json.loads(result_text)
            assert data['data']['wallet']['name'] == '0123456789'
            print('Значение поля name соответствует введенному')

    @allure.description('Кириллица (Счёт)')
    def test_05(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, 'Счёт', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)
        print(result_patch.text)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            result_text = result_patch.text
            data = json.loads(result_text)
            assert data['data']['wallet']['name'] == 'Счёт'
            print('Значение поля name соответствует введенному')

    @allure.description('Латиница (Moneybox)')
    def test_06(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, 'Moneybox', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)
        print(result_patch.text)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            result_text = result_patch.text
            data = json.loads(result_text)
            assert data['data']['wallet']['name'] == 'Moneybox'
            print('Значение поля name соответствует введенному')

    @allure.description('Пробел')
    def test_07(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, 'Мой счёт', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)
        print(result_patch.text)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            result_text = result_patch.text
            data = json.loads(result_text)
            assert data['data']['wallet']['name'] == 'Мой счёт'
            print('Значение поля name соответствует введенному')

    @allure.description('Нижнее подчеркивание')
    def test_08(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, 'Мой_счёт', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)
        print(result_patch.text)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            result_text = result_patch.text
            data = json.loads(result_text)
            assert data['data']['wallet']['name'] == 'Мой_счёт'
            print('Значение поля name соответствует введенному')
