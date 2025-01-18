import allure
from Subcategory.methods.subcategory_methods import SubcategoryMethods
from common_methods.checking import Checking
from Subcategory.methods.payloads import SubcategoryPayloads
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
from common_methods.variables import PersonalTransactionVariables
category_id = 156
amount = PersonalTransactionVariables.amount
description = PersonalTransactionVariables.description
transaction_type_income = PersonalTransactionVariables.transaction_type_income
transaction_type_consume = PersonalTransactionVariables.transaction_type_consume
transaction_date = PersonalTransactionVariables.transaction_date
category_id_income = PersonalTransactionVariables.category_id_income
category_id_consume = PersonalTransactionVariables.category_id_consume


@allure.epic('Delete/api/v1/subcategory/ - Удаление подкатегории - общие проверки')
class TestDeleteSubcategoryCommon:

    @allure.description('Общие проверки - Удаление подкатегории без транзакций - полное удаление')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        print(f'Id_subcategory: {subcategory_id}')

        """Удаление подкатегории"""
        result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
        Checking.check_statuscode(result_delete, 204)

        """Получение информации о подкатегории"""
        result_get = SubcategoryMethods.get_subcategory_by_id(subcategory_id, access_token)
        Checking.check_statuscode(result_get, 404)

    @allure.description('Общие проверки - Удаление подкатегории с транзакциями - архивирование')
    def test_02(self, create_moneybox_and_delete_for_personal_transaction):
        """Авторизация"""
        moneybox_id, wallet_id, access_token = create_moneybox_and_delete_for_personal_transaction

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        print(f'Id_subcategory: {subcategory_id}')

        """Создание транзакций"""
        create_personal_transaction = PersonalTransactionMethods.create_personal_transaction(
            100, 'descr', transaction_type_income, '2024-01-01', None,
            wallet_id, 156, subcategory_id, access_token
        )
        Checking.check_statuscode(create_personal_transaction, 201)

        result_consumption = PersonalTransactionMethods.create_personal_transaction(
            100, 'descr', transaction_type_consume, '2024-01-01', None,
            wallet_id, 136, None, access_token
        )
        Checking.check_statuscode(result_consumption, 201)

        """Удаление подкатегории"""
        result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
        Checking.check_statuscode(result_delete, 204)

        """Получение информации о подкатегории"""
        result_get = SubcategoryMethods.get_subcategory_by_id(subcategory_id, access_token)
        Checking.check_statuscode(result_get, 200)


