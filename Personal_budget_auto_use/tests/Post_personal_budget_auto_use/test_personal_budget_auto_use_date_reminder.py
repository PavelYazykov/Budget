import allure
import pytest

from common_methods.checking import Checking
from Personal_budget_auto_use.methods.personal_budget_auto_use_methods import PersonalBudgetAutoUseMethods
from Personal_budget_auto_use.methods.payloads_variables import Variables
from datetime import date
current_date = str(date.today())


@pytest.mark.Personal_budget_auto_use
@allure.epic('Post/api/v1/personal_budget_auto_use/ - Создание ежемесячного объекта бюджета - '
             'проверка поля date_reminder')
class TestPostAutoUsDateReminder:

    @allure.description('date_reminder - Текущая дата')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, 10,
            current_date, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_auto_use_id = data['data']['id']
        try:
            """Проверка поля date_reminder"""
            data = Checking.get_data(result_create)
            assert data['data']['date_reminder'] == current_date
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            if personal_budget_auto_use_id is not None:
                delete_result = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
                    personal_budget_auto_use_id, access_token
                )
                Checking.check_statuscode(delete_result, 204)

    @allure.description('date_reminder - Дата в будущем')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            '2030-12-12', access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_auto_use_id = data['data']['id']
        try:
            """Проверка поля date_reminder"""
            data = Checking.get_data(result_create)
            assert data['data']['date_reminder'] == '2030-12-12'
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            if personal_budget_auto_use_id is not None:
                delete_result = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
                    personal_budget_auto_use_id, access_token
                )
                Checking.check_statuscode(delete_result, 204)

    @allure.description('date_reminder - Дата в прошлом')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            '2023-12-12', access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('date_reminder - Значение месяца = 0')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            '2023-0-12', access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('date_reminder - Значение месяца = 13')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            '2023-13-12', access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('date_reminder - Значение дня = 0')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            '2023-12-0', access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('date_reminder - Значение дня = 32')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            '2023-12-32', access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('date_reminder - Нелопустимые символы')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            '2023-fg-32', access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('date_reminder - Неерный тип данных')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            2030-12-12, access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('date_reminder - Пустое поле')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            "", access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('date_reminder - Поле отсутствует')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use_without_date_reminder(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('date_reminder - Null')
    def test_12(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            None, access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)
