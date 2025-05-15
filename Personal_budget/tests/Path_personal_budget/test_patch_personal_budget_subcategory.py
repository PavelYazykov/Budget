import allure
import pytest

from common_methods.checking import Checking
from Personal_budget.methods.personal_budget_methods import PersonalBudgetMethods
from Personal_budget.methods.payloads import Variables
from Subcategory.methods.subcategory_methods import SubcategoryMethods


@pytest.mark.Personal_budget
@allure.epic('Patch/api/v1/personal_budget/{personal_budget_id}/ - Редактирование персонального бюджета - '
             'проверка поля subcategory_id')
class TestPatchPersonalBudgetSubcategoryId:

    @allure.description('Проверка поля subcategory_id - Существующий id')
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
        print(personal_budget_id)

        subcategory_id = None
        try:

            """Создание подкатегории"""
            result_subcategory = SubcategoryMethods.create_subcategory(Variables.category_id, 'Pavel_sub', access_token)
            Checking.check_statuscode(result_subcategory, 201)
            data = Checking.get_data(result_subcategory)
            subcategory_id = data['data']['id']

            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, Variables.transaction_type, Variables.category_id, subcategory_id,
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля subcategory_id"""
            data = Checking.get_data(result_patch)
            assert data['data']['subcategory_id'] == subcategory_id
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

            if personal_budget_id is not None:
                SubcategoryMethods.delete_subcategory(subcategory_id, access_token)

    @allure.description('Проверка поля subcategory_id - Поле отсутствует')
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
        print(personal_budget_id)

        try:

            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget_without_subcategory(
                personal_budget_id, Variables.transaction_type, Variables.category_id,
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 200)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля subcategory_id - Null')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_subcategory = SubcategoryMethods.create_subcategory(Variables.category_id, 'Pavel_sub', access_token)
        Checking.check_statuscode(result_subcategory, 201)
        data = Checking.get_data(result_subcategory)
        subcategory_id = data['data']['id']

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            Variables.transaction_type, Variables.category_id, subcategory_id, Variables.amount,
            Variables.month, Variables.year, Variables.date_reminder, Variables.title, Variables.have_to_remind,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_id = data['data']['id']
        print(personal_budget_id)

        try:

            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, Variables.transaction_type, Variables.category_id, Variables.subcategory_id,
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля subcategory_id"""
            data = Checking.get_data(result_patch)
            assert data['data']['subcategory_id'] is None
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

            if personal_budget_id is not None:
                SubcategoryMethods.delete_subcategory(subcategory_id, access_token)

    @allure.description('Проверка поля subcategory_id - несуществующий id')
    def test_04(self, auth_fixture):
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
                personal_budget_id, Variables.transaction_type, Variables.category_id, 404,
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 404)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля subcategory_id - Отрицательное значение')
    def test_05(self, auth_fixture):
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
                personal_budget_id, Variables.transaction_type, Variables.category_id, -404,
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля subcategory_id - Пустое поле')
    def test_06(self, auth_fixture):
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
                personal_budget_id, Variables.transaction_type, Variables.category_id, "",
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля subcategory_id - Неверный тип данных string')
    def test_07(self, auth_fixture):
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
                personal_budget_id, Variables.transaction_type, Variables.category_id, "string",
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля subcategory_id - Вещественное число')
    def test_08(self, auth_fixture):
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
                personal_budget_id, Variables.transaction_type, Variables.category_id, 1.1,
                Variables.amount, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

