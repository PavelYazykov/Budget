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


@allure.epic('Post/api/v1/personal_transaction/ Создание персональной транзакции Проверкра поля id_wallet_for_transfer')
class TestPTWalletForTransfer:

    @allure.description('Проверкра поля id_wallet_for_transfer - Существующий id')
    def test_01(self, auth_fixture):
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

            """Проверка значения поля amount"""
            data = Checking.get_data(result)
            assert data['data']['amount'] == '10.00'
        except AssertionError as error:
            print('Ошибка!')
            raise error
        finally:
            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_1, access_token)
            Checking.check_statuscode(result_delete, 204)

            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_2, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверкра поля id_wallet_for_transfer - Поле отсутствует при транзакции Income')
    def test_02(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, transaction_type_income, transaction_date, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных  полей"""
        Payloads.check_required_fields_post(result, Payloads.post_payloads)

    @allure.description('Проверкра поля id_wallet_for_transfer - Поле отсутствует при транзакции Consumption')
    def test_03(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, transaction_type_consume, transaction_date, wallet_id,
            category_id_consume, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных  полей"""
        Payloads.check_required_fields_post(result, Payloads.post_payloads)

    @allure.description(
        'Проверкра поля id_wallet_for_transfer - Поле отсутствует при транзакции Transfer between wallets'
    )
    def test_04(self, auth_fixture):
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

        moneybox_id_2 = MoneyboxMethods.get_moneybox_id(result_moneybox_2)
        try:
            """Создание транзакции"""
            result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
                10, description, 'Transfer between wallets', transaction_date,
                wallet_id_1, None, None, access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        except AssertionError as error:
            print('Ошибка!')
            raise error
        finally:
            """Обнуление баланса копилки"""
            PersonalTransactionMethods.create_personal_transaction(
                10, description, transaction_type_consume, transaction_date, None, wallet_id_1,
                category_id_consume, None, access_token
            )
            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_1, access_token)
            Checking.check_statuscode(result_delete, 204)

            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_2, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверкра поля id_wallet_for_transfer - Несуществующий id')
    def test_05(self, auth_fixture):
        """"Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_moneybox_1 = MoneyboxMethods.create_moneybox(
            '2030-12-31', 1000, 'moneybox', 2, 10, access_token
        )
        Checking.check_statuscode(result_moneybox_1, 201)

        """Получение wallet_id и moneybox_id"""
        wallet_id_1 = MoneyboxMethods.get_wallet_id(result_moneybox_1)
        moneybox_id_1 = MoneyboxMethods.get_moneybox_id(result_moneybox_1)

        try:
            """Создание транзакции"""
            result = PersonalTransactionMethods.create_personal_transaction(
                10, description, 'Transfer between wallets', transaction_date, 1,
                wallet_id_1, None, None, access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result, 404)
        except AssertionError as error:
            print('Ошибка!')
            raise error
        finally:
            """Обнуление баланса копилки"""
            PersonalTransactionMethods.create_personal_transaction(
                10, description, transaction_type_consume, transaction_date, None, wallet_id_1,
                category_id_consume, None, access_token
            )
            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_1, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверкра поля id_wallet_for_transfer - Вещественное число')
    def test_06(self, auth_fixture):
        """"Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_moneybox_1 = MoneyboxMethods.create_moneybox(
            '2030-12-31', 1000, 'moneybox', 2, 10, access_token
        )
        Checking.check_statuscode(result_moneybox_1, 201)

        """Получение wallet_id и moneybox_id"""
        wallet_id_1 = MoneyboxMethods.get_wallet_id(result_moneybox_1)
        moneybox_id_1 = MoneyboxMethods.get_moneybox_id(result_moneybox_1)

        try:
            """Создание транзакции"""
            result = PersonalTransactionMethods.create_personal_transaction(
                10, description, 'Transfer between wallets', transaction_date, 1.1,
                wallet_id_1, None, None, access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result, 404)
        except AssertionError as error:
            print('Ошибка!')
            raise error
        finally:
            """Обнуление баланса копилки"""
            PersonalTransactionMethods.create_personal_transaction(
                10, description, transaction_type_consume, transaction_date, None, wallet_id_1,
                category_id_consume, None, access_token
            )
            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_1, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверкра поля id_wallet_for_transfer - Значение id = 0')
    def test_07(self, auth_fixture):
        """"Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_moneybox_1 = MoneyboxMethods.create_moneybox(
            '2030-12-31', 1000, 'moneybox', 2, 10, access_token
        )
        Checking.check_statuscode(result_moneybox_1, 201)

        """Получение wallet_id и moneybox_id"""
        wallet_id_1 = MoneyboxMethods.get_wallet_id(result_moneybox_1)
        moneybox_id_1 = MoneyboxMethods.get_moneybox_id(result_moneybox_1)
        try:
            """Создание транзакции"""
            result = PersonalTransactionMethods.create_personal_transaction(
                10, description, 'Transfer between wallets', transaction_date, 0,
                wallet_id_1, None, None, access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        except AssertionError as error:
            print('Ошибка!')
            raise error
        finally:
            """Обнуление баланса копилки"""
            PersonalTransactionMethods.create_personal_transaction(
                10, description, transaction_type_consume, transaction_date, None, wallet_id_1,
                category_id_consume, None, access_token
            )
            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_1, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверкра поля id_wallet_for_transfer - Отрицательный id')
    def test_08(self, auth_fixture):
        """"Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_moneybox_1 = MoneyboxMethods.create_moneybox(
            '2030-12-31', 1000, 'moneybox', 2, 10, access_token
        )
        Checking.check_statuscode(result_moneybox_1, 201)

        """Получение wallet_id и moneybox_id"""
        wallet_id_1 = MoneyboxMethods.get_wallet_id(result_moneybox_1)
        moneybox_id_1 = MoneyboxMethods.get_moneybox_id(result_moneybox_1)
        try:
            """Создание транзакции"""
            result = PersonalTransactionMethods.create_personal_transaction(
                10, description, 'Transfer between wallets', transaction_date, 1,
                wallet_id_1, None, None, access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        except AssertionError as error:
            print('Ошибка!')
            raise error
        finally:
            """Обнуление баланса копилки"""
            PersonalTransactionMethods.create_personal_transaction(
                10, description, transaction_type_consume, transaction_date, None, wallet_id_1,
                category_id_consume, None, access_token
            )
            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_1, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверкра поля id_wallet_for_transfer - Неверный тип данных string (id = "string")')
    def test_09(self, auth_fixture):
        """"Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_moneybox_1 = MoneyboxMethods.create_moneybox(
            '2030-12-31', 1000, 'moneybox', 2, 10, access_token
        )
        Checking.check_statuscode(result_moneybox_1, 201)

        """Получение wallet_id и moneybox_id"""
        wallet_id_1 = MoneyboxMethods.get_wallet_id(result_moneybox_1)
        moneybox_id_1 = MoneyboxMethods.get_moneybox_id(result_moneybox_1)
        try:
            """Создание транзакции"""
            result = PersonalTransactionMethods.create_personal_transaction(
                10, description, 'Transfer between wallets', transaction_date,
                'string', wallet_id_1, None, None, access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        except AssertionError as error:
            print('Ошибка!')
            raise error
        finally:
            """Обнуление баланса копилки"""
            PersonalTransactionMethods.create_personal_transaction(
                10, description, transaction_type_consume, transaction_date, None, wallet_id_1,
                category_id_consume, None, access_token
            )
            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_1, access_token)
            Checking.check_statuscode(result_delete, 204)
