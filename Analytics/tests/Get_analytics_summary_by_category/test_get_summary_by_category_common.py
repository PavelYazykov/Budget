import time

import allure
import pytest

from common_methods.checking import Checking
from Analytics.methods.analytics_methods import AnalyticsMethods
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
from Settings.methods.settings_methods import SettingsMethods


@pytest.mark.Analytics
@allure.epic('GET/api/v1/analytics/summary_by_category - Запрос суммированных доходов/расходов по категориям за месяц')
class TestSummaryByCategoryCommon:

    @allure.description('Запрос аналитики авторизованный пользователь')
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

    @allure.description('Запрос аналитики при значении false в settings')
    def test_02(self, create_moneybox_and_delete_for_personal_transaction):
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Отправка запроса на изменение поля Аналитика на False"""
        result_settings = SettingsMethods.patch_settings(
            True, False, False, True, True,
            True, True, 2, None, access_token
        )

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

        """Отправка запроса на изменение поля Аналитика на True"""
        result_settings = SettingsMethods.patch_settings(
            True, False, True, True, True,
            True, True, 2, None, access_token
        )

    @allure.description('Запрос аналитики неавторизованный пользователь')
    def test_03(self):

        """Запрос аналитики"""
        result_get = AnalyticsMethods.get_summary_by_category_without_access_token('Income')

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 401)








