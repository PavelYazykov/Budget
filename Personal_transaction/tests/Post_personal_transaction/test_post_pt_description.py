import allure
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


@allure.epic('Post/api/v1/personal_transaction/ Создание транзакции Проверкра поля description')
class TestPTPostDescription:

    @allure.description('Проверкра поля description - 1 символ')
    def test_01(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, 't', transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей и типа данных"""
        data = Checking.get_data(result)
        assert data['data']['description'] == 't'

    @allure.description('Проверкра поля description - 19 символов')
    def test_02(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount,
            'ttttttttttttttttttt',
            transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей и типа данных"""
        data = Checking.get_data(result)
        assert data['data']['description'] == 'ttttttttttttttttttt'

    @allure.description('Проверкра поля description - Цифры')
    def test_03(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, '012345678', transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей и типа данных"""
        data = Checking.get_data(result)
        assert data['data']['description'] == '012345678'

    @allure.description('Проверкра поля description - Кириллица')
    def test_04(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, 'Счет', transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей и типа данных"""
        data = Checking.get_data(result)
        assert data['data']['description'] == 'Счет'

    @allure.description('Проверкра поля description - Латиница')
    def test_05(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, 'Trans', transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей и типа данных"""
        data = Checking.get_data(result)
        assert data['data']['description'] == 'Trans'

    @allure.description('Проверкра поля description - Пробел')
    def test_06(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, 't t', transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей и типа данных"""
        data = Checking.get_data(result)
        assert data['data']['description'] == 't t'

    @allure.description('Проверкра поля description - Нижнее подчеркивание')
    def test_07(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, 't_t', transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей и типа данных"""
        data = Checking.get_data(result)
        assert data['data']['description'] == 't_t'

    @allure.description('Проверкра поля description - Тире')
    def test_08(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, 't-t', transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей и типа данных"""
        data = Checking.get_data(result)
        assert data['data']['description'] == 't-t'

    @allure.description('Проверкра поля description - Точка')
    def test_09(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, 't.t', transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей и типа данных"""
        data = Checking.get_data(result)
        assert data['data']['description'] == 't.t'

    @allure.description('Проверкра поля description - Поле отсутствует')
    def test_10(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction_without_description(
            amount, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

    @allure.description('Проверкра поля description - Null')
    def test_11(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, None, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей и типа данных"""
        data = Checking.get_data(result)
        assert data['data']['description'] is None

    @allure.description('Проверкра поля description - 21 символ')
    def test_12(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount,
            'ttttttttttttttttttttq',
            transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверкра поля description - Пустое поле')
    def test_13(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount,
            '',
            transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверкра поля description - Неверный тип данный integer')
    def test_14(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount,
            123456789,
            transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверкра поля description - Спецсимволы')
    def test_15(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction
        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount,
            '@#$%^&',
            transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)
