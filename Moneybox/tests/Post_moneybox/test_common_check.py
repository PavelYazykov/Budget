import json

import allure
from Moneybox.methods.payloads import Payloads
from common_methods.auth import Auth
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking, Moneybox
from Auth.methods.auth_methods import AuthMethods

from common_methods.variables import MoneyboxVariables
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
amount = MoneyboxVariables.amount


@allure.epic('Post_moneybox /api/v1/moneybox/ Создание персональных транзакций общие проверки')
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

        """Проверка наличия обязательных полей"""
        with allure.step('Проверка наличия обязательных полей'):
            # result_text = post_result.text
            # data = json.loads(result_text)
            # required_fields = {
            #     "data": {
            #         "to_date": "2024-12-30",
            #         "goal": "1000.00",
            #         "wallet": {
            #             "name": "My Goal_2",
            #             "currency_id": 2,
            #             "amount": "0"
            #         }
            #     }
            # }
            #
            # for field in required_fields:
            #     assert field in data, f"Отсутствует обязательное поле: {field}"
            #     print(f'Обязательное поле {field} присутствует')
            #
            # for field in required_fields['data']:
            #     assert field in data['data'], f"Отсутствует обязательное поле: {field}"
            #     print(f'Обязательное поле {field} присутствует')
            #
            # for field in required_fields['data']['wallet']:
            #     assert field in data['data']['wallet'], f"Отсутствует обязательное поле: {field}"
            #     print(f'Обязательное поле {field} присутствует')

            check_fields = Moneybox()
        """Проверка значений обязательных полей"""
        get_data = Payloads.check_required_fields_value(
            post_result, to_date, goal, name, currency_id, amount
        )

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            result_text = post_result.text
            data = json.loads(result_text)
            moneybox_id = data['data']['id']
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
        pass





