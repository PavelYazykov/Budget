import allure
import pytest

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


@pytest.mark.Personal_transaction
@pytest.mark.get_Personal_transaction
@allure.epic('GET/api/v1/personal_budget/ Получение списка всех транзакций - проверка поля linked_regular_outcome')
class TestGetAllPTlinkedRegularOutcome:

    @allure.description('Проверка параметра linked_regular_outcome - Значение true')
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
        result_get = PersonalTransactionMethods.get_personal_transaction_with_linked_regular_outcome(
            'Income', 1, 1, 2024, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

    @allure.description('Проверка параметра linked_regular_outcome - Значение False')
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
        result_get = PersonalTransactionMethods.get_personal_transaction_with_linked_regular_outcome(
            'Income', 1, 1, 2024, False, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

    @allure.description('Проверка параметра linked_regular_outcome - Значение Null')
    def test_03(self, create_moneybox_and_delete_for_personal_transaction):
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
        result_get = PersonalTransactionMethods.get_personal_transaction_with_linked_regular_outcome(
            'Income', 1, 1, 2024, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка параметра linked_regular_outcome - Поле отсутствует')
    def test_04(self, create_moneybox_and_delete_for_personal_transaction):
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
        result_get = PersonalTransactionMethods.get_personal_transaction_with_params(
            'Income', 1, 1, 2025, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

    @allure.description('Проверка параметра linked_regular_outcome - неверный тип данных string')
    def test_05(self, create_moneybox_and_delete_for_personal_transaction):
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
        result_get = PersonalTransactionMethods.get_personal_transaction_with_linked_regular_outcome(
            'Income', 1, 1, 2024, 'string', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка параметра linked_regular_outcome - неверный тип данных integer')
    def test_06(self, create_moneybox_and_delete_for_personal_transaction):
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
        result_get = PersonalTransactionMethods.get_personal_transaction_with_linked_regular_outcome(
            'Income', 1, 1, 2024, 12345, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка параметра linked_regular_outcome - Пустое поле')
    def test_07(self, create_moneybox_and_delete_for_personal_transaction):
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
        result_get = PersonalTransactionMethods.get_personal_transaction_with_linked_regular_outcome(
            'Income', 1, 1, 2024, '', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
