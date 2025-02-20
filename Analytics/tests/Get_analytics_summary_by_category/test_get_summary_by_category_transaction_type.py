import time

import allure

from common_methods.checking import Checking
from Analytics.methods.analytics_methods import AnalyticsMethods
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods


@allure.epic('GET/api/v1/analytics/summary_by_category - Запрос суммированных доходов/расходов по категориям за месяц')
class TestSummaryByCategoryTransactionType:
    @allure.description('Проверка поля transaction_type - Значение  - Income')
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
        result_get = AnalyticsMethods.get_summary_by_category('Income', access_token)

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result', result_get.text)
        time.sleep(2)

        """Проверка типа транзакции"""
        data = Checking.get_data(result_get)
        assert data['meta']['transaction_type'] == 'Income'

    @allure.description('Проверка поля transaction_type - Значение  - Consumption')
    def test_02(self, create_moneybox_and_delete_for_personal_transaction):
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
        result_get = AnalyticsMethods.get_summary_by_category('Consumption', access_token)

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result', result_get.text)
        time.sleep(2)

        """Проверка типа транзакции"""
        data = Checking.get_data(result_get)
        assert data['meta']['transaction_type'] == 'Consumption'

    @allure.description('Проверка поля transaction_type - Значение  - Transfer between wallets')
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
        result_get = AnalyticsMethods.get_summary_by_category('Transfer between wallets', access_token)

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result', result_get.text)
        time.sleep(2)

        """Проверка типа транзакции"""
        data = Checking.get_data(result_get)
        assert data['meta']['transaction_type'] == 'Transfer between wallets'

    @allure.description('Проверка поля transaction_type - Несуществующее значение')
    def test_04(self, auth_fixture):
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_category('Transfer', access_token)

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля transaction_type - Неверный тип данных integer')
    def test_05(self, auth_fixture):
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_category(12345, access_token)

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля transaction_type - Поле отсутствует')
    def test_06(self, auth_fixture):
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_category_without_transaction_type(
            '&month=2&year=2025', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 404)

    @allure.description('Проверка поля transaction_type - Пустое поле')
    def test_07(self, auth_fixture):
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_category('', access_token)

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля transaction_type - Null')
    def test_08(self, auth_fixture):
        access_token = auth_fixture

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_category(None, access_token)

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
