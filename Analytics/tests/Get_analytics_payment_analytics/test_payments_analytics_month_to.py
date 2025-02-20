import allure

from Analytics.methods.analytics_methods import AnalyticsMethods
from common_methods.checking import Checking


@allure.epic('Get/api/v1/analytics/payments_analytics - аналитика исполненных и пропущенных регулярных платежей - '
             'проверка поля month_to')
class TestGetPaymentAnalyticsMonthTo:

    @allure.description('Проверка поля month_to - month_to  = 1')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?month_to=1', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля month_to - month_to = в формате 01')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?month_to=01', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля month_to - month_to  = 12')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?month_to=12', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля month_to - Поле отсутствует')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?year_from=2026', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля month_to - вещественное число')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?month_to=5.0', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля month_to - month_to  = 0')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?month_to=0', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля month_to - month_to  = 13')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?month_to=13', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля month_to - month_to = Отрицательное значение')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?month_to=-5', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля month_to - month_to = Пустое поле')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?month_to=""', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
        print('Result_analytics', result_get.text)

    @allure.description('Проверка поля month_to - month_to = Null')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_with_params(
            '?month_to=null', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
        print('Result_analytics', result_get.text)





