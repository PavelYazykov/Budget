import allure

from common_methods.checking import Checking
from Personal_budget_auto_use.methods.personal_budget_auto_use_methods import PersonalBudgetAutoUseMethods
from Personal_budget_auto_use.methods.payloads_variables import Variables


@allure.epic('Post/api/v1/personal_budget_auto_use/ - Создание ежемесячного объекта бюджета - '
             'проверка поля transaction_type')
class TestPostAutoUseTransactionType:

    @allure.description('transaction_type - Транзакция Income')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            'Income', Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_auto_use_id = data['data']['id']
        try:
            """Проверка поля transaction_type"""
            data = Checking.get_data(result_create)
            transaction_type = data['data']['transaction_type']
            assert transaction_type == 'Income'
        finally:
            if personal_budget_auto_use_id is not None:
                delete_result = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
                    personal_budget_auto_use_id, access_token
                )
                Checking.check_statuscode(delete_result, 204)

    @allure.description('transaction_type - Транзакция Consumption')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            'Consumption', 20, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_auto_use_id = data['data']['id']
        try:
            """Проверка поля transaction_type"""
            data = Checking.get_data(result_create)
            transaction_type = data['data']['transaction_type']
            assert transaction_type == 'Consumption'
        finally:
            if personal_budget_auto_use_id is not None:
                delete_result = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
                    personal_budget_auto_use_id, access_token
                )
                Checking.check_statuscode(delete_result, 204)

    @allure.description('transaction_type - Транзакция TBW')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            'Transfer between wallets', Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('transaction_type - несуществующий тип транзакции')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            'Transfer', Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('transaction_type - Неверный тип данных integer')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            12345, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('transaction_type - Поле отсутствует')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use_without_transaction_type(
            Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('transaction_type - Пустое поле')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            "", Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('transaction_type - Null')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            None, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )
        """Проверка статус кода"""
        PersonalBudgetAutoUseMethods.delete_auto_use_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)
