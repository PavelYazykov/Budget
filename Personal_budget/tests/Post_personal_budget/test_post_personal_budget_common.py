import allure
import pytest

from common_methods.checking import Checking
from Personal_budget.methods.personal_budget_methods import PersonalBudgetMethods
from Personal_budget.methods.payloads import Variables, Payloads


@pytest.mark.Personal_budget
@allure.epic('Post/api/v1/personal_budget/ - Создание нового объекта персонального бюджета - общие проверки')
class TestPostPersonalBudgetCommon:

    @allure.description('общие проверки - Создание бюджета с валидными данными (авторизованный пользователь)')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
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
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление персонального бюджета"""
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)
            """Удаление регулярного списания"""
            PersonalBudgetMethods.delete_regular_outcome(access_token)

    @allure.description('общие проверки - Создание бюджета с валидными данными (неавторизованный пользователь)')
    def test_02(self):

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget_without_auth(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, Variables.have_to_remind,
            Variables.remind_in_days
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 401)

    @allure.description('общие проверки - Создание бюджета без body')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget_without_body(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('общие проверки - Для Income указать категорию соответствующую Consumption')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            Variables.transaction_type, 20, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, Variables.have_to_remind,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 400)

    @allure.description('общие проверки - Для Consumption указать категорию соответствующую Income')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            "Consumption", Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, Variables.have_to_remind,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 400)

    @allure.description('общие проверки - Без поля regular_outcome')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget_without_regular_outcome(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields(result_create, Payloads.post_payloads)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('общие проверки - regular_outcome - null')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget_and_regular_outcome_null(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields(result_create, Payloads.post_payloads)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('общие проверки - Создание двух одинаковых бюджетов в один месяц')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета 1"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, Variables.have_to_remind,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_id = data['data']['id']

        """Удаление регулярного списания"""
        PersonalBudgetMethods.delete_regular_outcome(access_token)

        try:
            """Создание персонального бюджета 2"""
            result_create_2 = PersonalBudgetMethods.create_personal_budget(
                Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
                Variables.month, Variables.year, Variables.date_reminder, Variables.title, Variables.have_to_remind,
                Variables.remind_in_days, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_create_2, 201)
            data_2 = Checking.get_data(result_create_2)
            personal_budget_id_2 = data_2['data']['id']
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id_2, access_token)

            """Удаление регулярного списания"""
            PersonalBudgetMethods.delete_regular_outcome(access_token)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление персонального бюджета"""
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('общие проверки - Дата в прошлом')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, 2024, Variables.date_reminder, Variables.title, Variables.have_to_remind,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        PersonalBudgetMethods.delete_personal_budget_if_bug(result_create, 201, access_token)
        Checking.check_statuscode(result_create, 422)

