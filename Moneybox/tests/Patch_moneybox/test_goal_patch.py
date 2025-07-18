import json

import pytest

from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
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
amount = MoneyboxVariables.amount


@pytest.mark.patch_moneybox
@pytest.mark.Moneybox
@allure.epic('Patch_moneybox /api/v1/moneybox/{moneybox_id}/ Проверка поля goal')
class TestPatchMoneyboxGoal:

    @allure.description('Проверка поля goal - Значение вещественное число = "400.5"')
    def test_01(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

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

    @allure.description('Проверка поля goal - Увеличение цели')
    def test_02(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

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

    @allure.description('Проверка поля goal - Уменьшение цели')
    def test_03(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

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

    @allure.description('Проверка поля goal - Поле отсутствует')
    def test_04(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox_without_goal(
            moneybox_id, to_date, name, currency_id, is_archived, access_token
        )

        """Проверкра статус кода"""
        Checking.check_statuscode(result_patch, 200)

    @allure.description('Проверка поля goal - Уменьшение цели ниже текущего баланса копилки')
    def test_05(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_create = MoneyboxMethods.create_moneybox(
            '2030-12-30', 500, 'desc', 2, 100, access_token
        )
        Checking.check_statuscode(result_create, 201)
        moneybox_id = MoneyboxMethods.get_moneybox_id(result_create)
        wallet_id = MoneyboxMethods.get_wallet_id(result_create)
        try:
            """Patch_moneybox запрос"""
            result_patch = MoneyboxMethods.change_moneybox_only_goal(
                moneybox_id, 50, access_token
            )

            """Проверкра статус кода"""
            Checking.check_statuscode(result_patch, 400)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Обнуление баланса копилки"""
            result_consumption = PersonalTransactionMethods.create_personal_transaction(
                100, 'name', 'Consumption', '2024-10-10',
                None, wallet_id, 20, None, access_token
            )
            Checking.check_statuscode(result_consumption, 201)

            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля goal - Значение = 0')
    def test_06(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, 0, name, currency_id, is_archived, access_token
        )

        """Проверкра статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Проверка поля goal - Null')
    def test_07(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, None, name, currency_id, is_archived, access_token
        )

        """Проверкра статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Проверка поля goal - Отрицательное значение')
    def test_08(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, -1, name, currency_id, is_archived, access_token
        )

        """Проверкра статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Проверка поля goal - Неверный тип данных (string: "цель")')
    def test_09(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, 'string', name, currency_id, is_archived, access_token
        )

        """Проверкра статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Проверка поля goal - Уменьшить цель до текущего баланса копилки')
    def test_10(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_create = MoneyboxMethods.create_moneybox(
            '2030-12-30', 1000, 'desc', 2, 100, access_token
        )
        moneybox_id = MoneyboxMethods.get_moneybox_id(result_create)
        wallet_id = MoneyboxMethods.get_wallet_id(result_create)
        try:
            """Patch_moneybox запрос"""
            result_patch = MoneyboxMethods.change_moneybox_only_goal(
                moneybox_id, 100, access_token
            )

            """Проверкра статус кода"""
            Checking.check_statuscode(result_patch, 400)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id, wallet_id)


