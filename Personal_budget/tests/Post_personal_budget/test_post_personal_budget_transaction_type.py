import allure

from common_methods.checking import Checking
from Personal_budget.methods.personal_budget_methods import PersonalBudgetMethods
from Personal_budget.methods.payloads import Variables, Payloads


@allure.epic('Post/api/v1/personal_budget/ - Создание нового объекта персонального бюджета - '
             'проверка поля transaction_type')
class TestPostPersonalBudgetTransactionType:

    @allure.description('проверка поля transaction_type - Транзакция Income')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            "Income", Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, Variables.have_to_remind,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields(result_create, Payloads.post_payloads)
        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('проверка поля transaction_type - Транзакция Consumption')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            "Consumption", 20, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, Variables.have_to_remind,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields(result_create, Payloads.post_payloads)
        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('проверка поля transaction_type - Транзакция Transfer between wallets')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            "Transfer between wallets", 20, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, Variables.have_to_remind,
            Variables.remind_in_days, access_token
        )
        try:
            """Проверка статус кода"""
            Checking.check_statuscode(result_create, 422)
        finally:
            if result_create.status_code == 201:
                data = Checking.get_data(result_create)
                personal_budget_id = data['data']['id']
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('проверка поля transaction_type - Несуществующий тип транзакции')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            "Incoming", Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, Variables.have_to_remind,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetMethods.delete_personal_budget_if_bug(result_create, 201, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('проверка поля transaction_type - Неверный тип данных integer')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            1234, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, Variables.have_to_remind,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetMethods.delete_personal_budget_if_bug(result_create, 201, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('проверка поля transaction_type - Поле отсутствует')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget_without_transaction_type(
            Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, Variables.have_to_remind,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetMethods.delete_personal_budget_if_bug(result_create, 201, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('проверка поля transaction_type - Пустое поле')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            "", Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, Variables.have_to_remind,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetMethods.delete_personal_budget_if_bug(result_create, 201, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('проверка поля transaction_type - Null')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            None, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, Variables.have_to_remind,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetMethods.delete_personal_budget_if_bug(result_create, 201, access_token)
        Checking.check_statuscode(result_create, 422)

