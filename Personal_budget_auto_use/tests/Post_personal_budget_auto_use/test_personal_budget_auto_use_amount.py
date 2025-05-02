import allure

from common_methods.checking import Checking
from Personal_budget_auto_use.methods.personal_budget_auto_use_methods import PersonalBudgetAutoUseMethods
from Personal_budget_auto_use.methods.payloads_variables import Variables


@allure.epic('Post/api/v1/personal_budget_auto_use/ - Создание ежемесячного объекта бюджета - '
             'проверка поля amount')
class TestPostAutoUseAmount:

    @allure.description('amount - Целое число')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, 10,
            Variables.date_reminder, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_auto_use_id = data['data']['id']
        try:
            """Проверка поля amount"""
            data = Checking.get_data(result_create)
            assert data['data']['amount'] == '10.00'
        finally:
            if personal_budget_auto_use_id is not None:
                delete_result = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
                    personal_budget_auto_use_id, access_token
                )
                Checking.check_statuscode(delete_result, 204)

    @allure.description('amount - Вещественное число')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, 10.10,
            Variables.date_reminder, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_auto_use_id = data['data']['id']
        try:
            """Проверка поля amount"""
            data = Checking.get_data(result_create)
            assert data['data']['amount'] == '10.10'
        finally:
            if personal_budget_auto_use_id is not None:
                delete_result = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
                    personal_budget_auto_use_id, access_token
                )
                Checking.check_statuscode(delete_result, 204)

    @allure.description('amount - Значение 9999999999.99')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, 9999999999.99,
            Variables.date_reminder, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_auto_use_id = data['data']['id']
        try:
            """Проверка поля amount"""
            data = Checking.get_data(result_create)
            assert data['data']['amount'] == '9999999999.99'
        finally:
            if personal_budget_auto_use_id is not None:
                delete_result = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
                    personal_budget_auto_use_id, access_token
                )
                Checking.check_statuscode(delete_result, 204)

    @allure.description('amount - Значение 9999999999.101')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, 9999999999.101,
            Variables.date_reminder, access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('amount - Значение 10000000000')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, 10000000000,
            Variables.date_reminder, access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('amount - Значение = 0')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, 0,
            Variables.date_reminder, access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('amount - Отрицательное значение')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, -5,
            Variables.date_reminder, access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('amount - Поле отсутствует')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use_without_amount(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id,
            Variables.date_reminder, access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('amount - Пустое поле')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, "",
            Variables.date_reminder, access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('amount - Null')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, None,
            Variables.date_reminder, access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)

    @allure.description('amount - Недопустимые символы')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, "string",
            Variables.date_reminder, access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, 201)
        Checking.check_statuscode(result_create, 422)
