import allure

from Analytics.methods.analytics_methods import AnalyticsMethods
from common_methods.checking import Checking
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from datetime import date
date = date.today()
date_str = str(date)
month = date_str.split('-')[1]
year = date_str.split('-')[0]


@allure.epic(
    'Get/api/v1/analytics/summary_by_outcomes - суммированные по категориям расходы по платежам за заданный период'
)
class TestSummaryByOutcomesCommon:

    @allure.description(
        'Запрос суммированных по категориям расходов по платежам без параметров (автризованный пользователь)'
    )
    def test_01(self, create_moneybox_and_delete_for_analytics):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, None, 'month', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        """Оплата регулярного платежа"""
        result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
        Checking.check_statuscode(result_pay, 200)
        print('RESULT PAY: ', result_pay.text)

        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes('all', access_token)

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('Result_analytics', result_get.text)

            """Проверка типа транзакции"""
            data = Checking.get_data(result_get)
            assert data['meta']['outcome_type'] == 'all'

            """Проверка суммы расходов"""
            assert data['data'][0]['amount'] == '100.00'

        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Указать месяц, год и период дат одновременно')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'month', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', '&month=01&year=2025&first_day=2030-12-12&last_day=2030-12-30', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Запрос суммированных по категориям расходов по платежам (неавтризованный пользователь)')
    def test_03(self):

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_outcomes_with_params_without_auth(
            'all', '&month=01&year=2030'
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 401)

    @allure.description(
        'Запрос суммированных по категориям расходов по платежам с указанием month'
    )
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'month', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', '&month=01', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('Result', result_get.text)

            """Проверка типа транзакции"""
            data = Checking.get_data(result_get)
            assert data['meta']['outcome_type'] == 'all'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description(
        'Запрос суммированных по категориям расходов по платежам с указанием year'
    )
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'month', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', '&year=2030', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('Result', result_get.text)

            """Проверка типа транзакции"""
            data = Checking.get_data(result_get)
            assert data['meta']['outcome_type'] == 'all'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description(
        'Запрос суммированных по категориям расходов по платежам с указанием month и year'
    )
    def test_06(self, create_moneybox_and_delete_for_analytics):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'month', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        """Оплата регулярного платежа"""
        result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
        Checking.check_statuscode(result_pay, 200)
        print('RESULT PAY: ', result_pay.text)

        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', f'&month={month}&year={year}', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('Result', result_get.text)

            """Проверка типа транзакции"""
            data = Checking.get_data(result_get)
            assert data['meta']['outcome_type'] == 'all'

            """Проверка суммы расходов"""
            assert data['data'][0]['amount'] == '100.00'

        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description(
        'Запрос суммированных по категориям расходов по платежам с указанием first_day и last day'
    )
    def test_07(self, create_moneybox_and_delete_for_analytics):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'month', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        """Оплата регулярного платежа"""
        result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
        Checking.check_statuscode(result_pay, 200)
        print('RESULT PAY: ', result_pay.text)

        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', f'&first_day={date_str}&last_day=2030-12-12', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('Result', result_get.text)

            """Проверка типа транзакции"""
            data = Checking.get_data(result_get)
            assert data['meta']['outcome_type'] == 'all'

            """Проверка суммы расходов"""
            assert data['data'][0]['amount'] == '100.00'

        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description(
        'Запрос суммированных по категориям расходов по платежам с указанием first_day'
    )
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'month', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', '&first_day=2025-12-12', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description(
        'Запрос суммированных по категориям расходов по платежам с указанием last_day'
    )
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'month', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', '&last_day=2025-12-12', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

