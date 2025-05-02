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
@allure.epic('Post/api/v1/personal_transaction/ Создание персональной транзакции. Проверка поля wallet_id')
class TestPTPostWalletId:

    @allure.description('Проверка поля wallet_id - Существующий id')
    def test_01(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, transaction_type_income, transaction_date, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка значения поля amount"""
        data = Checking.get_data(result)
        assert data['data']['amount'] == '10.00'

    @allure.description('Проверка поля wallet_id - Несуществующий id')
    def test_02(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, transaction_type_income, transaction_date, 1,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('Проверка поля wallet_id - Значение id = 0')
    def test_03(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, transaction_type_income, transaction_date, 0,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля wallet_id - Отрицательное значение')
    def test_04(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, transaction_type_income, transaction_date, -1,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля wallet_id - Поле отсутствует')
    def test_05(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_wallet_id(
            amount, description, transaction_type_income, transaction_date, None, category_id_income,
            None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля wallet_id - Пустое поле')
    def test_06(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, transaction_type_income, transaction_date, '',
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля wallet_id - Null')
    def test_07(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, transaction_type_income, transaction_date, None,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля wallet_id - Неверный тип данных string')
    def test_08(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, transaction_type_income, transaction_date, 'string',
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля wallet_id - Вещественное число')
    def test_09(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, transaction_type_income, transaction_date, 1.1,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

