import json
import datetime

import allure
import pytest

from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking
from common_methods.variables import MoneyboxVariables
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
is_archived = MoneyboxVariables.is_archived


@pytest.mark.patch_moneybox
@pytest.mark.Moneybox
@allure.epic('Patch_moneybox /api/v1/moneybox/{moneybox_id}/ Проверка поля to_date')
class TestPatchMoneyboxToDate:

    @allure.description('Проверка поля to_date - Увеличить дату')
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

    @allure.description('Проверка поля to_date - Уменьшить дату')
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

    @allure.description('Проверка поля to_date - Поле отсутствует')
    def test_03(self, create_moneybox_and_delete):
        """Сoздание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox_without_to_date(
            moneybox_id, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

    @allure.description('Проверка поля to_date - Null')
    def test_04(self, create_moneybox_and_delete):
        """Сoздание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, None, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Проверка поля to_date - Дата в прошлом')
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

    @allure.description('Проверка поля to_date - Текущая дата')
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

    @allure.description('Проверка поля to_date - Месяц больше 12 (13)')
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

    @allure.description('Проверка поля to_date - Число больше 31 (32)')
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

    @allure.description('Проверка поля to_date - Неверный порядок формата даты (дд-мм-гг)')
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

    @allure.description('Проверка поля to_date - Неверный разделитель в формате даты (гггг.мм.дд)')
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

    @allure.description('Проверка поля to_date - Неверный тип данных (string: "дата")')
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

    @allure.description('Проверка поля to_date - Неверный тип данных (integer)')
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

    @allure.description('Проверка поля to_date - Пустое поле')
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