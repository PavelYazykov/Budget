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


@allure.epic('Post/api/v1/personal_transaction/ Создание персональной транзакции Проверка поля category_id')
class TestPostPTCategoryId:

    @allure.description('Проверка поля category_id - Существующий id')
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

        """Проверка наличия обязательных  полей"""
        Payloads.check_required_fields_post(result, Payloads.post_payloads)

    @allure.description('Проверка поля category_id - Поле отсутствует при тразакции Income')
    def test_02(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, transaction_type_income, transaction_date, wallet_id,
            None, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 400)

    @allure.description('Проверка поля category_id - Поле отсутствует при тразакции Consumption')
    def test_03(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, transaction_type_consume, transaction_date, wallet_id,
            None, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 400)

    @allure.description('Проверка поля category_id - Поле отсутствует при тразакции TBW')
    def test_04(self, auth_fixture):
        """"Авторизация"""
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
            result = PersonalTransactionMethods.create_personal_transaction_without_category(
                10, description, 'Transfer between wallets', transaction_date,
                wallet_id_2, wallet_id_1, None, access_token
            )
            Checking.check_statuscode(result, 201)

            """Списание средств с копилки"""
            PersonalTransactionMethods.writing_off_money(
                result, description, transaction_type_consume, transaction_date, wallet_id_1, wallet_id_2,
                category_id_consume, 10, access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result, 201)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_1, access_token)
            Checking.check_statuscode(result_delete, 204)

            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_2, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля category_id - Null - при тразакции Income')
    def test_05(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, transaction_type_income, transaction_date, wallet_id,
            None, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 400)

    @allure.description('Проверка поля category_id - Null - при тразакции Consumption')
    def test_06(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, transaction_type_consume, transaction_date, wallet_id,
            None, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 400)

    @allure.description('Проверка поля category_id - Null - при тразакции TBW')
    def test_07(self, auth_fixture):
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
                category_id_consume, 10, access_token
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

    @allure.description('Проверка поля category_id - Несуществующий id')
    def test_08(self, create_moneybox_and_delete_for_personal_transaction):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            1, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('Проверка поля category_id - Значение id = 0')
    def test_09(self, create_moneybox_and_delete_for_personal_transaction):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            0, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля category_id - Отрицательное значение (id = -1)')
    def test_10(self, create_moneybox_and_delete_for_personal_transaction):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            -1, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля category_id - Пустое поле')
    def test_11(self, create_moneybox_and_delete_for_personal_transaction):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            '', None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля category_id - Неверный тип данных string (id = "string")')
    def test_12(self, create_moneybox_and_delete_for_personal_transaction):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            'string', None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля category_id - Вещественное число (id = 1,1)')
    def test_13(self, create_moneybox_and_delete_for_personal_transaction):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            1.1, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)
