import allure
import pytest

from common_methods.checking import Checking
from Analytics.methods.analytics_methods import AnalyticsMethods
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from Subcategory.methods.subcategory_methods import SubcategoryMethods
from Analytics.methods.payloads import Payloads
from Payment_info.methods.payment_info_methods import PaymentInfoMethods


@pytest.mark.Analytics
@allure.epic('Get/api/v1/analytics/payments_analytics/{category_id}/missed_detail - Запрос аналитики по пропущенным'
             'регулярным платежам для заданной категории - проверка поля month_from')
class TestAnalyticsMissedDetailMonthFrom:

    @allure.description('проверка поля month_from - month_from  = 1')
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

        """Создание regular_outcome"""
        create_regular_outcome = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, subcategory_id, 'month', 10, False,
            '2030-04-12', access_token
        )
        Checking.check_statuscode(create_regular_outcome, 201)
        data = Checking.get_data(create_regular_outcome)
        regular_outcome_id = data['data']['id']

        PaymentInfoMethods.create_regular_outcome('2025-05-05', regular_outcome_id)

        try:
            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-05-05', None, False, 111
            )

            """Запрос аналитики"""
            get_analytics = AnalyticsMethods.get_payment_analytics_missed_detail_with_params(
                20,
                '?month_from=1&year_from=2025&month_to=12&year_to=2031&regular_payment=true&onetime_payment=true',
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(get_analytics, 200)

            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields(get_analytics, Payloads.get_missed_detail)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

            delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('проверка поля month_from - month_from  = 12')
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

        """Создание regular_outcome"""
        create_regular_outcome = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, subcategory_id, 'month', 10, False,
            '2030-04-12', access_token
        )
        Checking.check_statuscode(create_regular_outcome, 201)
        data = Checking.get_data(create_regular_outcome)
        regular_outcome_id = data['data']['id']

        PaymentInfoMethods.create_regular_outcome('2025-05-05', regular_outcome_id)

        try:
            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-05-05', None, False, 111
            )

            """Запрос аналитики"""
            get_analytics = AnalyticsMethods.get_payment_analytics_missed_detail_with_params(
                20,
                '?month_from=12&year_from=2024&month_to=12&year_to=2031&regular_payment=true&onetime_payment=true',
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(get_analytics, 200)

            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields(get_analytics, Payloads.get_missed_detail)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

            delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('проверка поля month_from - Поле отсутствует')
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

        """Создание regular_outcome"""
        create_regular_outcome = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, subcategory_id, 'month', 10, False,
            '2030-04-12', access_token
        )
        Checking.check_statuscode(create_regular_outcome, 201)
        data = Checking.get_data(create_regular_outcome)
        regular_outcome_id = data['data']['id']

        PaymentInfoMethods.create_regular_outcome('2025-05-05', regular_outcome_id)

        try:
            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-05-05', None, False, 111
            )

            """Запрос аналитики"""
            get_analytics = AnalyticsMethods.get_payment_analytics_missed_detail_with_params(
                20,
                '?year_from=2025&month_to=12&year_to=2031&regular_payment=true&onetime_payment=true',
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(get_analytics, 200)

            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields(get_analytics, Payloads.get_missed_detail)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

            delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('проверка поля month_from - month_from  = 0')
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

        """Создание regular_outcome"""
        create_regular_outcome = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, subcategory_id, 'month', 10, False,
            '2030-04-12', access_token
        )
        Checking.check_statuscode(create_regular_outcome, 201)
        data = Checking.get_data(create_regular_outcome)
        regular_outcome_id = data['data']['id']

        PaymentInfoMethods.create_regular_outcome('2025-05-05', regular_outcome_id)

        try:
            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-05-05', None, False, 111
            )

            """Запрос аналитики"""
            get_analytics = AnalyticsMethods.get_payment_analytics_missed_detail_with_params(
                20,
                '?month_from=0&year_from=2025&month_to=12&year_to=2031&regular_payment=true&onetime_payment=true',
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(get_analytics, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

            delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('проверка поля month_from - month_from  = 13')
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

        """Создание regular_outcome"""
        create_regular_outcome = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, subcategory_id, 'month', 10, False,
            '2030-04-12', access_token
        )
        Checking.check_statuscode(create_regular_outcome, 201)
        data = Checking.get_data(create_regular_outcome)
        regular_outcome_id = data['data']['id']

        PaymentInfoMethods.create_regular_outcome('2025-05-05', regular_outcome_id)

        try:
            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-05-05', None, False, 111
            )

            """Запрос аналитики"""
            get_analytics = AnalyticsMethods.get_payment_analytics_missed_detail_with_params(
                20,
                '?month_from=13&year_from=2025&month_to=12&year_to=2031&regular_payment=true&onetime_payment=true',
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(get_analytics, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

            delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('проверка поля month_from - Пустое поле')
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

        """Создание regular_outcome"""
        create_regular_outcome = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, subcategory_id, 'month', 10, False,
            '2030-04-12', access_token
        )
        Checking.check_statuscode(create_regular_outcome, 201)
        data = Checking.get_data(create_regular_outcome)
        regular_outcome_id = data['data']['id']

        PaymentInfoMethods.create_regular_outcome('2025-05-05', regular_outcome_id)

        try:
            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-05-05', None, False, 111
            )

            """Запрос аналитики"""
            get_analytics = AnalyticsMethods.get_payment_analytics_missed_detail_with_params(
                20,
                '?month_from=""&year_from=2025&month_to=12&year_to=2031&regular_payment=true&onetime_payment=true',
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(get_analytics, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

            delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(delete_subcategory, 204)