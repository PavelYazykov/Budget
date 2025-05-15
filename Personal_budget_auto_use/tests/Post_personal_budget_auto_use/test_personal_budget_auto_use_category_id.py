import allure
import pytest

from common_methods.checking import Checking
from Personal_budget_auto_use.methods.personal_budget_auto_use_methods import PersonalBudgetAutoUseMethods
from Personal_budget_auto_use.methods.payloads_variables import Variables


@pytest.mark.Personal_budget_auto_use
@allure.epic('Post/api/v1/personal_budget_auto_use/ - Создание ежемесячного объекта бюджета - '
             'проверка поля category_id')
class TestPostAutoUseCategotyId:

    @allure.description('category_id - Существующий id')
    def test_01(self, auth_fixture):
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
            """Проверка поля category_id"""
            data = Checking.get_data(result_create)
            category_id = data['data']['category_id']
            assert category_id == 30
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

    @allure.description('category_id - Null')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, None, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('category_id - Поле отсутствует')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use_without_category_id(
            Variables.transaction_type, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('category_id - Несуществующий id')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, 123456, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 404)

    @allure.description('category_id - Значение id = 0')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, 0, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('category_id - Отрицательное значение')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, -5, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('category_id - Пустое поле')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, "", Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('category_id - Неверный тип данных string')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, "string", Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('category_id - Вещественное число')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, 1.1, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)
