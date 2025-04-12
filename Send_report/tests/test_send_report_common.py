import allure

from Send_report.methods.send_reports_methods import SendReportsMethods
from common_methods.checking import Checking
from Personal_budget.methods.personal_budget_methods import PersonalBudgetMethods
from Send_report.methods.payloads import Variables


@allure.epic('Get/api/v1/send_report/ - Отправка отчёта персонального бюджета пользователя на почту - общие проверки')
class TestSendReportCommon:

    @allure.description('общие проверки - Отправка отчета без параметров (текущая дата)')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_personal_budget = PersonalBudgetMethods.create_personal_budget_without_regular_outcome(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, access_token
        )
        Checking.check_statuscode(result_personal_budget, 201)
        data = Checking.get_data(result_personal_budget)
        personal_budget_id = data['data']['id']
        try:
            """Запрос отчета"""
            result_get = SendReportsMethods.get_send_report_with_params(
                '?month_from=01&year_from=2026&month_to=12&year_to=2026&type_report=csv', access_token
            )
            Checking.check_statuscode(result_get, 200)
            data = Checking.get_data(result_get)
            assert (data['message']) == 'Request sent successfully'
        finally:
            if personal_budget_id is not None:
                delete_personal_budget = PersonalBudgetMethods.delete_personal_budget(
                    personal_budget_id, access_token
                )
                Checking.check_statuscode(delete_personal_budget, 204)

