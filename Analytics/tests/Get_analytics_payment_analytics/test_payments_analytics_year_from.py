import allure

from Analytics.methods.analytics_methods import AnalyticsMethods
from common_methods.checking import Checking


@allure.epic('Get/api/v1/analytics/payments_analytics - аналитика исполненных и пропущенных регулярных платежей - '
             'проверка поля year_from')
class TestGetPaymentAnalyticsYearFrom:

    @allure.description('Проверка поля year_from -  year_from  = 2020')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?year_from=2020', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля year_from -  year_from  = 2100')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?year_from=2100', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля year_from -  Поле отсутствует')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?month_from=12', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля year_from -  year_from  = 2019')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?year_from=2019', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля year_from - year_from  = 2101')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?year_from=2101', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля year_from - Отрицательное значение')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?year_from=-2030', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля year_from - Пустое поле')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?year_from=""', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля year_from - Null')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?year_from=null', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
        print('Result_analytics', result_get.text)