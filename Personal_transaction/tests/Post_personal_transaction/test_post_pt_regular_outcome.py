import allure
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
from common_methods.variables import PersonalTransactionVariables
from common_methods.checking import Checking
from Subcategory.methods.subcategory_methods import SubcategoryMethods
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
amount = PersonalTransactionVariables.amount
description = PersonalTransactionVariables.description
transaction_type_income = PersonalTransactionVariables.transaction_type_income
transaction_type_consume = PersonalTransactionVariables.transaction_type_consume
transaction_date = PersonalTransactionVariables.transaction_date
category_id_income = PersonalTransactionVariables.category_id_income
category_id_consume = PersonalTransactionVariables.category_id_consume
transaction_type_tbw = PersonalTransactionVariables.transaction_type_tbw


@allure.epic('Post/api/v1/personal_transaction/ Создание персональной транзакции Проверка поля regular_outcome_id')
class TestPTPostRegularOutcome:

    @allure.description('Проверка поля regular_outcome_id - Существующий id')
    def test_01(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание regular_outcome"""
        regular_outcome_result = RegularOutcomeMethods.create_regular_outcome(
            'title_desc', 156, None, 'День', 10, False,
            '2030-12-12', access_token
        )
        Checking.check_statuscode(regular_outcome_result, 201)
        print(regular_outcome_result.text)

        """Получение id подкатегории"""
        data = Checking.get_data(regular_outcome_result)
        regular_outcome_id = data['data']['id']
        try:
            """Создание транзакции"""
            result = PersonalTransactionMethods.create_personal_transaction_with_regular_outcome(
                amount, 't', transaction_type_income, transaction_date,
                None, wallet_id, category_id_income, None, regular_outcome_id, access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result, 201)

            """Проверка значения поля amount"""
            data = Checking.get_data(result)
            assert data['data']['regular_outcome_id'] == regular_outcome_id
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление подкатегории"""
            delete_result = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_result, 204)

    @allure.description('Проверка поля regular_outcome_id - Поле отсутствует')
    def test_02(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание подкатегории"""
        subcategory_result = SubcategoryMethods.create_subcategory(category_id_income, 'title', access_token)
        Checking.check_statuscode(subcategory_result, 201)

        """Получение id подкатегории"""
        subcategory_id = SubcategoryMethods.get_subcategory_id(subcategory_result)
        try:
            """Создание транзакции"""
            result = PersonalTransactionMethods.create_personal_transaction(
                amount, 't', transaction_type_income, transaction_date,
                None, wallet_id, category_id_income, subcategory_id, access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result, 201)

            """Проверка значения поля amount"""
            data = Checking.get_data(result)
            assert data['data']['amount'] == '0.00'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление подкатегории"""
            delete_result = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(delete_result, 204)

    @allure.description('Проверка поля regular_outcome_id - Null')
    def test_03(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание regular_outcome"""
        regular_outcome_result = RegularOutcomeMethods.create_regular_outcome(
            'title_desc', 156, None, 'День', 10, False,
            '2030-12-12', access_token
        )
        Checking.check_statuscode(regular_outcome_result, 201)
        print(regular_outcome_result.text)

        """Получение id подкатегории"""
        data = Checking.get_data(regular_outcome_result)
        regular_outcome_id = data['data']['id']
        try:
            """Создание транзакции"""
            result = PersonalTransactionMethods.create_personal_transaction_with_regular_outcome(
                amount, 't', transaction_type_income, transaction_date,
                None, wallet_id, category_id_income, None, None, access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(result, 201)

            """Проверка значения поля amount"""
            data = Checking.get_data(result)
            assert data['data']['regular_outcome_id'] is None
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление подкатегории"""
            delete_result = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_result, 204)

    @allure.description('Проверка поля regular_outcome_id - Несуществующий id')
    def test_04(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_with_regular_outcome(
            amount, 't', transaction_type_income, transaction_date,
            None, wallet_id, category_id_income, None, 9, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('Проверка поля regular_outcome_id - Значение id = 0')
    def test_05(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_with_regular_outcome(
            amount, 't', transaction_type_income, transaction_date,
            None, wallet_id, category_id_income, None, 9, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля regular_outcome_id - Отрицательное значение')
    def test_06(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_with_regular_outcome(
            amount, 't', transaction_type_income, transaction_date,
            None, wallet_id, category_id_income, None, -9, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля regular_outcome_id - Пустое поле')
    def test_07(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_with_regular_outcome(
            amount, 't', transaction_type_income, transaction_date,
            None, wallet_id, category_id_income, None, '', access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля regular_outcome_id - Неверный тип данных string')
    def test_08(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_with_regular_outcome(
            amount, 't', transaction_type_income, transaction_date,
            None, wallet_id, category_id_income, None, 'string',
            access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля regular_outcome_id - Вещественное число')
    def test_09(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_with_regular_outcome(
            amount, 't', transaction_type_income, transaction_date,
            None, wallet_id, category_id_income, None, 1.1, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)
