import allure
import pytest

from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
from common_methods.variables import PersonalTransactionVariables
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking
amount = PersonalTransactionVariables.amount
description = PersonalTransactionVariables.description
transaction_type_income = PersonalTransactionVariables.transaction_type_income
transaction_type_consume = PersonalTransactionVariables.transaction_type_consume
transaction_date = PersonalTransactionVariables.transaction_date
category_id_income = PersonalTransactionVariables.category_id_income
category_id_consume = PersonalTransactionVariables.category_id_consume


@pytest.mark.Personal_transaction
@allure.epic('Post/api/v1/personal_transaction/ Проверка поля amount')
class TestPostAmount:

    @allure.description('Проверка поля amount - Целое число')
    def test_01(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            10, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Обнуление баланса копилки"""
        result_consume = PersonalTransactionMethods.create_personal_transaction(
            10, description, transaction_type_consume, transaction_date, None, wallet_id,
            category_id_consume, None, access_token
        )
        Checking.check_statuscode(result_consume, 201)

        """Проверка значения поля amount"""
        data = Checking.get_data(result)
        assert data['data']['amount'] == '10.00'

    @allure.description('Проверка поля amount - Вещественное число')
    def test_02(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            10.10, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Обнуление баланса копилки"""
        result_consume = PersonalTransactionMethods.create_personal_transaction(
            10.10, description, transaction_type_consume, transaction_date, None, wallet_id,
            category_id_consume, None, access_token
        )
        Checking.check_statuscode(result_consume, 201)

        """Проверка значения поля amount"""
        data = Checking.get_data(result)
        assert data['data']['amount'] == '10.10'

    @allure.description('Значение = 0')
    def test_03(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            0, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Значение 9999999999.99')
    def test_04(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_moneybox = MoneyboxMethods.create_moneybox(
            '2030-12-31', 9999999999.99, 'moneybox', 2, 0, access_token
        )
        Checking.check_statuscode(result_moneybox, 201)

        """Получение wallet_id и moneybox_id"""
        wallet_id = MoneyboxMethods.get_wallet_id(result_moneybox)
        moneybox_id = MoneyboxMethods.get_moneybox_id(result_moneybox)
        try:
            """Создание транзакции"""
            result = PersonalTransactionMethods.create_personal_transaction(
                9999999999.99, description, transaction_type_income, transaction_date, None,
                wallet_id, category_id_income, None, access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result, 201)

            """Обнуление баланса копилки"""
            result_consume = PersonalTransactionMethods.create_personal_transaction(
                9999999999.99, description, transaction_type_consume, transaction_date, None,
                wallet_id, category_id_consume, None, access_token
            )
            Checking.check_statuscode(result_consume, 201)

            """Проверка значения поля amount"""
            data = Checking.get_data(result)
            print(data['data']['amount'])
            assert data['data']['amount'] == '9999999999.99'
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Значение 9999999999.111')
    def test_05(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_moneybox = MoneyboxMethods.create_moneybox(
            '2030-12-31', 9999999999.99, 'moneybox', 2, 0, access_token
        )
        Checking.check_statuscode(result_moneybox, 201)

        """Получение wallet_id и moneybox_id"""
        wallet_id = MoneyboxMethods.get_wallet_id(result_moneybox)
        moneybox_id = MoneyboxMethods.get_moneybox_id(result_moneybox)
        try:
            """Создание транзакции"""
            result = PersonalTransactionMethods.create_personal_transaction(
                9999999999.111, description, transaction_type_income, transaction_date, None,
                wallet_id, category_id_income, None, access_token
            )
            """Проверка статус кода"""
            print('RESULT:', result.json())
            Checking.check_statuscode(result, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Значение 10000000000')
    def test_06(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_moneybox = MoneyboxMethods.create_moneybox(
            '2030-12-31', 9999999999.99, 'moneybox', 2, 0, access_token
        )
        Checking.check_statuscode(result_moneybox, 201)

        """Получение wallet_id и moneybox_id"""
        wallet_id = MoneyboxMethods.get_wallet_id(result_moneybox)
        moneybox_id = MoneyboxMethods.get_moneybox_id(result_moneybox)
        try:
            """Создание транзакции"""
            result = PersonalTransactionMethods.create_personal_transaction(
                10000000000, description, transaction_type_income, transaction_date, None,
                wallet_id, category_id_income, None, access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Отрицательное значение')
    def test_07(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            -10, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Пустое поле')
    def test_08(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            '', description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Null')
    def test_09(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            None, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Неверный тип данный "string"')
    def test_10(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            'string', description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

