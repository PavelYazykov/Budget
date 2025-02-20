import allure

from common_methods.checking import Checking
from Analytics.methods.analytics_methods import AnalyticsMethods
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods


@allure.epic('Get/api/v1/analytics/payments_analytics/{category_id}/completed_detail - '
             'Запрос аналитики по исполненным регулярным платежам для заданой категории - Общие проверки')
class TestAnalyticsCompletedDetailCommon:

    @allure.description('Общие проверки - Запросить аналитику по регулярным платежам без параметров '
                        'авторизованный пользователь')
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
            result_get = AnalyticsMethods.get_payments_analytics_completed_detail(20, access_token)

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