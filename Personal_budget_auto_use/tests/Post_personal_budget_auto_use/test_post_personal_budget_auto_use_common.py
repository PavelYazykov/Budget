import allure

from common_methods.checking import Checking
from Personal_budget_auto_use.methods.personal_budget_auto_use_methods import PersonalBudgetAutoUseMethods
from Personal_budget_auto_use.methods.payloads_variables import Variables, Payloads


@allure.epic('Post/api/v1/personal_budget_auto_use/ - Создание ежемесячного объекта бюджета - общие проверки')
class TestPostAutoUseCommon:

    @allure.description('общие проверки - Создание бюджета с валидными данными (авторизованный пользователь)')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            '2025-03-27', access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_auto_use_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            Payloads.check_req_fields_post(result_create, Payloads.post_payloads)
        finally:
            if personal_budget_auto_use_id is not None:
                delete_result = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
                    personal_budget_auto_use_id, access_token
                )
                Checking.check_statuscode(delete_result, 204)

    @allure.description('общие проверки - Без body')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use_without_body(access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('общие проверки - Для Income указать категорию соответствующую Consume')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, 20, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 400)

    @allure.description('общие проверки - Для Consumption указать категорию соответствующую Income')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            'Consumption', 30, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 400)

    @allure.description('общие проверки - Создание двух одинаковых регулярных бюджетов в один месяц')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        personal_budget_auto_use_id_2 = None

        """Создание ежемесячного объекта бюджета_1"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_auto_use_id = data['data']['id']
        try:
            """Создание ежемесячного объекта бюджета_2"""
            result_create_2 = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
                Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
                Variables.date_reminder, access_token
            )
            Checking.check_statuscode(result_create_2, 201)
            data_2 = Checking.get_data(result_create_2)
            personal_budget_auto_use_id_2 = data_2['data']['id']
        finally:
            if personal_budget_auto_use_id:
                delete_result = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
                    personal_budget_auto_use_id, access_token
                )
                Checking.check_statuscode(delete_result, 204)
            if personal_budget_auto_use_id_2:
                delete_result_2 = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
                    personal_budget_auto_use_id_2, access_token
                )
                Checking.check_statuscode(delete_result_2, 204)

