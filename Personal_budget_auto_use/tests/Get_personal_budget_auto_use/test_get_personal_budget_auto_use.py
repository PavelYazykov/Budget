import allure
import pytest

from common_methods.checking import Checking
from Personal_budget_auto_use.methods.personal_budget_auto_use_methods import PersonalBudgetAutoUseMethods
from Personal_budget_auto_use.methods.payloads_variables import Variables, Payloads


@pytest.mark.personal_budget_auto_use
@allure.epic('Get/api/v1/personal_budget_auto_use/ - Запрос списка ежемесячных объектов бюджета')
class TestGetAutoUse:

    @allure.description('Запрос информации о регулярном бюджете авторизованный пользователь')
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
            """Запрос списка ежемесячных объектов бюджета"""
            result_get = PersonalBudgetAutoUseMethods.get_personal_budget_auto_use(access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка наличия обязательных полей"""
            Payloads.check_req_fields(result_get, Payloads.get_payloads)
        finally:
            if personal_budget_auto_use_id:
                delete_result = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
                    personal_budget_auto_use_id, access_token
                )
                Checking.check_statuscode(delete_result, 204)

    @allure.description('Запрос информации о регулярном бюджете неавторизованный пользователь')
    def test_02(self):

        """Запрос списка ежемесячных объектов бюджета"""
        result_get = PersonalBudgetAutoUseMethods.get_personal_budget_auto_use_without_auth()

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 401)



