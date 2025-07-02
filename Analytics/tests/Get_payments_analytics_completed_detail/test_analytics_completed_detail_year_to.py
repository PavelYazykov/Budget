import allure
import pytest

from common_methods.checking import Checking
from Analytics.methods.analytics_methods import AnalyticsMethods
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from Subcategory.methods.subcategory_methods import SubcategoryMethods
from Analytics.methods.payloads import Payloads


@pytest.mark.Analytics
@allure.epic('Get/api/v1/analytics/payments_analytics/{category_id}/completed_detail - '
             'Запрос аналитики по исполненным регулярным платежам для заданой категории - проверка поля year to')
class TestAnalyticsCompletedDetailYearTo:

    @allure.description('проверка поля year to - Значение  = 2020')
    def test_01(self, create_moneybox_and_delete_for_analytics):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_payments_analytics_completed_detail_with_params(
            20,
            '?month_from=1&year_from=2020&month_to=12&year_to=2020&regular_payment=true&onetime_payment=true',
            access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

        """Проверка наличия обязательных полей"""
        Payloads.check_data_mete(result_get)

    @allure.description('проверка поля year from - Значение  = 2100')
    def test_02(self, create_moneybox_and_delete_for_analytics):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        regular_outcome_id = None
        subcategory_id = None

        """Создание подкатегории"""
        try:
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

            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_completed_detail_with_params(
                20,
                '?month_from=1&year_from=2020&month_to=1&year_to=2100&regular_payment=true&onetime_payment=true',
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
            if regular_outcome_id is not None:
                result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
                Checking.check_statuscode(result_delete, 204)
            if subcategory_id is not None:
                delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
                Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('проверка поля year from - Поле отсутствует')
    def test_03(self, create_moneybox_and_delete_for_analytics):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        regular_outcome_id = None
        subcategory_id = None

        """Создание подкатегории"""
        try:
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

            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_completed_detail_with_params(
                20,
                '?month_from=1&year_from=2020&regular_payment=true&onetime_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка наличие полей data meta"""
            Payloads.check_data_mete(result_get)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            if regular_outcome_id is not None:
                result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
                Checking.check_statuscode(result_delete, 204)
            if subcategory_id is not None:
                delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
                Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('проверка поля year from - year from > year to')
    def test_04(self, create_moneybox_and_delete_for_analytics):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        regular_outcome_id = None
        subcategory_id = None

        """Создание подкатегории"""
        try:
            create_subcategory = SubcategoryMethods.create_subcategory(
                20, "Pavel_subcategory", access_token
            )
            Checking.check_statuscode(create_subcategory, 201)
            data = Checking.get_data(create_subcategory)
            subcategory_id = data['data']['id']

            """Запрос на создание regular_outcome"""
            result = RegularOutcomeMethods.create_regular_outcome(
                'Pavel', 20, subcategory_id, 'month', 100, False,
                '2029-01-30', access_token,
            )
            Checking.check_statuscode(result, 201)
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']

            """Оплата регулярного платежа"""
            result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
            Checking.check_statuscode(result_pay, 200)
            print('RESULT PAY: ', result_pay.text)

            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_completed_detail_with_params(
                20,
                '?month_from=1&year_from=2031&month_to=11&year_to=2030&regular_payment=true&onetime_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            data_2 = Checking.get_data(result_get)

            """Проверка наличия полей data meta"""
            Payloads.check_data_mete(result_get)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            if regular_outcome_id is not None:
                result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
                Checking.check_statuscode(result_delete, 204)
            if subcategory_id is not None:
                delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
                Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('проверка поля year from - Значение = 2019')
    def test_05(self, create_moneybox_and_delete_for_analytics):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        regular_outcome_id = None
        subcategory_id = None

        """Создание подкатегории"""
        try:
            create_subcategory = SubcategoryMethods.create_subcategory(
                20, "Pavel_subcategory", access_token
            )
            Checking.check_statuscode(create_subcategory, 201)
            data = Checking.get_data(create_subcategory)
            subcategory_id = data['data']['id']

            """Запрос на создание regular_outcome"""
            result = RegularOutcomeMethods.create_regular_outcome(
                'Pavel', 20, subcategory_id, 'month', 100, False,
                '2030-01-30', access_token,
            )
            Checking.check_statuscode(result, 201)
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']

            """Оплата регулярного платежа"""
            result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
            Checking.check_statuscode(result_pay, 200)
            print('RESULT PAY: ', result_pay.text)

            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_completed_detail_with_params(
                20,
                '?month_from=1&year_from=2030&month_to=12&year_to=2019&regular_payment=true&onetime_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            if regular_outcome_id is not None:
                result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
                Checking.check_statuscode(result_delete, 204)
            if subcategory_id is not None:
                delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
                Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('проверка поля year from - Значение = 2101')
    def test_06(self, create_moneybox_and_delete_for_analytics):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        regular_outcome_id = None
        subcategory_id = None

        """Создание подкатегории"""
        try:
            create_subcategory = SubcategoryMethods.create_subcategory(
                20, "Pavel_subcategory", access_token
            )
            Checking.check_statuscode(create_subcategory, 201)
            data = Checking.get_data(create_subcategory)
            subcategory_id = data['data']['id']

            """Запрос на создание regular_outcome"""
            result = RegularOutcomeMethods.create_regular_outcome(
                'Pavel', 20, subcategory_id, 'month', 100, False,
                '2030-01-30', access_token,
            )
            Checking.check_statuscode(result, 201)
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']

            """Оплата регулярного платежа"""
            result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
            Checking.check_statuscode(result_pay, 200)
            print('RESULT PAY: ', result_pay.text)

            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_completed_detail_with_params(
                20,
                '?month_from=1&year_from=2030&month_to=12&year_to=2101&regular_payment=true&onetime_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            if regular_outcome_id is not None:
                result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
                Checking.check_statuscode(result_delete, 204)
            if subcategory_id is not None:
                delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
                Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('проверка поля year from - отрицательное значение')
    def test_07(self, create_moneybox_and_delete_for_analytics):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        regular_outcome_id = None
        subcategory_id = None

        """Создание подкатегории"""
        try:
            create_subcategory = SubcategoryMethods.create_subcategory(
                20, "Pavel_subcategory", access_token
            )
            Checking.check_statuscode(create_subcategory, 201)
            data = Checking.get_data(create_subcategory)
            subcategory_id = data['data']['id']

            """Запрос на создание regular_outcome"""
            result = RegularOutcomeMethods.create_regular_outcome(
                'Pavel', 20, subcategory_id, 'month', 100, False,
                '2030-01-30', access_token,
            )
            Checking.check_statuscode(result, 201)
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']

            """Оплата регулярного платежа"""
            result_pay = RegularOutcomeMethods.pay_regular_outcome(regular_outcome_id, wallet_id, access_token)
            Checking.check_statuscode(result_pay, 200)
            print('RESULT PAY: ', result_pay.text)

            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_payments_analytics_completed_detail_with_params(
                20,
                '?month_from=1&year_from=2030&month_to=12&year_to=2019&regular_payment=true&onetime_payment=true',
                access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            if regular_outcome_id is not None:
                result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
                Checking.check_statuscode(result_delete, 204)
            if subcategory_id is not None:
                delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
                Checking.check_statuscode(delete_subcategory, 204)

