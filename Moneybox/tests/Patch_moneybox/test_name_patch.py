import json

import allure
from common_methods.variables import MoneyboxVariables
from common_methods.auth import Auth
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
is_archived = MoneyboxVariables.is_archived


@allure.epic('Patch_moneybox /api/v1/moneybox/{moneybox_id}/ Проверка поля name')
class TestNamePatch:

    @allure.description('1 символ')
    def test_01(self,  create_moneybox_and_delete):
        """Сoздание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, "М", currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            data = Checking.get_data(result_patch)
            assert data['data']['wallet']['name'] == 'М'
            print('Значение поля name соответствует введенному')

    @allure.description('19 символов')
    def test_02(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, 'Нунунунунунунунунун', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            data = Checking.get_data(result_patch)
            assert data['data']['wallet']['name'] == 'Нунунунунунунунунун'
            print('Значение поля name соответствует введенному')

    @allure.description('20 символов')
    def test_03(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, 'Нунунунунунунунунуну', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            data = Checking.get_data(result_patch)
            assert data['data']['wallet']['name'] == 'Нунунунунунунунунуну'
            print('Значение поля name соответствует введенному')

    @allure.description('Цифры (0123456789)')
    def test_04(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, '0123456789', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            data = Checking.get_data(result_patch)
            assert data['data']['wallet']['name'] == '0123456789'
            print('Значение поля name соответствует введенному')

    @allure.description('Кириллица')
    def test_05(self, auth_fixture, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, 'Счет', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            data = Checking.get_data(result_patch)
            assert data['data']['wallet']['name'] == 'Счет'
            print('Значение поля name соответствует введенному')

    @allure.description('Латиница (Moneybox)')
    def test_06(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, 'Moneybox', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            data = Checking.get_data(result_patch)
            assert data['data']['wallet']['name'] == 'Moneybox'
            print('Значение поля name соответствует введенному')

    @allure.description('Пробел')
    def test_07(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, 'Мой счёт', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            data = Checking.get_data(result_patch)
            assert data['data']['wallet']['name'] == 'Мой счёт'
            print('Значение поля name соответствует введенному')

    @allure.description('Нижнее подчеркивание')
    def test_08(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, 'Мой_счёт', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            data = Checking.get_data(result_patch)
            assert data['data']['wallet']['name'] == 'Мой_счёт'
            print('Значение поля name соответствует введенному')

    @allure.description('Тире')
    def test_09(self, auth_fixture, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, 'Мой-счёт', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            data = Checking.get_data(result_patch)
            assert data['data']['wallet']['name'] == 'Мой-счёт'
            print('Значение поля name соответствует введенному')

    @allure.description('Точка')
    def test_10(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, 'Мой.счёт', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            data = Checking.get_data(result_patch)
            assert data['data']['wallet']['name'] == 'Мой.счёт'
            print('Значение поля name соответствует введенному')

    @allure.description('Поле отсутствует')
    def test_11(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox_without_name(
            moneybox_id, to_date, goal, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

    @allure.description('Пустое поле')
    def test_12(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, '', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Null')
    def test_13(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, None, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('21 символ')
    def test_14(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, 'Нунунунунунунунунунуу', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Спецсимволы')
    def test_15(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, '@#$&%', currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)
