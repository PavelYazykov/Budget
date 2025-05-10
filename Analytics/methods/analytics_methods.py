import allure
from common_methods.variables import CommonVariables
from common_methods.http_methods import HttpMethods


class AnalyticsMethods:

    @staticmethod
    def get_summary_by_category(transaction_type, access_token):
        with allure.step('Запрос суммированных доходов/расходов по категориям за месяц без параметров'):
            endpoint = '/api/v1/analytics/summary_by_category'
            transaction_type = f'?transaction_type={transaction_type}'
            get_url = CommonVariables.base_url + endpoint + transaction_type
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_summary_by_category_without_access_token(transaction_type):
        with allure.step('Запрос суммированных доходов/расходов по категориям за месяц без параметров'):
            endpoint = '/api/v1/analytics/summary_by_category'
            transaction_type = f'?transaction_type={transaction_type}'
            get_url = CommonVariables.base_url + endpoint + transaction_type
            result = HttpMethods.get_without_auth(get_url)
            return result

    @staticmethod
    def get_summary_by_category_with_params(transaction_type, payloads, access_token):
        with allure.step('Запрос суммированных доходов/расходов по категориям за месяц c параметрами'):
            endpoint = '/api/v1/analytics/summary_by_category'
            transaction_type = f'?transaction_type={transaction_type}'
            get_url = CommonVariables.base_url + endpoint + transaction_type + payloads
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_summary_by_category_without_transaction_type(payloads, access_token):
        with allure.step(
                'Запрос суммированных доходов/расходов по категориям за месяц c параметрами without_transaction_type'):
            endpoint = '/api/v1/analytics/summary_by_category'
            get_url = CommonVariables.base_url + endpoint + payloads
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_summary_by_outcomes(outcome_type, access_token):
        with allure.step('Запрос суммированных расходов по категориям за заданный период без параметров'):
            endpoint = '/api/v1/analytics/summary_by_outcomes'
            outcome_type = f'?outcome_type={outcome_type}'
            get_url = CommonVariables.base_url + endpoint + outcome_type
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_summary_by_outcomes_with_params(outcome_type, payloads, access_token):
        with allure.step('Запрос суммированных расходов по категориям за заданный период с параметрами'):
            endpoint = '/api/v1/analytics/summary_by_outcomes'
            outcome_type = f'?outcome_type={outcome_type}'
            get_url = CommonVariables.base_url + endpoint + outcome_type + payloads
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_summary_by_outcomes_with_params_without_auth(outcome_type, payloads):
        with allure.step(
                'Запрос суммированных расходов по категориям за заданный период с параметрами без авторизации'
        ):
            endpoint = '/api/v1/analytics/summary_by_outcomes'
            outcome_type = f'?outcome_type={outcome_type}'
            get_url = CommonVariables.base_url + endpoint + outcome_type + payloads
            result = HttpMethods.get_without_auth(get_url)
            return result

    @staticmethod
    def get_summary_by_outcomes_with_params_without_outcome_type(payloads, access_token):
        with allure.step(
                'Запрос суммированных расходов по категориям за заданный период с параметрами without_outcome_type'
        ):
            endpoint = '/api/v1/analytics/summary_by_outcomes'
            get_url = CommonVariables.base_url + endpoint + payloads
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_payments_analytics(access_token):
        with allure.step('Запрос аналитики по исполненым и пропущенным плвтежам без параметров'):
            endpoint = '/api/v1/analytics/payments_analytics'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_payments_analytics_without_auth():
        with allure.step('Запрос аналитики по исполненым и пропущенным плвтежам без параметров'):
            endpoint = '/api/v1/analytics/payments_analytics'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get_without_auth(get_url)
            return result

    @staticmethod
    def get_payments_analytics_with_params(payloads, access_token):
        with (allure.step('Запрос аналитики по исполненым и пропущенным плaтежам с параметрами')):
            endpoint = '/api/v1/analytics/payments_analytics'
            get_url = CommonVariables.base_url + endpoint + payloads
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_payments_analytics_completed_detail(category_id, access_token):
        with allure.step('Запрос аналитики по исполненным регулярным платежам для заданой категории без параметров'):
            endpoint = f'/api/v1/analytics/payments_analytics/{category_id}/completed_detail'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_payments_analytics_completed_detail_without_auth(category_id):
        with allure.step('Запрос аналитики по исполненным регулярным платежам для заданой '
                         'категории без параметров и авторизации'):
            endpoint = f'/api/v1/analytics/payments_analytics/{category_id}/completed_detail'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get_without_auth(get_url)
            return result

    @staticmethod
    def get_payments_analytics_completed_detail_with_params(category_id, paylodas, access_token):
        with allure.step('Запрос аналитики по исполненным регулярным платежам для заданой категории c параметрами'):
            endpoint = f'/api/v1/analytics/payments_analytics/{category_id}/completed_detail'
            get_url = CommonVariables.base_url + endpoint + paylodas
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_payment_analytics_missed_detail(category_id, access_token):
        with allure.step('Запрос аналитики по пропущенным регулярным платежам для заданой категории'):
            endpoint = f'/api/v1/analytics/payments_analytics/{category_id}/missed_detail'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_payment_analytics_missed_detail_with_params(category_id, payloads, access_token):
        with allure.step('Запрос аналитики по пропущенным регулярным платежам для заданой категории с параметрами'):
            endpoint = f'/api/v1/analytics/payments_analytics/{category_id}/missed_detail'
            get_url = CommonVariables.base_url + endpoint + payloads
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_payment_analytics_missed_detail_with_params_without_auth(category_id, payloads):
        with allure.step('Запрос аналитики по пропущенным регулярным платежам для заданой категории с параметрами'):
            endpoint = f'/api/v1/analytics/payments_analytics/{category_id}/missed_detail'
            get_url = CommonVariables.base_url + endpoint + payloads
            result = HttpMethods.get_without_auth(get_url)
            return result

