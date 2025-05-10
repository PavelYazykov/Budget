import allure
import pytest

from Send_report.methods.send_reports_methods import SendReportsMethods
from common_methods.checking import Checking
from Personal_budget.methods.personal_budget_methods import PersonalBudgetMethods
from Send_report.methods.payloads import Variables


@pytest.mark.Send_report
@allure.epic('Get/api/v1/send_report/ - Отправка отчёта персонального бюджета пользователя на почту - '
             'проверка поля month_to')
class TestSendReportMonthTo:

    @allure.description('проверка поля month_to - Значение месяца = 1')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_personal_budget = PersonalBudgetMethods.create_personal_budget_without_regular_outcome(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            '01', Variables.year, access_token
        )
        Checking.check_statuscode(result_personal_budget, 201)
        data = Checking.get_data(result_personal_budget)
        personal_budget_id = data['data']['id']
        try:
            """Запрос отчета"""
            result_get = SendReportsMethods.get_send_report_with_params(
                '?month_from=1&year_from=2025&month_to=1&year_to=2027&type_report=csv', access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка отправк отчета"""
            data = Checking.get_data(result_get)
            assert (data['message']) == 'Request sent successfully'
        finally:
            if personal_budget_id is not None:
                delete_personal_budget = PersonalBudgetMethods.delete_personal_budget(
                    personal_budget_id, access_token
                )
                Checking.check_statuscode(delete_personal_budget, 204)

    @allure.description('проверка поля month_to - Значение месяца = 01')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_personal_budget = PersonalBudgetMethods.create_personal_budget_without_regular_outcome(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            '01', Variables.year, access_token
        )
        Checking.check_statuscode(result_personal_budget, 201)
        data = Checking.get_data(result_personal_budget)
        personal_budget_id = data['data']['id']
        try:
            """Запрос отчета"""
            result_get = SendReportsMethods.get_send_report_with_params(
                '?month_from=1&year_from=2025&month_to=01&year_to=2027&type_report=csv', access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка отправк отчета"""
            data = Checking.get_data(result_get)
            assert (data['message']) == 'Request sent successfully'
        finally:
            if personal_budget_id is not None:
                delete_personal_budget = PersonalBudgetMethods.delete_personal_budget(
                    personal_budget_id, access_token
                )
                Checking.check_statuscode(delete_personal_budget, 204)

    @allure.description('проверка поля month_to - Значение месяца = 12')
    def test_03(self, auth_fixture):
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
                '?month_from=1&year_from=2025&month_to=12&year_to=2027&type_report=csv', access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка отправк отчета"""
            data = Checking.get_data(result_get)
            assert (data['message']) == 'Request sent successfully'
        finally:
            if personal_budget_id is not None:
                delete_personal_budget = PersonalBudgetMethods.delete_personal_budget(
                    personal_budget_id, access_token
                )
                Checking.check_statuscode(delete_personal_budget, 204)

    @allure.description('проверка поля month_to - Поле отсутствует')
    def test_04(self, auth_fixture):
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
                '?month_from=1&year_from=2025&year_to=2027&type_report=csv', access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 404)

        finally:
            if personal_budget_id is not None:
                delete_personal_budget = PersonalBudgetMethods.delete_personal_budget(
                    personal_budget_id, access_token
                )
                Checking.check_statuscode(delete_personal_budget, 204)

    @allure.description('проверка поля month_to - Значение месяца = 0')
    def test_05(self, auth_fixture):
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
                '?month_from=1&year_from=2025&month_to=0&year_to=2027&type_report=csv', access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        finally:
            if personal_budget_id is not None:
                delete_personal_budget = PersonalBudgetMethods.delete_personal_budget(
                    personal_budget_id, access_token
                )
                Checking.check_statuscode(delete_personal_budget, 204)

    @allure.description('проверка поля month_to - Значение месяца = 13')
    def test_06(self, auth_fixture):
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
                '?month_from=1&year_from=2025&month_to=13&year_to=2027&type_report=csv', access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        finally:
            if personal_budget_id is not None:
                delete_personal_budget = PersonalBudgetMethods.delete_personal_budget(
                    personal_budget_id, access_token
                )
                Checking.check_statuscode(delete_personal_budget, 204)

    @allure.description('проверка поля month_to - Отрицательное значение')
    def test_07(self, auth_fixture):
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
                '?month_from=1&year_from=2025&month_to=-12&year_to=2027&type_report=csv', access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        finally:
            if personal_budget_id is not None:
                delete_personal_budget = PersonalBudgetMethods.delete_personal_budget(
                    personal_budget_id, access_token
                )
                Checking.check_statuscode(delete_personal_budget, 204)

    @allure.description('проверка поля month_to - Недопустимые символы')
    def test_08(self, auth_fixture):
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
                '?month_from=1&year_from=2025&month_to=fg&year_to=2027&type_report=csv', access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        finally:
            if personal_budget_id is not None:
                delete_personal_budget = PersonalBudgetMethods.delete_personal_budget(
                    personal_budget_id, access_token
                )
                Checking.check_statuscode(delete_personal_budget, 204)