import datetime
import json

import allure
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking

from common_methods.variables import MoneyboxVariables
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
amount = MoneyboxVariables.amount


@allure.epic('Post_moneybox /api/v1/moneybox/ Проверка поля to_date')
class TestToDate:

    @allure.description('Создание копилки с валидной датой')
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
            """Проверка значения поля дата"""
            with allure.step('Проверка значения поля to_date'):
                data = Checking.get_data(post_result)
                assert data['data']['to_date'] == to_date
                print('Значение поля соответствует введенному')
        except AssertionError:
            print(post_result.text)
            raise AssertionError
        finally:
            """Удаление копилки"""
            with allure.step('Удаление копилки'):
                moneybox_id = data['data']['id']
                MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

    @allure.description('Поле отсутствует')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox_without_to_date(
           goal, name, currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Пустое поле')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            '', goal, name, currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Null')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            None, goal, name, currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Дата в прошлом')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            '2022-01-01', goal, name, currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Текущая дата')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        transaction_date = datetime.date.today().isoformat()
        post_result = MoneyboxMethods.create_moneybox(
            transaction_date, goal, name, currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Месяц больше 12 (13)')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            '2025-13-01', goal, name, currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Число больше 31 (32)')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            '2025-12-32', goal, name, currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Неверный порядок формата даты (дд-мм-гг)')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            '01-01-2025', goal, name, currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Неверный разделитель в формате даты (гггг.мм.дд)')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            '2025.01.01', goal, name, currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Неверный тип данных (string: "дата")')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            'дата', goal, name, currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Неверный тип данных (integer)')
    def test_12(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
           2025/11/11, goal, name, currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)
