import time

import allure
import pytest

from common_methods.checking import Checking
from Analytics.methods.analytics_methods import AnalyticsMethods
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods


@pytest.mark.Analytics
@allure.epic('GET/api/v1/analytics/summary_by_category - Запрос суммированных доходов/расходов по категориям за месяц')
class TestSummaryByCategoryMonth:
    @allure.description('Проверка поля month - Значение = 1')
    def test_01(self, create_moneybox_and_delete_for_personal_transaction):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции 1"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Income', None,
            wallet_id, 30, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Создание транзакции 2"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Consumption', None,
            wallet_id, 20, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_category_with_params(
            'Income', '&month=2&year=2025', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result', result_get.text)

        """Проверка типа транзакции"""
        data = Checking.get_data(result_get)
        assert data['meta']['transaction_type'] == 'Income'

    @allure.description('Проверка поля month - Значение = 12')
    def test_01(self, create_moneybox_and_delete_for_personal_transaction):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции 1"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Income', None,
            wallet_id, 30, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Создание транзакции 2"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Consumption', None,
            wallet_id, 20, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_category_with_params(
            'Income', '&month=12&year=2025', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result', result_get.text)

        """Проверка типа транзакции"""
        data = Checking.get_data(result_get)
        assert data['meta']['transaction_type'] == 'Income'

    @allure.description('Проверка поля month - Поле отсутствует')
    def test_03(self, create_moneybox_and_delete_for_personal_transaction):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции 1"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Income', None,
            wallet_id, 30, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Создание транзакции 2"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Consumption', None,
            wallet_id, 20, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_category_with_params(
            'Income', '&year=2025', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result', result_get.text)

        """Проверка типа транзакции"""
        data = Checking.get_data(result_get)
        assert data['meta']['transaction_type'] == 'Income'

    @allure.description('Проверка поля month - Ввод месяца в формате (01; 02)')
    def test_04(self, create_moneybox_and_delete_for_personal_transaction):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции 1"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Income', None,
            wallet_id, 30, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Создание транзакции 2"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Consumption', None,
            wallet_id, 20, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_category_with_params(
            'Income', '&month=01&year=2025', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result', result_get.text)

        """Проверка типа транзакции"""
        data = Checking.get_data(result_get)
        assert data['meta']['transaction_type'] == 'Income'

    @allure.description('Проверка поля month - Вещественное число 11.0')
    def test_05(self, create_moneybox_and_delete_for_personal_transaction):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции 1"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Income', None,
            wallet_id, 30, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Создание транзакции 2"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Consumption', None,
            wallet_id, 20, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_category_with_params(
            'Income', '&month=11.0&year=2025', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result', result_get.text)

        """Проверка типа транзакции"""
        data = Checking.get_data(result_get)
        assert data['meta']['transaction_type'] == 'Income'

    @allure.description('Проверка поля month - Месяц - 13')
    def test_06(self, create_moneybox_and_delete_for_personal_transaction):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции 1"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Income', None,
            wallet_id, 30, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Создание транзакции 2"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Consumption', None,
            wallet_id, 20, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_category_with_params(
            'Income', '&month=13&year=2025', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля month - Отрицательный месяц')
    def test_07(self, create_moneybox_and_delete_for_personal_transaction):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции 1"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Income', None,
            wallet_id, 30, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Создание транзакции 2"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Consumption', None,
            wallet_id, 20, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_category_with_params(
            'Income', '&month=-2&year=2025', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля month - Пустое поле')
    def test_08(self, create_moneybox_and_delete_for_personal_transaction):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции 1"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Income', None,
            wallet_id, 30, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Создание транзакции 2"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Consumption', None,
            wallet_id, 20, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_category_with_params(
            'Income', '&month=''&year=2025', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля month - Null')
    def test_09(self, create_moneybox_and_delete_for_personal_transaction):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции 1"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Income', None,
            wallet_id, 30, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Создание транзакции 2"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Consumption', None,
            wallet_id, 20, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_category_with_params(
            'Income', '&month=null&year=2025', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля month - Недопустимые символы')
    def test_10(self, create_moneybox_and_delete_for_personal_transaction):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции 1"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Income', None,
            wallet_id, 30, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Создание транзакции 2"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Consumption', None,
            wallet_id, 20, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_category_with_params(
            'Income', '&month=@#&year=2025', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля month - Месяц - 0')
    def test_10(self, create_moneybox_and_delete_for_personal_transaction):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции 1"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Income', None,
            wallet_id, 30, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Создание транзакции 2"""
        create_pt = PersonalTransactionMethods.create_personal_transaction_without_transaction_date(
            10, 'title', 'Consumption', None,
            wallet_id, 20, None, access_token
        )
        Checking.check_statuscode(create_pt, 201)

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_category_with_params(
            'Income', '&month=0&year=2025', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

