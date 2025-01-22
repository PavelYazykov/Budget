import allure
import pytest

from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
from common_methods.variables import PersonalTransactionVariables
from common_methods.checking import Checking
from common_methods.variables import AuthVariables
amount = PersonalTransactionVariables.amount
description = PersonalTransactionVariables.description
transaction_type_income = PersonalTransactionVariables.transaction_type_income
transaction_type_consume = PersonalTransactionVariables.transaction_type_consume
transaction_date = PersonalTransactionVariables.transaction_date
category_id_income = PersonalTransactionVariables.category_id_income
category_id_consume = PersonalTransactionVariables.category_id_consume
transaction_type_tbw = PersonalTransactionVariables.transaction_type_tbw
payloads = AuthVariables.auth_payloads_2


@pytest.mark.Personal_transaction
@allure.epic('Patch /api/v1/personal_transaction/{personal_transaction_id}/ Редактирование транзакций,'
             ' проверка поля description')
class TestPatchDescription:

    @allure.description('description - 1 символ')
    def test_01(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Редактирование транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            personal_transaction_id, 't', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка наличия обязательных полей"""
        data = Checking.get_data(result_patch)
        PersonalTransactionMethods.check_required_fields_get(data)

        """Проверка значения в изменяемом поле"""
        assert data['data']['description'] == 't'

    @allure.description('description - 19 символов')
    def test_02(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Редактирование транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            personal_transaction_id, 'ttttttttttttttttttt', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка наличия обязательных полей"""
        data = Checking.get_data(result_patch)
        PersonalTransactionMethods.check_required_fields_get(data)

        """Проверка значения в изменяемом поле"""
        assert data['data']['description'] == 'ttttttttttttttttttt'

    @allure.description('description - 20 символов')
    def test_03(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Редактирование транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            personal_transaction_id, 'tttttttttttttttttttq', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка наличия обязательных полей"""
        data = Checking.get_data(result_patch)
        PersonalTransactionMethods.check_required_fields_get(data)

        """Проверка значения в изменяемом поле"""
        assert data['data']['description'] == 'tttttttttttttttttttq'

    @allure.description('Цифры')
    def test_04(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Редактирование транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            personal_transaction_id, '123456789', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка наличия обязательных полей"""
        data = Checking.get_data(result_patch)
        PersonalTransactionMethods.check_required_fields_get(data)

        """Проверка значения в изменяемом поле"""
        assert data['data']['description'] == '123456789'

    @allure.description('description - Кириллица')
    def test_05(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Редактирование транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            personal_transaction_id, 'йцукен', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка наличия обязательных полей"""
        data = Checking.get_data(result_patch)
        PersonalTransactionMethods.check_required_fields_get(data)

        """Проверка значения в изменяемом поле"""
        assert data['data']['description'] == 'йцукен'

    @allure.description('description - Латиница')
    def test_06(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Редактирование транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            personal_transaction_id, 'tttttttttttttttttt', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка наличия обязательных полей"""
        data = Checking.get_data(result_patch)
        PersonalTransactionMethods.check_required_fields_get(data)

        """Проверка значения в изменяемом поле"""
        assert data['data']['description'] == 'tttttttttttttttttt'

    @allure.description('description - Пробел')
    def test_07(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Редактирование транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            personal_transaction_id, 'tttttttttttttttt t', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка наличия обязательных полей"""
        data = Checking.get_data(result_patch)
        PersonalTransactionMethods.check_required_fields_get(data)

        """Проверка значения в изменяемом поле"""
        assert data['data']['description'] == 'tttttttttttttttt t'

    @allure.description('description - Нижнее подчеркивание')
    def test_08(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Редактирование транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            personal_transaction_id, 'tttt_t', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка наличия обязательных полей"""
        data = Checking.get_data(result_patch)
        PersonalTransactionMethods.check_required_fields_get(data)

        """Проверка значения в изменяемом поле"""
        assert data['data']['description'] == 'tttt_t'

    @allure.description('description - Тире')
    def test_09(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Редактирование транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            personal_transaction_id, 'tttt-t', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка наличия обязательных полей"""
        data = Checking.get_data(result_patch)
        PersonalTransactionMethods.check_required_fields_get(data)

        """Проверка значения в изменяемом поле"""
        assert data['data']['description'] == 'tttt-t'

    @allure.description('description - Точка')
    def test_10(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Редактирование транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            personal_transaction_id, 'tttt.t', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка наличия обязательных полей"""
        data = Checking.get_data(result_patch)
        PersonalTransactionMethods.check_required_fields_get(data)

        """Проверка значения в изменяемом поле"""
        assert data['data']['description'] == 'tttt.t'

    @allure.description('description - Null')
    def test_10(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Редактирование транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            personal_transaction_id, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка наличия обязательных полей"""
        data = Checking.get_data(result_patch)
        PersonalTransactionMethods.check_required_fields_get(data)

        """Проверка значения в изменяемом поле"""
        assert data['data']['description'] is None

    @allure.description('description - без body')
    def test_11(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Редактирование транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_patch = PersonalTransactionMethods.change_personal_transaction_without_body(
            personal_transaction_id, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('description - 21 символ')
    def test_12(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Редактирование транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            personal_transaction_id, 'ttttttttttttttttttttq', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('description - Пустое поле')
    def test_13(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Редактирование транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            personal_transaction_id, '', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('description - Неверный тип данный integer')
    def test_14(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Редактирование транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            personal_transaction_id, 123456, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('description - Спецсимволы')
    def test_15(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Редактирование транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            personal_transaction_id, '@#$%^&*', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)


