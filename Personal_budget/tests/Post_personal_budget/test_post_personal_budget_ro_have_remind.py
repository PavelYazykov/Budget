import allure
from datetime import date
from common_methods.checking import Checking
from Personal_budget.methods.personal_budget_methods import PersonalBudgetMethods
from Personal_budget.methods.payloads import Variables, Payloads

current_date = str(date.today())


@allure.epic('Post/api/v1/personal_budget/ - Создание нового объекта персонального бюджета - '
             'Раздел regular_outcome/проверка поля have_to_remind')
class TestPostPersonalBudgetHaveRemind:

    @allure.description('проверка поля have_to_remind - True')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, True,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields(result_create, Payloads.post_payloads)
        except AssertionError:
            raise AssertionError
        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('проверка поля have_to_remind - False')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, False,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields(result_create, Payloads.post_payloads)
        except AssertionError:
            raise AssertionError
        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('проверка поля have_to_remind - Пустое поле')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, '',
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetMethods.delete_personal_budget_if_bug(result_create, 201, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('проверка поля have_to_remind - Поле отсутствует')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget_without_have_to_remind(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetMethods.delete_personal_budget_if_bug(result_create, 201, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('проверка поля have_to_remind - Null')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, None,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetMethods.delete_personal_budget_if_bug(result_create, 201, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('проверка поля have_to_remind - Неверный тип данных integer')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, 123,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetMethods.delete_personal_budget_if_bug(result_create, 201, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('проверка поля have_to_remind - Неверный тип данных string')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, 'string',
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetMethods.delete_personal_budget_if_bug(result_create, 201, access_token)
        Checking.check_statuscode(result_create, 422)


