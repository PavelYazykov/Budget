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


@allure.epic('Patch_moneybox /api/v1/moneybox/{moneybox_id}/ Редактирование копилок, общие проверки')
class TestCommonPatch:

    @allure.description('С существующим ID и валидными значениями в полях (авторизованный пользователь')
    def test_01(self, auth_fixture, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id = create_moneybox_and_delete

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка наличия обязательных полей"""
        with allure.step('Проверка наличия обязательных полей'):
            result_text = result_patch.text
            data = json.loads(result_text)
            required_fields = {
                "data": {
                    "to_date": "2024-12-30",
                    "goal": "1000.00",
                    "wallet": {
                        "name": "My Goal_2",
                        "currency_id": 2,
                        "amount": "0"
                    }
                }
            }

            for field in required_fields:
                assert field in data, f"Отсутствует обязательное поле: {field}"
                print(f'Обязательное поле {field} присутствует')

            for field in required_fields['data']:
                assert field in data['data'], f"Отсутствует обязательное поле: {field}"
                print(f'Обязательное поле {field} присутствует')

            for field in required_fields['data']['wallet']:
                assert field in data['data']['wallet'], f"Отсутствует обязательное поле: {field}"
                print(f'Обязательное поле {field} присутствует')

    @allure.description('С существующим ID и валидными значениями в полях (неавторизованный пользователь')
    def test_02(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox_without_auth(
            moneybox_id, to_date, goal, name, currency_id, is_archived
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 401)

    @allure.description('C пустым body')
    def test_03(self, auth_fixture, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id = create_moneybox_and_delete

        """Авторизация"""
        access_token = auth_fixture

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

    @allure.description('Пустое поле')
    def test_10(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            '', to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Отсутствует id')
    def test_11(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox_without_moneybox_id(
            to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Null')
    def test_12(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            None, to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Попытка внести изменения в копилку после достижения цели')
    def test_13(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        pass

    @allure.description('Редактирование чужой копилки')
    def test_14(self, auth_fixture):
        pass
