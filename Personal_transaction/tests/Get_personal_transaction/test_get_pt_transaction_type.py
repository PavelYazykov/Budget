import allure
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
from common_methods.variables import PersonalTransactionVariables
from common_methods.checking import Checking
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from Personal_transaction.methods.payloads import Payloads
amount = PersonalTransactionVariables.amount
description = PersonalTransactionVariables.description
transaction_type_income = PersonalTransactionVariables.transaction_type_income
transaction_type_consume = PersonalTransactionVariables.transaction_type_consume
transaction_date = PersonalTransactionVariables.transaction_date
category_id_income = PersonalTransactionVariables.category_id_income
category_id_consume = PersonalTransactionVariables.category_id_consume
transaction_type_tbw = PersonalTransactionVariables.transaction_type_tbw


@allure.epic('GET/api/v1/personal_budget/ Получение списка всех транзакций - проверка параметра transaction_type')
class TestGetAllPTTransactionType:

    @allure.description('transaction_type -Income')
    def test_01(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result_income = PersonalTransactionMethods.create_personal_transaction(
            10, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result_income, 201)

        result_consumption = PersonalTransactionMethods.create_personal_transaction(
            10, description, transaction_type_consume, transaction_date, None, wallet_id,
            category_id_consume, None, access_token
        )
        Checking.check_statuscode(result_consumption, 201)

        """Получние списка транзакций"""
        result_get = PersonalTransactionMethods.get_personal_transaction(
            'Income', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

        """Проверка наличия обязательных полей"""
        Payloads.check_required_fields(result_get, Payloads.get_payloads)

        """Проверка значения поля transaction_type"""
        data = Checking.get_data(result_get)
        assert data['data'][0]['transaction_type'] == 'Income'

    @allure.description('transaction_type - Consumption')
    def test_02(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result_income = PersonalTransactionMethods.create_personal_transaction(
            10, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result_income, 201)

        result_consumption = PersonalTransactionMethods.create_personal_transaction(
            10, description, transaction_type_consume, transaction_date, None, wallet_id,
            category_id_consume, None, access_token
        )
        Checking.check_statuscode(result_consumption, 201)

        """Получние списка транзакций"""
        result_get = PersonalTransactionMethods.get_personal_transaction(
            'Consumption', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

        """Проверка наличия обязательных полей"""
        Payloads.check_required_fields(result_get, Payloads.get_payloads)

        """Проверка значения поля transaction_type"""
        data = Checking.get_data(result_get)
        assert data['data'][0]['transaction_type'] == 'Consumption'

    @allure.description('transaction_type - Transfer between wallets')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_moneybox_1 = MoneyboxMethods.create_moneybox(
            '2030-12-31', 1000, 'moneybox', 2, 10, access_token
        )
        Checking.check_statuscode(result_moneybox_1, 201)
        result_moneybox_2 = MoneyboxMethods.create_moneybox(
            '2030-12-31', 1000, 'moneybox_2', 2, 0, access_token
        )
        Checking.check_statuscode(result_moneybox_1, 201)

        """Получение wallet_id и moneybox_id"""
        wallet_id_1 = MoneyboxMethods.get_wallet_id(result_moneybox_1)
        moneybox_id_1 = MoneyboxMethods.get_moneybox_id(result_moneybox_1)

        wallet_id_2 = MoneyboxMethods.get_wallet_id(result_moneybox_2)
        moneybox_id_2 = MoneyboxMethods.get_moneybox_id(result_moneybox_2)
        try:
            """Создание транзакции"""
            result = PersonalTransactionMethods.create_personal_transaction(
                10, description, 'Transfer between wallets', transaction_date, wallet_id_2,
                wallet_id_1, None, None, access_token
            )

            """Списание средств с копилки"""
            PersonalTransactionMethods.writing_off_money(
                result, description, transaction_type_consume, transaction_date, wallet_id_1, wallet_id_2,
                category_id_consume, amount, access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result, 201)

            """Получение списка транзакций"""
            result_get = PersonalTransactionMethods.get_personal_transaction(
                'Transfer between wallets', access_token
            )
            Checking.check_statuscode(result_get, 200)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_1, access_token)
            Checking.check_statuscode(result_delete, 204)

            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_2, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('transaction_type - Несуществующее значение')
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
        result_get = PersonalTransactionMethods.get_personal_transaction(
            'Income_transaction', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('transaction_type - Неверный тип данных integer (123)')
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
        result_get = PersonalTransactionMethods.get_personal_transaction(
            123456, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('transaction_type - Поле отсутствует')
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
        result_get = PersonalTransactionMethods.get_personal_transaction_without_transaction_type(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('transaction_type - Пустое поле')
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
        result_get = PersonalTransactionMethods.get_personal_transaction('', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Null')
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
        result_get = PersonalTransactionMethods.get_personal_transaction(
            None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)


