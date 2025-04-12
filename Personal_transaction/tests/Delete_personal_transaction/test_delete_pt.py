import time

import allure
import pytest

from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
from common_methods.variables import PersonalTransactionVariables, AuthVariables
from common_methods.checking import Checking
from common_methods.auth import Auth
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from Auth.methods.auth_methods import AuthMethods
amount = PersonalTransactionVariables.amount
description = PersonalTransactionVariables.description
transaction_type_income = PersonalTransactionVariables.transaction_type_income
transaction_type_consume = PersonalTransactionVariables.transaction_type_consume
transaction_date = PersonalTransactionVariables.transaction_date
category_id_income = PersonalTransactionVariables.category_id_income
category_id_consume = PersonalTransactionVariables.category_id_consume
transaction_type_tbw = PersonalTransactionVariables.transaction_type_tbw


@pytest.mark.Personal_transaction
@allure.epic('Delete /api/v1/personal_transaction/{personal_transaction_id}/ Редактирование транзакций, общие проверки')
class TestDeletePersonalTransaction:

    @allure.description('Удаление транзакции с существующим id (авторизованный пользователь)')
    def test_01(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Удаление транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_delete = PersonalTransactionMethods.delete_personal_transaction(personal_transaction_id, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 204)

        """Повторное удаление транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_delete = PersonalTransactionMethods.delete_personal_transaction(personal_transaction_id, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 404)

        """Получение удаленной транзакции"""
        result_get = PersonalTransactionMethods.get_personal_transaction_by_id(
            personal_transaction_id, access_token
        )

    @allure.description('Удаление транзакции с существующим id (неавторизованный пользователь)')
    def test_02(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Удаление транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_delete = PersonalTransactionMethods.delete_personal_transaction_without_auth(personal_transaction_id)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 401)

    @allure.description('Удаление транзакции с Несуществующим id')
    def test_03(self, auth_fixture):
        """Авторизациия"""
        access_token = auth_fixture

        """Удаление транзакции"""
        result_delete = PersonalTransactionMethods.delete_personal_transaction(1, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 404)

    @allure.description('Удаление транзакции с id = 0')
    def test_04(self, auth_fixture):
        """Авторизациия"""
        access_token = auth_fixture

        """Удаление транзакции"""
        result_delete = PersonalTransactionMethods.delete_personal_transaction(0, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление транзакции с id = отрицательное значение')
    def test_05(self, auth_fixture):
        """Авторизациия"""
        access_token = auth_fixture

        """Удаление транзакции"""
        result_delete = PersonalTransactionMethods.delete_personal_transaction(-1, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление транзакции с id - Поле отсутствует')
    def test_06(self, auth_fixture):
        """Авторизациия"""
        access_token = auth_fixture

        """Удаление транзакции"""
        result_delete = PersonalTransactionMethods.delete_personal_transaction_without_id(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 405)

    @allure.description('Удаление транзакции с id = пустое поле')
    def test_07(self, auth_fixture):
        """Авторизациия"""
        access_token = auth_fixture

        """Удаление транзакции"""
        result_delete = PersonalTransactionMethods.delete_personal_transaction('', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 404)

    @allure.description('Удаление транзакции с id = Null')
    def test_08(self, auth_fixture):
        """Авторизациия"""
        access_token = auth_fixture

        """Удаление транзакции"""
        result_delete = PersonalTransactionMethods.delete_personal_transaction(None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление транзакции с id = Вещественное число (id = 1,1)')
    def test_09(self, auth_fixture):
        """Авторизациия"""
        access_token = auth_fixture

        """Удаление транзакции"""
        result_delete = PersonalTransactionMethods.delete_personal_transaction(1.1, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление транзакции с id = Неверный тип данных string')
    def test_10(self, auth_fixture):
        """Авторизациия"""
        access_token = auth_fixture

        """Удаление транзакции"""
        result_delete = PersonalTransactionMethods.delete_personal_transaction('string', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление транзакции чужого пользователя')
    def test_11(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result_pt = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result_pt, 201)

        """Получение personal transaction id"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result_pt)

        """Создание второго пользователя"""
        result_create_second_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_second_user, 201)
        data, user_id = AuthMethods.get_id(result_create_second_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Авторизация второго пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token_2 = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Удаление копилки другого пользователя"""
            result_delete = PersonalTransactionMethods.delete_personal_transaction(personal_transaction_id, access_token_2)
            Checking.check_statuscode(result_delete, 400)
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Удалить транзакцию с копилкой, при этом копилка в архиве')
    def test_12(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Получение personal transaction id"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)

        """Перенос копилки в архив"""
        result_archived = MoneyboxMethods.change_moneybox(
            moneybox_id, '2030-12-12', 1000, 'name', 2, True, access_token
        )
        Checking.check_statuscode(result_archived, 200)

        """Удаление транзакции"""
        result_delete = PersonalTransactionMethods.delete_personal_transaction(personal_transaction_id, access_token)
        Checking.check_statuscode(result_delete, 400)

    @allure.description('Удалить транзакцию "доход", чтобы баланс wallet/копилки стал отрицательным')
    def test_13(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Пополнение копилки"""
        result_income = PersonalTransactionMethods.create_personal_transaction(
            200, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result_income, 201)

        """Получение personal transaction id"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result_income)

        """Списание средств с копилки"""
        result_consumption = PersonalTransactionMethods.create_personal_transaction(
            200, description, transaction_type_consume, transaction_date, None, wallet_id,
            category_id_consume, None, access_token
        )
        Checking.check_statuscode(result_consumption, 201)

        """Удаление транзакции"""
        result_delete = PersonalTransactionMethods.delete_personal_transaction(
            personal_transaction_id, access_token
        )
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удалить транзакцию расход (сумма в wallet/копилке увеличивается на сумму транзакции)')
    def test_14(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Пополнение копилки"""
        result_income = PersonalTransactionMethods.create_personal_transaction(
            200, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result_income, 201)

        """Списание средств с копилки"""
        result_consumption = PersonalTransactionMethods.create_personal_transaction(
            200, description, transaction_type_consume, transaction_date, None, wallet_id,
            category_id_consume, None, access_token
        )
        Checking.check_statuscode(result_consumption, 201)

        """Получение personal transaction id"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result_consumption)
        print(f'personal_transaction_id: {personal_transaction_id}')

        """Удаление транзакции"""
        result_delete = PersonalTransactionMethods.delete_personal_transaction(
            personal_transaction_id, access_token
        )
        Checking.check_statuscode(result_delete, 204)
        try:
            """Проверка баланса копилки"""
            result_get = MoneyboxMethods.get_one_moneybox(moneybox_id, access_token)
            data = Checking.get_data(result_get)
            print(data)
            assert data['data']['wallet']['amount'] == '200.00'
        except AssertionError:
            raise AssertionError
        finally:
            """Списание средств с копилки"""
            result_consumption = PersonalTransactionMethods.create_personal_transaction(
                200, description, transaction_type_consume, transaction_date, None,
                wallet_id, category_id_consume, None, access_token
            )
            Checking.check_statuscode(result_consumption, 201)
            """Удаление копилки"""
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

    @allure.description('Удалить транзакцию расход, чтобы баланс wallet/копилки превышал max число')
    def test_15(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        create_result = MoneyboxMethods.create_moneybox(
            '2030-12-30', 9999999999.99, 'name', 2, 9999999999, access_token
        )
        Checking.check_statuscode(create_result, 201)

        """Получение wallet id"""
        data = Checking.get_data(create_result)
        wallet_id = data['data']['wallet']['id']
        try:
            """Списание средств с копилки"""
            result_consumption = PersonalTransactionMethods.create_personal_transaction(
                200, description, transaction_type_consume, transaction_date, None, wallet_id,
                category_id_consume, None, access_token
            )
            Checking.check_statuscode(result_consumption, 201)

            """Получение personal transaction id"""
            personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result_consumption)

            """Пополнение копилки"""
            result_income = PersonalTransactionMethods.create_personal_transaction(
                200, description, transaction_type_income, transaction_date, None, wallet_id,
                category_id_income, None, access_token
            )
            Checking.check_statuscode(result_income, 201)

            """Удаление транзакции"""
            result_delete = PersonalTransactionMethods.delete_personal_transaction(
                personal_transaction_id, access_token
            )
            Checking.check_statuscode(result_delete, 400)
        except AssertionError:
            raise AssertionError
        finally:
            """Списание средств с копилки"""
            result_consumption = PersonalTransactionMethods.create_personal_transaction(
                9999999999, description, transaction_type_consume, transaction_date, None,
                wallet_id, category_id_consume, None, access_token
            )
            Checking.check_statuscode(result_consumption, 201)

            """Удаление копилки"""
            data = Checking.get_data(create_result)
            moneybox_id = data['data']['id']
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Удалить транзакцию перевод между счетами (один из кошельков в архиве)')
    def test_16(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилкок"""
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

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            10, description, 'Transfer between wallets', transaction_date, wallet_id_2,
            wallet_id_1, None, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Получение personal transaction id"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)

        try:
            """Перенос копилки в архив"""
            result_archived = MoneyboxMethods.change_moneybox(
                moneybox_id_1, '2030-12-12', 1000, 'None', 2, True, access_token
            )
            Checking.check_statuscode(result_archived, 200)

            """Удаление транзакции"""
            result_delete = PersonalTransactionMethods.delete_personal_transaction(
                personal_transaction_id, access_token
            )
            Checking.check_statuscode(result_delete, 400)

        except AssertionError:
            raise AssertionError
        finally:
            """Списание средств с копилки"""
            result = PersonalTransactionMethods.create_personal_transaction(
                10, description, transaction_type_consume, transaction_date, None,
                wallet_id_2, category_id_consume, None, access_token
            )
            Checking.check_statuscode(result, 201)

            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_1, access_token)
            Checking.check_statuscode(result_delete, 204)

            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_2, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Удалить транзакцию перевод между счетами'
                        ' (кошелек получателя баланс отрицательный, кошелек отправителя баланс превышает max число)')
    def test_17(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_moneybox_1 = MoneyboxMethods.create_moneybox(
            '2030-12-31', 9999999999.99, 'moneybox', 2, 100, access_token
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

        """Создание транзакции перевод между счетами"""
        result = PersonalTransactionMethods.create_personal_transaction(
            100, description, 'Transfer between wallets', transaction_date, wallet_id_2,
            wallet_id_1, None, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Получение personal transaction id (перевод между счетами)"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)

        """Создание транзакции (пополнение первого wallet)"""
        result_income = PersonalTransactionMethods.create_personal_transaction(
            9999999999, description, transaction_type_income, transaction_date, None,
            wallet_id_1, category_id_income, None, access_token
        )
        Checking.check_statuscode(result_income, 201)

        """Создание транзакции (списание со второго wallet)"""
        result_income = PersonalTransactionMethods.create_personal_transaction(
            100, description, transaction_type_consume, transaction_date, None,
            wallet_id_2, category_id_consume, None, access_token
        )
        Checking.check_statuscode(result_income, 201)
        try:
            """Удаление транзакции перевод между счетами"""
            result_delete = PersonalTransactionMethods.delete_personal_transaction(personal_transaction_id, access_token)
            Checking.check_statuscode(result_delete, 400)
        except AssertionError:
            raise AssertionError
        finally:
            """Списание средств с первой копилки"""
            result = PersonalTransactionMethods.create_personal_transaction(
                9999999999, description, transaction_type_consume, transaction_date, None,
                wallet_id_1, category_id_consume, None, access_token
            )
            Checking.check_statuscode(result, 201)

            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_1, access_token)
            Checking.check_statuscode(result_delete, 204)

            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_2, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Удалить транзакцию "перевод между счетами" (баланс копилки отправителя превышает '
                        'сумму цели, а баланс копилки получателя стал отрицательным)')
    def test_18(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_moneybox_1 = MoneyboxMethods.create_moneybox(
            '2030-12-31', 1000, 'moneybox', 2, 100, access_token
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

        """Создание транзакции перевод между счетами"""
        result = PersonalTransactionMethods.create_personal_transaction(
            100, description, 'Transfer between wallets', transaction_date, wallet_id_2,
            wallet_id_1, None, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Получение personal transaction id (перевод между счетами)"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)

        """Создание транзакции (пополнение первого wallet)"""
        result_income = PersonalTransactionMethods.create_personal_transaction(
            950, description, transaction_type_income, transaction_date, None,
            wallet_id_1, category_id_income, None, access_token
        )
        Checking.check_statuscode(result_income, 201)

        """Создание транзакции (списание со второго wallet)"""
        result_income = PersonalTransactionMethods.create_personal_transaction(
            100, description, transaction_type_consume, transaction_date, None,
            wallet_id_2, category_id_consume, None, access_token
        )
        Checking.check_statuscode(result_income, 201)
        try:
            """Удаление транзакции перевод между счетами"""
            result_delete = PersonalTransactionMethods.delete_personal_transaction(personal_transaction_id, access_token)
            Checking.check_statuscode(result_delete, 400)
        except AssertionError:
            raise AssertionError
        finally:
            """Списание средств с первой копилки"""
            result = PersonalTransactionMethods.create_personal_transaction(
                950, description, transaction_type_consume, transaction_date, None,
                wallet_id_1, category_id_consume, None, access_token
            )
            Checking.check_statuscode(result, 201)

            """Удаление копилки"""
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_1, access_token)
            Checking.check_statuscode(result_delete, 204)

            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id_2, access_token)
            Checking.check_statuscode(result_delete, 204)
