import allure
import pytest

from Analytics.methods.analytics_methods import AnalyticsMethods
from Payment_info.methods.payment_info_methods import PaymentInfoMethods
from Subcategory.methods.subcategory_methods import SubcategoryMethods
from common_methods.checking import Checking
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from Analytics.methods.payloads import Payloads


@pytest.mark.Analytics
@allure.epic('Get/api/v1/analytics/payments_analytics - аналитика исполненных и пропущенных регулярных платежей - '
             'общие проверки')
class TestGetPaymentAnalyticsCommon:

    @allure.description(
        'Общие проверки - Запросить аналитику по всем платежам без параметров авторизованный пользователь'
    )
    def test_01(self, create_moneybox_and_delete_for_analytics):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        regular_outcome_id = None

        """Запрос на создание regular_outcome"""
        try:
            result = RegularOutcomeMethods.create_regular_outcome(
                'Pavel_title', 20, None, 'month', 100, False,
                '2030-02-17', access_token,
            )
            Checking.check_statuscode(result, 201)
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            print(regular_outcome_id)

            """Оплата регулярного платежа"""
            result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
            Checking.check_statuscode(result_pay, 200)
            print('RESULT PAY: ', result_pay.text)

            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics(access_token)

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка наличия обязательных полей"""
            Payloads.check_get_payments_analytics(result_get, Payloads.get_payments_analytics)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e

        finally:
            if regular_outcome_id is not None:
                result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
                Checking.check_statuscode(result_delete, 204)

    @allure.description(
        'Общие проверки - Запросить аналитику по регулярным платежам без параметров авторизованный пользователь'
    )
    def test_02(self, create_moneybox_and_delete_for_analytics):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        regular_outcome_id = None

        """Запрос на создание regular_outcome"""
        try:
            result = RegularOutcomeMethods.create_regular_outcome(
                'Pavel_title', 20, None, 'month', 100, False,
                '2030-02-17', access_token,
            )
            Checking.check_statuscode(result, 201)
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            print(regular_outcome_id)

            """Оплата регулярного платежа"""
            result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
            Checking.check_statuscode(result_pay, 200)
            print('RESULT PAY: ', result_pay.text)

            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_with_params(
                '?regular_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка наличия обязательных полей"""
            Payloads.check_get_payments_analytics(result_get, Payloads.get_payments_analytics)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e

        finally:
            if regular_outcome_id is not None:
                result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
                Checking.check_statuscode(result_delete, 204)

    @allure.description(
        'Общие проверки - Запросить аналитику по регулярным платежам с параметрами авторизованный пользователь'
    )
    def test_03(self, create_moneybox_and_delete_for_analytics):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        regular_outcome_id = None

        """Запрос на создание regular_outcome"""
        try:
            result = RegularOutcomeMethods.create_regular_outcome(
                'Pavel_title', 20, None, 'month', 100, False,
                '2030-02-17', access_token,
            )
            Checking.check_statuscode(result, 201)
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            print(regular_outcome_id)

            """Оплата регулярного платежа"""
            result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
            Checking.check_statuscode(result_pay, 200)
            print('RESULT PAY: ', result_pay.text)

            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_with_params(
                '?month_from=02&year_from=2025&month_to=12&year_to=2030&regular_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('Result_analytics', result_get.text)

            """Проверка наличия обязательных полей"""
            Payloads.check_get_payments_analytics(result_get, Payloads.get_payments_analytics)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e

        finally:
            if regular_outcome_id is not None:
                result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
                Checking.check_statuscode(result_delete, 204)

    @allure.description(
        'Общие проверки - Запросить аналитику по единоразовым платежам без параметров авторизованный пользователь'
    )
    def test_04(self, create_moneybox_and_delete_for_analytics):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        regular_outcome_id = None

        """Запрос на создание regular_outcome"""
        try:
            result = RegularOutcomeMethods.create_regular_outcome(
                'Pavel_title', 20, None, 'onetime', 100, False,
                '2030-02-17', access_token,
            )
            Checking.check_statuscode(result, 201)
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            print(regular_outcome_id)

            """Оплата регулярного платежа"""
            result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
            Checking.check_statuscode(result_pay, 200)
            print('RESULT PAY: ', result_pay.text)

            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_with_params(
                '?onetime_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('Result_analytics', result_get.text)

            """Проверка наличия обязательных полей"""
            Payloads.check_get_payments_analytics(result_get, Payloads.get_payments_analytics)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e

        finally:
            if regular_outcome_id is not None:
                result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
                Checking.check_statuscode(result_delete, 204)

    @allure.description(
        'Общие проверки - Запросить аналитику по единоразовым платежам с  параметрами авторизованный пользователь'
    )
    def test_05(self, create_moneybox_and_delete_for_analytics):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        regular_outcome_id = None

        """Запрос на создание regular_outcome"""
        try:
            result = RegularOutcomeMethods.create_regular_outcome(
                'Pavel_title', 20, None, 'day', 100, False,
                '2030-02-17', access_token,
            )
            Checking.check_statuscode(result, 201)
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            print(regular_outcome_id)

            """Оплата регулярного платежа"""
            result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
            Checking.check_statuscode(result_pay, 200)
            print('RESULT PAY: ', result_pay.text)

            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_with_params(
                '?month_from=02&year_from=2025&month_to=12&year_to=2030&onetime_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('Result_analytics', result_get.text)

            """Проверка наличия обязательных полей"""
            Payloads.check_get_payments_analytics(result_get, Payloads.get_payments_analytics)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e

        finally:
            if regular_outcome_id is not None:
                result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
                Checking.check_statuscode(result_delete, 204)

    @allure.description(
        'Общие проверки - Запросить аналитику одновременно указав и регулярные и единоразовые платежи'
    )
    def test_06(self, create_moneybox_and_delete_for_analytics):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        regular_outcome_id = None

        """Запрос на создание regular_outcome"""
        try:
            result = RegularOutcomeMethods.create_regular_outcome(
                'Pavel_title', 20, None, 'month', 100, False,
                '2030-02-17', access_token,
            )
            Checking.check_statuscode(result, 201)
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            print(regular_outcome_id)

            """Оплата регулярного платежа"""
            result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
            Checking.check_statuscode(result_pay, 200)
            print('RESULT PAY: ', result_pay.text)

            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_with_params(
                '?month_from=02&year_from=2025&month_to=12&year_to=2030&regular_payment=true&onetime_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('Result_analytics', result_get.text)

            """Проверка наличия обязательных полей"""
            Payloads.check_get_payments_analytics(result_get, Payloads.get_payments_analytics)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e

        finally:
            if regular_outcome_id is not None:
                result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
                Checking.check_statuscode(result_delete, 204)

    @allure.description(
        'Общие проверки - Запросить аналитику одновременно указав значение False регулярным и единоразовым платежам'
    )
    def test_07(self, create_moneybox_and_delete_for_analytics):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        regular_outcome_id = None

        """Запрос на создание regular_outcome"""
        try:
            result = RegularOutcomeMethods.create_regular_outcome(
                'Pavel_title', 20, None, 'month', 100, False,
                '2030-02-17', access_token,
            )
            Checking.check_statuscode(result, 201)
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            print(regular_outcome_id)

            """Оплата регулярного платежа"""
            result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
            Checking.check_statuscode(result_pay, 200)
            print('RESULT PAY: ', result_pay.text)

            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_with_params(
                '?month_from=02&year_from=2025&month_to=12&year_to=2030&regular_payment=false&onetime_payment=false',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 400)
            print('Result_analytics', result_get.text)
        finally:
            if regular_outcome_id is not None:
                result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
                Checking.check_statuscode(result_delete, 204)

    @allure.description('Общие проверки - Запрос аналитики неавторизованный пользователь')  # Дата текущий месяц
    def test_08(self):

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_without_auth()

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 401)

    @allure.description('Запросить аналитику по просроченным платежам')
    def test_09(self, create_moneybox_and_delete_for_analytics):  # Дата текущий месяц
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        subcategory_id = None
        regular_outcome_id = None

        """Создание подкатегории"""
        try:
            create_subcategory = SubcategoryMethods.create_subcategory(
                20, "Pavel_subcategory", access_token
            )
            Checking.check_statuscode(create_subcategory, 201)
            data = Checking.get_data(create_subcategory)
            subcategory_id = data['data']['id']

            """Создание regular_outcome"""
            create_regular_outcome = RegularOutcomeMethods.create_regular_outcome(
                'Pavel', 20, subcategory_id, 'month', 10, False,
                '2030-04-12', access_token
            )
            Checking.check_statuscode(create_regular_outcome, 201)
            data = Checking.get_data(create_regular_outcome)
            regular_outcome_id = data['data']['id']

            PaymentInfoMethods.create_regular_outcome('2025-06-03', regular_outcome_id)  # Дата текущий месяц

            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-06-03', None, False, 111
            )  # Дата текущий месяц

            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics(access_token)

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('R', result_get.text)

            """Проверка отображения просроченного платежа"""
            data = Checking.get_data(result_get)
            assert data['data']['missed'][0]['category'] == 20

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            if regular_outcome_id is not None:
                delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
                Checking.check_statuscode(delete_regular_outcome, 204)
            if subcategory_id is not None:
                delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
                Checking.check_statuscode(delete_subcategory, 204)

    # @allure.description('Общие проверки -  month_from > month_to')
    # def test_10(self, auth_fixture):
    #     """Авторизация"""
    #     access_token = auth_fixture
    #
    #     """Запрос аналитики"""
    #     result_get = AnalyticsMethods.get_payments_analytics_with_params(
    #         '?month_from=12&month_to=02', access_token
    #     )
    #
    #     """проверка статус кода"""
    #     Checking.check_statuscode(result_get, 422)
    #     print('Result_analytics', result_get.text)
    #
    # @allure.description('Общие проверки -  year_from > year_to')
    # def test_11(self, auth_fixture):
    #     """Авторизация"""
    #     access_token = auth_fixture
    #
    #     """Запрос аналитики"""
    #     result_get = AnalyticsMethods.get_payments_analytics_with_params(
    #         '?year_from=2030&year_to=2025', access_token
    #     )
    #
    #     """проверка статус кода"""
    #     Checking.check_statuscode(result_get, 422)
    #     print('Result_analytics', result_get.text)
    #
    # @allure.description('Общие проверки -  year_from > year_to')
    # def test_12(self, auth_fixture):
    #     """Авторизация"""
    #     access_token = auth_fixture
    #
    #     """Запрос аналитики"""
    #     result_get = AnalyticsMethods.get_payments_analytics_with_params(
    #         '?month_from=12&year_from=2030&month_to=01&year_to=2025', access_token
    #     )
    #
    #     """проверка статус кода"""
    #     Checking.check_statuscode(result_get, 422)
    #     print('Result_analytics', result_get.text)

