import allure
import pytest

from Analytics.methods.analytics_methods import AnalyticsMethods
from common_methods.checking import Checking
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods


@pytest.mark.Analytics
@allure.epic(
    'Get/api/v1/analytics/summary_by_outcomes - суммированные по категориям расходы по платежам за заданный период - '
    'Провнерка поля Outcome_type'
)
class TestSummaryByOutcomesOutcomeType:

    @allure.description('Проверка поля Outcome_type - Значение all')
    def test_01(self, create_moneybox_and_delete_for_analytics):
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
            result_get = AnalyticsMethods.get_summary_by_outcomes('all', access_token)

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('Result', result_get.text)

            """Проверка типа транзакции"""
            data = Checking.get_data(result_get)
            assert data['meta']['outcome_type'] == 'all'
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля Outcome_type - Значение onetime')
    def test_0(self, create_moneybox_and_delete_for_analytics):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_analytics

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'onetime', 100, False,
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
            result_get = AnalyticsMethods.get_summary_by_outcomes('onetime', access_token)

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('Result', result_get.text)

            """Проверка типа транзакции"""
            data = Checking.get_data(result_get)
            assert data['meta']['outcome_type'] == 'onetime'
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля Outcome_type - Значение regular')
    def test_03(self, create_moneybox_and_delete_for_analytics):
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
            result_get = AnalyticsMethods.get_summary_by_outcomes('regular', access_token)

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('Result', result_get.text)

            """Проверка типа транзакции"""
            data = Checking.get_data(result_get)
            assert data['meta']['outcome_type'] == 'regular'
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Провнерка поля Outcome_type - Несуществующее значение')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes('type', access_token)

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Провнерка поля Outcome_type - Неверный тип данных integer')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes(1234, access_token)

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Провнерка поля Outcome_type - Поле отсутствует')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params_without_outcome_type(
                '?month=01', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Провнерка поля Outcome_type - Пустое поле')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes('', access_token)

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Провнерка поля Outcome_type - Null')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes(None, access_token)

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
