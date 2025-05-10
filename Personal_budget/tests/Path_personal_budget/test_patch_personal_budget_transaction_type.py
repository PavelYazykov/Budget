import allure
import pytest

from common_methods.checking import Checking
from Personal_budget.methods.personal_budget_methods import PersonalBudgetMethods
from Personal_budget.methods.payloads import Variables


@pytest.mark.personal_budget
@allure.epic('Patch/api/v1/personal_budget/{personal_budget_id}/ - Редактирование персонального бюджета - '
             'проверка поля transaction_type')
class TestPatchPersonalBudgetTransactionType:

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
            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, Variables.transaction_type, Variables.category_id, Variables.subcategory_id,
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля transaction_type"""
            data = Checking.get_data(result_patch)
            assert data['data']['transaction_type'] == "Income"
        except AssertionError:
            raise AssertionError
        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('проверка поля transaction_type - Транзакция Consumption')
    def test_02(self, auth_fixture):
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
            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, "Consumption", 20, Variables.subcategory_id,
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля transaction_type"""
            data = Checking.get_data(result_patch)
            assert data['data']['transaction_type'] == "Consumption"
        except AssertionError:
            raise AssertionError
        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('проверка поля transaction_type - Транзакция Transfer between wallets')
    def test_03(self, auth_fixture):
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
            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, "Transfer between wallets", 20, Variables.subcategory_id,
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля transaction_type"""
            data = Checking.get_data(result_patch)
            assert data['data']['transaction_type'] == "Transfer between wallets"
        except AssertionError:
            raise AssertionError
        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('проверка поля transaction_type - Поле отсутствует')
    def test_04(self, auth_fixture):
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
            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget_without_transaction_type(
                personal_budget_id, 30, Variables.subcategory_id,
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 200)

        except AssertionError:
            raise AssertionError
        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('проверка поля transaction_type - Null')
    def test_05(self, auth_fixture):
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
            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, None, 30, Variables.subcategory_id,
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError
        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('проверка поля transaction_type - Несуществующий тип транзакции')
    def test_06(self, auth_fixture):
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
            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, 'None_transaction', 30, Variables.subcategory_id,
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError
        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('проверка поля transaction_type - Пустое поле')
    def test_07(self, auth_fixture):
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
            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, '', 30, Variables.subcategory_id,
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError
        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)
            