import allure
import pytest

from Personal_transaction.methods.payloads import Payloads
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
@allure.epic('GET/api/v1/personal_budget/ Получение списка всех транзакций - проверка поля day')
class TestGetAllPTDayCheck:

    @allure.description('Проверка параметра day - День = 1')
    def test_01(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, '2025-05-01', None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Получние списка транзакций"""
        result_get = PersonalTransactionMethods.get_personal_transaction_with_params(
            'Income', 1, 5, 2025, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

        """Проверка наличия обязательных полей"""
        Payloads.check_required_fields(result_get, Payloads.get_payloads)

    @allure.description('Проверка параметра day - День = 31')
    def test_02(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, '2025-05-31', None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Получние списка транзакций"""
        result_get = PersonalTransactionMethods.get_personal_transaction_with_params(
            'Income', 31, 5, 2025, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

        """Проверка наличия обязательных полей"""
        Payloads.check_required_fields(result_get, Payloads.get_payloads)

    @allure.description('Проверка параметра day - Поле отсутствует')
    def test_03(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, '2025-05-01', None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Получние списка транзакций"""
        result_get = PersonalTransactionMethods.get_personal_transaction_with_params_wd(
            'Income', 5, 2025, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

        """Проверка наличия обязательных полей"""
        Payloads.check_required_fields(result_get, Payloads.get_payloads)

    @allure.description('Проверка параметра day - Ввод дня в формате (01; 02)')
    def test_04(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, '2025-05-01', None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Получние списка транзакций"""
        result_get = PersonalTransactionMethods.get_personal_transaction_with_params(
            'Income', '01', 5, 2025, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

        """Проверка наличия обязательных полей"""
        Payloads.check_required_fields(result_get, Payloads.get_payloads)

    @allure.description('Проверка параметра day - Вещественное число')
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
            'Income', '1.1', 10, 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка параметра day - День 32')
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
            'Income', '32', 10, 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка параметра day - Отрицательное значение')
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
            'Income', '-1', 10, 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка параметра day - Пустое поле')
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
            'Income', '', 10, 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка параметра day - Null')
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
            'Income', None, 10, 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка параметра day - Недопустимые символы')
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
            'Income', 'None', 10, 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка параметра day - day = 0')
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
            'Income', '0', 10, 2024, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)



