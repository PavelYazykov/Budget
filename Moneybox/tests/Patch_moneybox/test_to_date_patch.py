import json
import datetime

import allure

from common_methods.auth import Auth
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking

from common_methods.variables import MoneyboxVariables
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
is_archived = MoneyboxVariables.is_archived


@allure.epic('Patch_moneybox /api/v1/moneybox/{moneybox_id}/ Проверка поля to_date')
class TestToDate:

    @allure.description('Увеличить дату')
    def test_01(self, create_moneybox_and_delete):
        """Сoздание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, '2025-11-30', goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        data = Checking.get_data(result_patch)
        assert data['data']['to_date'] == '2025-11-30'
        print('Значение поля to_date соответствует введенному')

    @allure.description('Уменьшить дату')
    def test_02(self, create_moneybox_and_delete):
        """Сoздание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, '2029-11-30', goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        data = Checking.get_data(result_patch)
        assert data['data']['to_date'] == '2029-11-30'
        print('Значение поля to_date соответствует введенному')

    @allure.description('Поле отсутствует')
    def test_03(self, create_moneybox_and_delete):
        """Сoздание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox_without_to_date(
            moneybox_id, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

    @allure.description('Null')
    def test_04(self, create_moneybox_and_delete):
        """Сoздание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, None, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Дата в прошлом')
    def test_05(self, create_moneybox_and_delete):
        """Сoздание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, '2022-01-01', goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        if result_patch.status_code == 201:
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Текущая дата')
    def test_06(self, create_moneybox_and_delete):
        """Сoздание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        transaction_date = datetime.date.today().isoformat()
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, transaction_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        if result_patch.status_code == 201:
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Месяц больше 12 (13)')
    def test_07(self, create_moneybox_and_delete):
        """Сoздание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, '2025-13-01', goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        if result_patch.status_code == 201:
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Число больше 31 (32)')
    def test_08(self, create_moneybox_and_delete):
        """Сoздание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, '2025-12-32', goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        if result_patch.status_code == 201:
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Неверный порядок формата даты (дд-мм-гг)')
    def test_09(self, create_moneybox_and_delete):
        """Сoздание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, '01-01-2025', goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        if result_patch.status_code == 201:
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Неверный разделитель в формате даты (гггг.мм.дд)')
    def test_10(self, create_moneybox_and_delete):
        """Сoздание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, '2025.01.01', goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        if result_patch.status_code == 201:
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Неверный тип данных (string: "дата")')
    def test_11(self, create_moneybox_and_delete):
        """Сoздание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, 'string', goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        if result_patch.status_code == 201:
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Неверный тип данных (integer)')
    def test_12(self, create_moneybox_and_delete):
        """Сoздание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, 2025/11/11, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        if result_patch.status_code == 201:
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Пустое поле')
    def test_13(self, create_moneybox_and_delete):
        """Сoздание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, '', goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        if result_patch.status_code == 201:
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
        Checking.check_statuscode(result_patch, 422)