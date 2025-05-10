import allure
import pytest

from common_methods.checking import Checking
from Personal_budget.methods.personal_budget_methods import PersonalBudgetMethods
from Personal_budget.methods.payloads import Variables


@pytest.mark.personal_budget
@allure.epic('Patch/api/v1/personal_budget/{personal_budget_id}/ - Редактирование персонального бюджета - '
             'проверка поля amount')
class TestPatchPersonalBudgetAmount:

    @allure.description('Проверка поля amount - Целое число')
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

        try:
            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, Variables.transaction_type, Variables.category_id, Variables.subcategory_id,
                10, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля amount"""
            data = Checking.get_data(result_patch)
            assert data['data']['amount'] == '10.00'
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля amount - Вещественное число')
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
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, Variables.transaction_type, Variables.category_id, Variables.subcategory_id,
                10.10, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля amount"""
            data = Checking.get_data(result_patch)
            assert data['data']['amount'] == '10.10'
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля amount - Значение 9999999999.99')
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
        print(personal_budget_id)

        try:
            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, Variables.transaction_type, Variables.category_id, Variables.subcategory_id,
                9999999999.99, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля amount"""
            data = Checking.get_data(result_patch)
            assert data['data']['amount'] == '9999999999.99'
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля amount - Поле отсутствует')
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
        print(personal_budget_id)

        try:
            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget_without_amount(
                personal_budget_id, Variables.transaction_type, Variables.category_id, Variables.subcategory_id,
                Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля amount"""
            data = Checking.get_data(result_patch)
            assert data['data']['amount'] == '10.00'
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля amount - Значение Null')
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
        print(personal_budget_id)

        try:
            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, Variables.transaction_type, Variables.category_id, Variables.subcategory_id,
                None, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля amount - Значение 9999999999.101')
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
        print(personal_budget_id)

        try:
            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, Variables.transaction_type, Variables.category_id, Variables.subcategory_id,
                9999999999.101, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля amount - Значение 10000000000')
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
        print(personal_budget_id)

        try:
            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, Variables.transaction_type, Variables.category_id, Variables.subcategory_id,
                10000000000, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля amount - Значение 0')
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
        print(personal_budget_id)

        try:
            """Запрос на изменение персонального бюджета"""
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, Variables.transaction_type, Variables.category_id, Variables.subcategory_id,
                0, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля amount - Отрицательное значение')
    def test_09(self, auth_fixture):
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
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, Variables.transaction_type, Variables.category_id, Variables.subcategory_id,
                -5, Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля amount - Пустое поле')
    def test_10(self, auth_fixture):
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
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, Variables.transaction_type, Variables.category_id, Variables.subcategory_id,
                "", Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля amount - Недопустимые символы')
    def test_11(self, auth_fixture):
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
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, Variables.transaction_type, Variables.category_id, Variables.subcategory_id,
                "", Variables.month, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

