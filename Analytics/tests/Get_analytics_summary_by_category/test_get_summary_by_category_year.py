import allure

from common_methods.checking import Checking
from Analytics.methods.analytics_methods import AnalyticsMethods
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods


@allure.epic('GET/api/v1/analytics/summary_by_category - Запрос суммированных доходов/расходов по категориям за месяц')
class TestSummaryByCategoryYear:
    @allure.description('Проверка поля year - Значение = 2020')
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
            'Income', '&month=2&year=2020', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result', result_get.text)

        """Проверка типа транзакции"""
        data = Checking.get_data(result_get)
        assert data['meta']['transaction_type'] == 'Income'

    @allure.description('Проверка поля year - Значение = 2100')
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
        result_get = AnalyticsMethods.get_summary_by_category_with_params(
            'Income', '&month=2&year=2100', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result', result_get.text)

        """Проверка типа транзакции"""
        data = Checking.get_data(result_get)
        assert data['meta']['transaction_type'] == 'Income'

    @allure.description('Проверка поля year - Поле отсутствует')
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
            'Income', '&month=2', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print('Result', result_get.text)

        """Проверка типа транзакции"""
        data = Checking.get_data(result_get)
        assert data['meta']['transaction_type'] == 'Income'

    @allure.description('Проверка поля year - Значение - 2019')
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
            'Income', '&month=2&year=2019', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля year - Значение - 2101')
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
            'Income', '&month=2&year=2101', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля year - Поле в формате гг')
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
            'Income', '&month=2&year=25', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля year - Пустое поле')
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
            'Income', '&month=2&year=""', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля year - Null')
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
            'Income', '&month=2&year=null', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля year - Отрицательный год (-2040)')
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
            'Income', '&month=2&year=-2025', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля year - Недопустимые символы')
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
            'Income', '&month=2&year=@#', access_token
        )

        """проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

