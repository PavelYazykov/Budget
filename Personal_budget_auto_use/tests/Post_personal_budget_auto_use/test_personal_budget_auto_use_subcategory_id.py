import allure
import pytest

from common_methods.checking import Checking
from Personal_budget_auto_use.methods.personal_budget_auto_use_methods import PersonalBudgetAutoUseMethods
from Personal_budget_auto_use.methods.payloads_variables import Variables
from Subcategory.methods.subcategory_methods import SubcategoryMethods


@pytest.mark.personal_budget_auto_use
@allure.epic('Post/api/v1/personal_budget_auto_use/ - Создание ежемесячного объекта бюджета - '
             'проверка поля subcategory_id')
class TestPostAutoUseSubcategoryId:

    @allure.description('subcategory_id - Существующий id')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_subcategory = SubcategoryMethods.create_subcategory(Variables.category_id, 'Pavel', access_token)
        Checking.check_statuscode(result_subcategory, 201)
        data = Checking.get_data(result_subcategory)
        subcategory_id = data['data']['id']

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_auto_use_id = data['data']['id']

        try:
            """Проверка поля subcategory_id"""
            data = Checking.get_data(result_create)
            assert data['data']['subcategory_id'] == subcategory_id
        finally:
            if personal_budget_auto_use_id is not None:
                delete_result = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
                    personal_budget_auto_use_id, access_token
                )
                Checking.check_statuscode(delete_result, 204)
            if subcategory_id is not None:
                result_delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
                Checking.check_statuscode(result_delete_subcategory, 204)

    @allure.description('subcategory_id - Null')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_auto_use_id = data['data']['id']

        try:
            """Проверка поля subcategory_id"""
            data = Checking.get_data(result_create)
            assert data['data']['subcategory_id'] is None
        finally:
            if personal_budget_auto_use_id is not None:
                delete_result = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
                    personal_budget_auto_use_id, access_token
                )
                Checking.check_statuscode(delete_result, 204)

    @allure.description('subcategory_id - Поле отсутствует')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use_without_subcategory_id(
            Variables.transaction_type, Variables.category_id, Variables.amount,
            Variables.date_reminder, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_auto_use_id = data['data']['id']

        try:
            """Проверка поля subcategory_id"""
            data = Checking.get_data(result_create)
            assert data['data']['subcategory_id'] is None
        finally:
            if personal_budget_auto_use_id is not None:
                delete_result = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
                    personal_budget_auto_use_id, access_token
                )
                Checking.check_statuscode(delete_result, 204)

    @allure.description('subcategory_id - Несуществующий id')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, 12345, Variables.amount,
            Variables.date_reminder, access_token
        )

        """Проеверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 404)

    @allure.description('subcategory_id - Значение id = 0')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, 0, Variables.amount,
            Variables.date_reminder, access_token
        )

        """Проеверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('subcategory_id - Отрицательное значение')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, -5, Variables.amount,
            Variables.date_reminder, access_token
        )

        """Проеверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('subcategory_id - Отрицательное значение')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, -5, Variables.amount,
            Variables.date_reminder, access_token
        )

        """Проеверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('subcategory_id - Пустое поле')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, "", Variables.amount,
            Variables.date_reminder, access_token
        )

        """Проеверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('subcategory_id - Неверный тип данных string')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, "string", Variables.amount,
            Variables.date_reminder, access_token
        )

        """Проеверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('subcategory_id - Вещественное число')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, 1.1, Variables.amount,
            Variables.date_reminder, access_token
        )

        """Проеверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)


