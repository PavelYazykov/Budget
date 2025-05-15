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
@allure.epic('Post/api/v1/personal_transaction/ Создание персональной транзакции')
class TestPTCommonCheck:

    @allure.description('Создание транзакции "Income" с валидными данными (авторизованный пользователь)')
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

        """Проверка значения поля amount"""
        data = Checking.get_data(result)
        assert data['data']['amount'] == '10.00'

    @allure.description('Создание транзакции "Consumption" с валидными данными (авторизованный пользователь)')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_moneybox = MoneyboxMethods.create_moneybox(
            '2030-12-31', 1000, 'moneybox', 2, 10, access_token
        )
        Checking.check_statuscode(result_moneybox, 201)

        """Получение wallet_id и moneybox_id"""
        wallet_id = MoneyboxMethods.get_wallet_id(result_moneybox)
        moneybox_id = MoneyboxMethods.get_moneybox_id(result_moneybox)
        try:
            """Создание транзакции"""
            result = PersonalTransactionMethods.create_personal_transaction(
                10, description, transaction_type_consume, transaction_date, None, wallet_id,
                category_id_consume, None, access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result, 201)

            """Проверка значения поля amount"""
            data = Checking.get_data(result)
            print(data['data']['amount'])
            assert data['data']['amount'] == '10.00'
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Создание транзакции "Transfer between wallet" с валидными данными авторизованный пользователь')
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
        print('информация по валетам и копилкам заканчивается')
        try:
            """Создание транзакции"""
            result = PersonalTransactionMethods.create_personal_transaction(
                10, description, 'Transfer between wallets', transaction_date, wallet_id_2,
                wallet_id_1, None, None, access_token
            )
            print('RESULT:', result.json())

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
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_1, access_token)
            Checking.check_statuscode(result_delete, 204)

            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_2, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Создание транзакции (неавторизованный пользователь)')
    def test_04(self):
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_auth(
            amount, description, transaction_type_income, transaction_date, None, 99,
            category_id_income, None
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 401)

    @allure.description('Создание транзакции без body')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_body(access_token)
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('При создании транзакции "Income", указать кошелек списания')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_moneybox_1 = MoneyboxMethods.create_moneybox(
            '2030-12-31', 1000, 'moneybox', 2, 0, access_token
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
                0, description, 'Income', transaction_date, wallet_id_2,
                wallet_id_1, category_id_income, None, access_token
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
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_1, access_token)
            Checking.check_statuscode(result_delete, 204)

            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_2, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('При создании транзакции "Transfer between wallets" не указать кошелек списания')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_moneybox_2 = MoneyboxMethods.create_moneybox(
            '2030-12-31', 1000, 'moneybox_2', 2, 0, access_token
        )
        Checking.check_statuscode(result_moneybox_2, 201)

        """Получение wallet_id и moneybox_id"""
        wallet_id_2 = MoneyboxMethods.get_wallet_id(result_moneybox_2)
        moneybox_id_2 = MoneyboxMethods.get_moneybox_id(result_moneybox_2)
        try:
            """Создание транзакции"""
            result = PersonalTransactionMethods.create_personal_transaction(
                10, description, 'Transfer between wallets', transaction_date, wallet_id_2,
                None, category_id_consume, None, access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_2, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('При создании транзакции "Transfer between wallets" не указать кошелек пополнения')
    def test_08(self, auth_fixture):
        """Авторизация"""
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
                10, description, 'Transfer between wallets', transaction_date, None,
                wallet_id_1, None, None, access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result, 400)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Списание средств с копилки"""
            result_consume = PersonalTransactionMethods.create_personal_transaction(
                10, description, transaction_type_consume, transaction_date, None, wallet_id_1,
                category_id_consume, None, access_token
            )
            Checking.check_statuscode(result_consume, 201)
            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_1, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Перевести сумму больше чем есть на wallet')
    def test_09(self, auth_fixture):
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
                20, description, 'Transfer between wallets', transaction_date, wallet_id_2,
                wallet_id_1, None, None, access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result, 400)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Списание средств с копилки"""
            result_consume = PersonalTransactionMethods.create_personal_transaction(
                10, description, transaction_type_consume, transaction_date, None, wallet_id_1,
                category_id_consume, None, access_token
            )
            Checking.check_statuscode(result_consume, 201)
            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_1, access_token)
            Checking.check_statuscode(result_delete, 204)

            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_2, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Пополнить копилку на сумму превышающую цель')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_moneybox = MoneyboxMethods.create_moneybox(
            '2030-12-31', 1000, 'moneybox', 2, 0, access_token
        )
        Checking.check_statuscode(result_moneybox, 201)

        """Получение wallet_id и moneybox_id"""
        wallet_id = MoneyboxMethods.get_wallet_id(result_moneybox)
        moneybox_id = MoneyboxMethods.get_moneybox_id(result_moneybox)
        try:
            """Создание транзакции"""
            result = PersonalTransactionMethods.create_personal_transaction(
                2000, description, transaction_type_income, transaction_date, None, wallet_id,
                category_id_income, None, access_token
            )
            """Проверка статус кода"""
            if result.status_code == 201:
                """Обнуление баланса копилки"""
                PersonalTransactionMethods.create_personal_transaction(
                    2000, description, transaction_type_consume, transaction_date, None,
                    wallet_id, category_id_consume, None, access_token
                )
            Checking.check_statuscode(result, 400)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Для Consumption указать категорию соответствующую Income')
    def test_11(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            3000, description, transaction_type_consume, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 400)

    @allure.description('Для Income указать категорию соответствующую Consumption')
    def test_12(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            50, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_consume, None, access_token
        )
        """Проверка статус кода"""
        if result.status_code == 201:
            PersonalTransactionMethods.create_personal_transaction(
                50, description, transaction_type_consume, transaction_date, None, wallet_id,
                category_id_consume, None, access_token
            )
        Checking.check_statuscode(result, 400)




