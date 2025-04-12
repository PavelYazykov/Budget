import json

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
amount = MoneyboxVariables.amount


@pytest.mark.patch_moneybox
@pytest.mark.Moneybox
@allure.epic('Patch_moneybox /api/v1/moneybox/{moneybox_id}/ Проверка поля is_archived')
class TestPatchMoneyboxIsArchived:

    @allure.description('Проверка поля is_archived - Перенос копилки в архив')
    def test_01(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        with allure.step('Перенос копилки в архив'):
            result_patch = MoneyboxMethods.change_moneybox(
                moneybox_id, to_date, goal, name, currency_id, True, access_token
            )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            data = Checking.get_data(result_patch)
            print('Data', data)
            assert data['data']['wallet']['is_archived'] is True
            print('Значение соответствует введенному')

    @allure.description('Проверка поля is_archived - Поле отсутствует')
    def test_02(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox_without_is_archhived(
            moneybox_id, to_date, goal, name, currency_id, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

    @allure.description('Проверка поля is_archived - Перенос копилки в архив с положительным amount') #Есть вероятность что нельзя удалить копилку с положительным amount
    def test_03(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        create_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, '100', access_token)
        moneybox_id = MoneyboxMethods.get_moneybox_id(create_result)

        """Patch_moneybox запрос"""
        with allure.step('Перенос копилки в архив'):
            result_patch = MoneyboxMethods.change_moneybox(
                moneybox_id, to_date, goal, name, currency_id, True, access_token
            )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 400)

    @allure.description('Проверка поля is_archived - Возврат копилки из архива')
    def test_04(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        with allure.step('Перенос копилки в архив'):
            result_patch = MoneyboxMethods.change_moneybox(
                moneybox_id, to_date, goal, name, currency_id, True, access_token
            )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Patch_moneybox запрос"""
        with allure.step('Возврат копилки из архива'):
            result_patch = MoneyboxMethods.change_moneybox(
                moneybox_id, to_date, goal, name, currency_id, False, access_token
            )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 400)

    @allure.description('Проверка поля is_archived - Неверный тип данных (string: "строка")')
    def test_05(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, name, currency_id, 'string', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Проверка поля is_archived - Неверный тип данных (integer: 12345)')
    def test_06(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, name, currency_id, 12345, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Проверка поля is_archived - Пустое поле')
    def test_07(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, name, currency_id, '', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Проверка поля is_archived - Null')
    def test_07(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, name, currency_id, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)
