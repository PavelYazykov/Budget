import allure
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
from common_methods.variables import PersonalTransactionVariables
from common_methods.checking import Checking
from common_methods.auth import Auth
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


@allure.epic('Patch /api/v1/personal_transaction/{personal_transaction_id}/ Редактирование транзакций, общие проверки')
class TestPatchCommonCheck:

    @allure.description('Изменение транзакции с существующим id (авторизованный пользователь)')
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
            personal_transaction_id, 'title', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка наличия обязательных полей"""
        data = Checking.get_data(result_patch)
        PersonalTransactionMethods.check_required_fields_get(data)

        """Проверка значения в изменяемом поле"""
        assert data['data']['description'] == 'title'

    @allure.description('Изменение транзакции с существующим id (авторизованный пользователь)')
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
        result_patch = PersonalTransactionMethods.change_personal_transaction_without_auth(
            personal_transaction_id, 'title'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 401)

    @allure.description('Редактирование транзакции чужого пользователя')
    def test_03(self, create_moneybox_and_delete_for_personal_transaction):
        """Создание копилки"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание транзакции"""
        result = PersonalTransactionMethods.create_personal_transaction(
            amount, description, transaction_type_income, transaction_date, None, wallet_id,
            category_id_income, None, access_token
        )
        Checking.check_statuscode(result, 201)

        """Авторизация второго пользователя"""
        auth_result = Auth.auth_with_params('22222', payloads)
        Checking.check_statuscode(auth_result, 200)
        data = Checking.get_data(auth_result)
        access_token_2 = data['access_token']

        """Редактирование транзакции"""
        personal_transaction_id = PersonalTransactionMethods.get_personal_transaction_id(result)
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            personal_transaction_id, 'title', access_token_2
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 404)

    @allure.description('Несуществующий id')
    def test_04(self, auth_fixture):
        """Авторизациия"""
        access_token = auth_fixture

        """Редактирование транзакции"""
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            1, 'title', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 404)

    @allure.description('id = вещественное число (1,5)')
    def test_05(self, auth_fixture):
        """Авторизациия"""
        access_token = auth_fixture

        """Редактирование транзакции"""
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            1.5, 'title', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('id = 0')
    def test_06(self, auth_fixture):
        """Авторизациия"""
        access_token = auth_fixture

        """Редактирование транзакции"""
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            0, 'title', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('id = отрицательное число')
    def test_07(self, auth_fixture):
        """Авторизациия"""
        access_token = auth_fixture

        """Редактирование транзакции"""
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            0, 'title', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('id = string ("строка")')
    def test_08(self, auth_fixture):
        """Авторизациия"""
        access_token = auth_fixture

        """Редактирование транзакции"""
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            'string', 'title', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('id - Поле отсутствует')
    def test_09(self, auth_fixture):
        """Авторизациия"""
        access_token = auth_fixture

        """Редактирование транзакции"""
        result_patch = PersonalTransactionMethods.change_personal_transaction_without_id(
            'title', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 405)

    @allure.description('id = Пустое поле')
    def test_10(self, auth_fixture):
        """Авторизациия"""
        access_token = auth_fixture

        """Редактирование транзакции"""
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            '', 'title', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 405)

    @allure.description('Null')
    def test_11(self, auth_fixture):
        """Авторизациия"""
        access_token = auth_fixture

        """Редактирование транзакции"""
        result_patch = PersonalTransactionMethods.change_personal_transaction(
            None, 'title', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

