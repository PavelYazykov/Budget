import allure
import pytest

from Analytics.methods.analytics_methods import AnalyticsMethods
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking


@pytest.mark.Analytics
@allure.epic('Get/api/v1/analytics/payments_analytics - аналитика исполненных и пропущенных регулярных платежей - '
             'проверка поля regular_payment')
class TestGetPaymentAnalyticsRegularPayment:

    @allure.description('Проверка поля regular_payment - True')
    def test_01(self, create_moneybox_and_delete_for_analytics):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        """Запрос на создание регулярного regular_outcome """
        result = RegularOutcomeMethods.create_regular_outcome(
            'Pavel_regular', 20, None, 'month', 50, False,
            '2030-02-17', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        """Запрос на создание единоразового regular_outcome """
        result_2 = RegularOutcomeMethods.create_regular_outcome(
            'Pavel_onetime', 20, None, 'onetime', 50, False,
            '2030-02-18', access_token,
        )
        Checking.check_statuscode(result_2, 201)
        data_2 = Checking.get_data(result_2)
        regular_outcome_id_2 = data_2['data']['id']

        """Оплата регулярного платежа"""
        result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
        Checking.check_statuscode(result_pay, 200)

        """Оплата единоразового платежа"""
        result_pay_2 = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id_2, wallet_id, access_token)
        Checking.check_statuscode(result_pay_2, 200)

        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_with_params(
                '?month_from=02&year_from=2025&month_to=12&year_to=2031&regular_payment=true&onetime_payment=false',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка отображения платежей"""
            data_get = Checking.get_data(result_get)
            assert data_get['meta']['completed'] == 1

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

            result_delete_2 = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id_2, access_token)
            Checking.check_statuscode(result_delete_2, 204)

    @allure.description('Проверка поля regular_payment - False')
    def test_02(self, create_moneybox_and_delete_for_analytics):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        """Запрос на создание регулярного regular_outcome """
        result = RegularOutcomeMethods.create_regular_outcome(
            'Pavel_regular', 20, None, 'month', 50, False,
            '2030-02-17', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        """Запрос на создание единоразового regular_outcome """
        result_2 = RegularOutcomeMethods.create_regular_outcome(
            'Pavel_onetime', 20, None, 'onetime', 50, False,
            '2030-02-18', access_token,
        )
        Checking.check_statuscode(result_2, 201)
        data_2 = Checking.get_data(result_2)
        regular_outcome_id_2 = data_2['data']['id']

        """Оплата регулярного платежа"""
        result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
        Checking.check_statuscode(result_pay, 200)

        """Оплата единоразового платежа"""
        result_pay_2 = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id_2, wallet_id, access_token)
        Checking.check_statuscode(result_pay_2, 200)

        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_with_params(
                '?month_from=02&year_from=2025&month_to=12&year_to=2031&regular_payment=false&onetime_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка отображения платежей"""
            data_get = Checking.get_data(result_get)
            assert data_get['meta']['completed'] == 1

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

            result_delete_2 = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id_2, access_token)
            Checking.check_statuscode(result_delete_2, 204)

    @allure.description('Проверка поля regular_payment - Поле отсутствует')
    def test_03(self, create_moneybox_and_delete_for_analytics):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        """Запрос на создание регулярного regular_outcome """
        result = RegularOutcomeMethods.create_regular_outcome(
            'Pavel_regular', 20, None, 'month', 50, False,
            '2030-02-17', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        """Запрос на создание единоразового regular_outcome """
        result_2 = RegularOutcomeMethods.create_regular_outcome(
            'Pavel_onetime', 20, None, 'onetime', 50, False,
            '2030-02-18', access_token,
        )
        Checking.check_statuscode(result_2, 201)
        data_2 = Checking.get_data(result_2)
        regular_outcome_id_2 = data_2['data']['id']

        """Оплата регулярного платежа"""
        result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
        Checking.check_statuscode(result_pay, 200)

        """Оплата единоразового платежа"""
        result_pay_2 = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id_2, wallet_id, access_token)
        Checking.check_statuscode(result_pay_2, 200)

        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_with_params(
                '?month_from=02&year_from=2025&month_to=12&year_to=2031&onetime_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка отображения платежей"""
            data_get = Checking.get_data(result_get)
            assert data_get['meta']['completed'] == 2

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

            result_delete_2 = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id_2, access_token)
            Checking.check_statuscode(result_delete_2, 204)

    @allure.description('Проверка поля regular_payment - Null')
    def test_04(self, create_moneybox_and_delete_for_analytics):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        """Запрос на создание регулярного regular_outcome """
        result = RegularOutcomeMethods.create_regular_outcome(
            'Pavel_regular', 20, None, 'month', 50, False,
            '2030-02-17', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        """Запрос на создание единоразового regular_outcome """
        result_2 = RegularOutcomeMethods.create_regular_outcome(
            'Pavel_onetime', 20, None, 'onetime', 50, False,
            '2030-02-18', access_token,
        )
        Checking.check_statuscode(result_2, 201)
        data_2 = Checking.get_data(result_2)
        regular_outcome_id_2 = data_2['data']['id']

        """Оплата регулярного платежа"""
        result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
        Checking.check_statuscode(result_pay, 200)

        """Оплата единоразового платежа"""
        result_pay_2 = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id_2, wallet_id, access_token)
        Checking.check_statuscode(result_pay_2, 200)

        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_with_params(
                '?month_from=02&year_from=2025&month_to=12&year_to=2031&regular_payment=null&onetime_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

            result_delete_2 = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id_2, access_token)
            Checking.check_statuscode(result_delete_2, 204)

    @allure.description('Проверка поля regular_payment - Пустое поле')
    def test_05(self, create_moneybox_and_delete_for_analytics):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        """Запрос на создание регулярного regular_outcome """
        result = RegularOutcomeMethods.create_regular_outcome(
            'Pavel_regular', 20, None, 'month', 50, False,
            '2030-02-17', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        """Запрос на создание единоразового regular_outcome """
        result_2 = RegularOutcomeMethods.create_regular_outcome(
            'Pavel_onetime', 20, None, 'onetime', 50, False,
            '2030-02-18', access_token,
        )
        Checking.check_statuscode(result_2, 201)
        data_2 = Checking.get_data(result_2)
        regular_outcome_id_2 = data_2['data']['id']

        """Оплата регулярного платежа"""
        result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
        Checking.check_statuscode(result_pay, 200)

        """Оплата единоразового платежа"""
        result_pay_2 = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id_2, wallet_id, access_token)
        Checking.check_statuscode(result_pay_2, 200)

        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_with_params(
                '?month_from=02&year_from=2025&month_to=12&year_to=2031&regular_payment=""&onetime_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

            result_delete_2 = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id_2, access_token)
            Checking.check_statuscode(result_delete_2, 204)

    @allure.description('Проверка поля regular_payment - Несуществующее значение')
    def test_06(self, create_moneybox_and_delete_for_analytics):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        """Запрос на создание регулярного regular_outcome """
        result = RegularOutcomeMethods.create_regular_outcome(
            'Pavel_regular', 20, None, 'month', 50, False,
            '2030-02-17', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        """Запрос на создание единоразового regular_outcome """
        result_2 = RegularOutcomeMethods.create_regular_outcome(
            'Pavel_onetime', 20, None, 'onetime', 50, False,
            '2030-02-18', access_token,
        )
        Checking.check_statuscode(result_2, 201)
        data_2 = Checking.get_data(result_2)
        regular_outcome_id_2 = data_2['data']['id']

        """Оплата регулярного платежа"""
        result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
        Checking.check_statuscode(result_pay, 200)

        """Оплата единоразового платежа"""
        result_pay_2 = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id_2, wallet_id, access_token)
        Checking.check_statuscode(result_pay_2, 200)

        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_with_params(
                '?month_from=02&year_from=2025&month_to=12&year_to=2031&regular_payment=string&onetime_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

            result_delete_2 = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id_2, access_token)
            Checking.check_statuscode(result_delete_2, 204)
