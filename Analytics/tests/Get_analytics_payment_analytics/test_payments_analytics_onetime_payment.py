import allure

from Analytics.methods.analytics_methods import AnalyticsMethods
from common_methods.checking import Checking


@allure.epic('Get/api/v1/analytics/payments_analytics - аналитика исполненных и пропущенных регулярных платежей - '
             'проверка поля onetime_payment')
class TestGetPaymentAnalyticsOnetimePayment:

    @allure.description('Проверка поля onetime_payment - True')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?onetime_payment=true', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля onetime_payment - False')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?onetime_payment=false', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля onetime_payment - Поле отсутствует')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?regular_payment=true', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля onetime_payment - Null')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?onetime_payment=null', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля onetime_payment - Пустое поле')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?onetime_payment=""', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля onetime_payment - Несуществующее значение')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?onetime_payment="№;%', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
        print('Result_analytics', result_get.text)

