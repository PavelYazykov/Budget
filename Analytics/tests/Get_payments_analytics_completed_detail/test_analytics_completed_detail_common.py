import allure
import pytest

from common_methods.checking import Checking
from Analytics.methods.analytics_methods import AnalyticsMethods
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from Subcategory.methods.subcategory_methods import SubcategoryMethods
from Analytics.methods.payloads import Payloads


@pytest.mark.Analytics
@allure.epic('Get/api/v1/analytics/payments_analytics/{category_id}/completed_detail - '
             'Запрос аналитики по исполненным регулярным платежам для заданой категории - Общие проверки')
class TestAnalyticsCompletedDetailCommon:

    @allure.description('Общие проверки - Запросить аналитику по регулярным платежам без параметров '
                        'авторизованный пользователь')
    def test_01(self, create_moneybox_and_delete_for_analytics):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        """Создание подкатегории"""
        create_subcategory = SubcategoryMethods.create_subcategory(
            20, "Pavel_subcategory", access_token
        )
        Checking.check_statuscode(create_subcategory, 201)
        data = Checking.get_data(create_subcategory)
        subcategory_id = data['data']['id']

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, subcategory_id, 'month', 100, False,
            '2025-06-05', access_token,
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
            data_2 = Checking.get_data(result_get)

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('Result_analytics', result_get.text)

            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields(result_get, Payloads.get_completed_detail)

            """Проверка суммы расходов"""
            assert data_2['data'][0]['amount'] == '100.00'

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
            delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('Общие проверки - Запросить аналитику по регулярным платежам с  '
                        'параметрами авторизованный пользователь')
    def test_02(self, create_moneybox_and_delete_for_analytics):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        """Создание подкатегории"""
        create_subcategory = SubcategoryMethods.create_subcategory(
            20, "Pavel_subcategory", access_token
        )
        Checking.check_statuscode(create_subcategory, 201)
        data = Checking.get_data(create_subcategory)
        subcategory_id = data['data']['id']

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, subcategory_id, 'month', 100, False,
            '2030-05-30', access_token,
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
            result_get = AnalyticsMethods.get_payments_analytics_completed_detail_with_params(
                20,
                '?month_from=1&year_from=2025&month_to=12&year_to=2030&regular_payment=true&onetime_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            data_2 = Checking.get_data(result_get)

            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields(result_get, Payloads.get_completed_detail)

            """Проверка суммы расходов"""
            assert data_2['data'][0]['amount'] == '100.00'
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
            delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('Общие проверки - Запросить аналитику по единоразовым платежам без параметров '
                        'авторизованный пользователь')
    def test_03(self, create_moneybox_and_delete_for_analytics):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        """Создание подкатегории"""
        create_subcategory = SubcategoryMethods.create_subcategory(
            20, "Pavel_subcategory", access_token
        )
        Checking.check_statuscode(create_subcategory, 201)
        data = Checking.get_data(create_subcategory)
        subcategory_id = data['data']['id']

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, subcategory_id, 'onetime', 100, False,
            '2025-06-05', access_token,
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
            data_2 = Checking.get_data(result_get)

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('Result_analytics', result_get.text)

            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields(result_get, Payloads.get_completed_detail)

            """Проверка суммы расходов"""
            assert data_2['data'][0]['amount'] == '100.00'
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
            delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('Запросить аналитику по единоразовым платежам с '
                        'параметрами авторизованный пользователь')
    def test_04(self, create_moneybox_and_delete_for_analytics):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        """Создание подкатегории"""
        create_subcategory = SubcategoryMethods.create_subcategory(
            20, "Pavel_subcategory", access_token
        )
        Checking.check_statuscode(create_subcategory, 201)
        data = Checking.get_data(create_subcategory)
        subcategory_id = data['data']['id']

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, subcategory_id, 'onetime', 100, False,
            '2030-06-30', access_token,
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
            result_get = AnalyticsMethods.get_payments_analytics_completed_detail_with_params(
                20,
                '?month_from=1&year_from=2025&month_to=12&year_to=2030&regular_payment=true&onetime_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            data_2 = Checking.get_data(result_get)

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('Result_analytics', result_get.text)

            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields(result_get, Payloads.get_completed_detail)

            """Проверка суммы расходов"""
            assert data_2['data'][0]['amount'] == '100.00'
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
            delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('Общие проверки - Запросить аналитику одновременно указав и '
                        'регулярные и единоразовые платежи')
    def test_05(self, create_moneybox_and_delete_for_analytics):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        """Создание подкатегории"""
        create_subcategory = SubcategoryMethods.create_subcategory(
            20, "Pavel_subcategory", access_token
        )
        Checking.check_statuscode(create_subcategory, 201)
        data = Checking.get_data(create_subcategory)
        subcategory_id = data['data']['id']

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, subcategory_id, 'month', 100, False,
            '2030-06-30', access_token,
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
            result_get = AnalyticsMethods.get_payments_analytics_completed_detail_with_params(
                20,
                '?month_from=1&year_from=2025&month_to=12&year_to=2030&regular_payment=true&onetime_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            data_2 = Checking.get_data(result_get)

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('Result_analytics', result_get.text)

            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields(result_get, Payloads.get_completed_detail)

            """Проверка суммы расходов"""
            assert data_2['data'][0]['amount'] == '100.00'
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
            delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('Общие проверки - Запросить аналитику одновременно указав значение False '
                        'регулярным и единоразовым платежам')
    def test_06(self, create_moneybox_and_delete_for_analytics):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        """Создание подкатегории"""
        create_subcategory = SubcategoryMethods.create_subcategory(
            20, "Pavel_subcategory", access_token
        )
        Checking.check_statuscode(create_subcategory, 201)
        data = Checking.get_data(create_subcategory)
        subcategory_id = data['data']['id']

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, subcategory_id, 'month', 100, False,
            '2030-05-30', access_token,
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
            result_get = AnalyticsMethods.get_payments_analytics_completed_detail_with_params(
                20,
                '?month_from=1&year_from=2025&month_to=12&year_to=2030&regular_payment=false&onetime_payment=false',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 400)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
            delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('Общие проверки - запрос аналитики - неавторизованный пользователь')
    def test_07(self):
        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_completed_detail_without_auth(20)
        Checking.check_statuscode(result_get, 401)


