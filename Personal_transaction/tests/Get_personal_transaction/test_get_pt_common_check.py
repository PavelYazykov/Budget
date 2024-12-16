import allure
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
from common_methods.variables import PersonalTransactionVariables
from common_methods.checking import Checking
amount = PersonalTransactionVariables.amount
description = PersonalTransactionVariables.description
transaction_type_income = PersonalTransactionVariables.transaction_type_income
transaction_type_consume = PersonalTransactionVariables.transaction_type_consume
transaction_date = PersonalTransactionVariables.transaction_date
category_id_income = PersonalTransactionVariables.category_id_income
category_id_consume = PersonalTransactionVariables.category_id_consume
transaction_type_tbw = PersonalTransactionVariables.transaction_type_tbw


@allure.epic('GET/api/v1/personal_budget/ Получение списка всех транзакций - общие проверки')
class TestGetAllPTCommon:

    @allure.description('Получение списка всех транзакций  (авторизованный пользователь)')
    def test_01(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Получние списка транзакций"""
        result_get = PersonalTransactionMethods.get_personal_transaction('Income', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

    @allure.description('Получение списка всех транзакций  (неавторизованный пользователь)')
    def test_02(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Получние списка транзакций"""
        result_get = PersonalTransactionMethods.get_personal_transaction_without_auth('Income')

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 401)
