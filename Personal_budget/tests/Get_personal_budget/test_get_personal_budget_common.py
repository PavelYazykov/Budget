import allure
from common_methods.checking import Checking
from Personal_budget.methods.personal_budget_methods import PersonalBudgetMethods
from Personal_budget.methods.payloads import Variables, Payloads


@allure.epic('Get/api/v1/personal_budget/ - Запрос всех объектов бюджета - Общие проверки')
class TestGetPersonalBudgetCommon:

    @allure.description('Общие проверки - Получене списка с валидными данными')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, Variables.have_to_remind,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_id = data['data']['id']

        try:
            """Запрос на отображение персональных бюджетов"""
            result_get = PersonalBudgetMethods.get_personal_budget_with_params(
                '?month_from=01&year_from=2026&month_to=12&year_to=2026', access_token
            )
            Checking.check_statuscode(result_get, 200)

            """Проверка наличия транзакции"""
            data = Checking.get_data(result_get)
            assert data['data'][0]['transaction_type'] == 'Income'

            assert data['data'][0]['year'] == 2026

            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields_get(result_get, Payloads.get_payloads)

        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

