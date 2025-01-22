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
@allure.epic('GET/api/v1/personal_budget/ Получение списка всех транзакций - проверка поля month')
class TestGetAllPTMonthCheck:

    @allure.description('Проверка параметра month - month = 1')
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
        result_get = PersonalTransactionMethods.get_personal_transaction_with_params(
            'Income', 1, 1, 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

    @allure.description('Проверка параметра month - month = 12')
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
        result_get = PersonalTransactionMethods.get_personal_transaction_with_params(
            'Income', 1, 12, 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

    @allure.description('Проверка параметра month - Поле отсутствует')
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
        result_get = PersonalTransactionMethods.get_personal_transaction_with_params_wm(
            'Income', 1, 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

    @allure.description('Проверка параметра month - Ввод месяца в формате (01; 02)')
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
            'Income', 1, '01', 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

    @allure.description('Проверка параметра month - Вещественное число')
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
        result_get = PersonalTransactionMethods.get_personal_transaction_with_params(
            'Income', 1, '1.1', 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка параметра month - Месяц 13')
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
        result_get = PersonalTransactionMethods.get_personal_transaction_with_params(
            'Income', 1, '13', 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка параметра month - Отрицательный месяц (-1)')
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
        result_get = PersonalTransactionMethods.get_personal_transaction_with_params(
            'Income', 1, '-1', 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка параметра month - Пустое поле')
    def test_08(self, create_moneybox_and_delete_for_personal_transaction):
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
            'Income', 1, '', 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка параметра month - Null')
    def test_09(self, create_moneybox_and_delete_for_personal_transaction):
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
            'Income', 1, None, 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка параметра month - Недопустимые символы')
    def test_10(self, create_moneybox_and_delete_for_personal_transaction):
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
            'Income', 1, 'None', 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка параметра month - month = 0')
    def test_11(self, create_moneybox_and_delete_for_personal_transaction):
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
            'Income', 1, '0', 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

