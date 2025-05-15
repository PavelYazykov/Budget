import allure
import pytest

from common_methods.checking import Checking
from Personal_budget.methods.personal_budget_methods import PersonalBudgetMethods
from Personal_budget.methods.payloads import Variables, Payloads


@pytest.mark.Personal_budget
@allure.epic('Patch/api/v1/personal_budget/{personal_budget_id}/ - Редактирование персонального бюджета - '
             'проверка поля category_id')
class TestPatchPersonalBudgetCategoryId:

    @allure.description('Проверка поля category_id - Транзакция Income')
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
            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, Variables.transaction_type, 29, Variables.subcategory_id,
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля category_id"""
            data = Checking.get_data(result_patch)
            assert data['data']['category_id'] == 29
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля category_id - Поле отсутствует')
    def test_02(self, auth_fixture):
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
            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget_without_category_id(
                personal_budget_id, Variables.transaction_type, Variables.subcategory_id,
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля category_id"""
            Payloads.check_required_fields(result_patch, Payloads.post_payloads)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля category_id - Null')
    def test_03(self, auth_fixture):
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
            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, Variables.transaction_type, None, Variables.subcategory_id,
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля category_id - Несуществующий id')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на изменение персонального бюджета"""
        result_patch = PersonalBudgetMethods.change_personal_budget(
            404, Variables.transaction_type, None, Variables.subcategory_id,
            Variables.amount, Variables.month, Variables.year, access_token
        )
        Checking.check_statuscode(result_patch, 404)

    @allure.description('Проверка поля category_id - Отрицательное значение')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на изменение персонального бюджета"""
        result_patch = PersonalBudgetMethods.change_personal_budget(
            -404, Variables.transaction_type, None, Variables.subcategory_id,
            Variables.amount, Variables.month, Variables.year, access_token
        )
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Проверка поля category_id - Пустое поле')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на изменение персонального бюджета"""
        result_patch = PersonalBudgetMethods.change_personal_budget(
            "", Variables.transaction_type, None, Variables.subcategory_id,
            Variables.amount, Variables.month, Variables.year, access_token
        )
        Checking.check_statuscode(result_patch, 404)

    @allure.description('Проверка поля category_id - Неверный тип данных string')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на изменение персонального бюджета"""
        result_patch = PersonalBudgetMethods.change_personal_budget(
            "string", Variables.transaction_type, None, Variables.subcategory_id,
            Variables.amount, Variables.month, Variables.year, access_token
        )
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Проверка поля category_id - Вещественное число')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на изменение персонального бюджета"""
        result_patch = PersonalBudgetMethods.change_personal_budget(
            1.1, Variables.transaction_type, None, Variables.subcategory_id,
            Variables.amount, Variables.month, Variables.year, access_token
        )
        Checking.check_statuscode(result_patch, 422)
