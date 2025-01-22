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


@pytest.mark.Personal_transaction
@allure.epic(
    'Post/api/v1/personal_transaction/ Создание персональной транзакции Проверка поля transaction_type'
)
class TestPTTransactionType:

    @allure.description('Проверка поля transaction_type -  Несуществующий тип транзакции')
    def test_01(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, 'transaction_type_income', transaction_date, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля transaction_type - Неверный тип данных integer')
    def test_02(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, 123456, transaction_date, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля transaction_type - Поле отсутствует')
    def test_03(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer_trans_type(
            amount, description, transaction_date, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля transaction_type - Пустое поле')
    def test_04(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, '', transaction_date, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля transaction_type - Null')
    def test_05(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, None, transaction_date, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)
