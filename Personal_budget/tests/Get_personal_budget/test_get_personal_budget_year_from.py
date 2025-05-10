import allure
import pytest

from common_methods.checking import Checking
from Personal_budget.methods.personal_budget_methods import PersonalBudgetMethods
from Personal_budget.methods.payloads import Variables, Payloads


@pytest.mark.personal_budget
@allure.epic('Get/api/v1/personal_budget/ - Запрос всех объектов бюджета - Проверка поля year_from')
class TestGetPersonalBudgetYearFrom:

    @allure.description('Проверка поля year_from - Год = 2024')
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
            """Запрос на отображение персональных бюджетов"""
            result_get = PersonalBudgetMethods.get_personal_budget_with_params(
                '?month_from=1&year_from=2024&month_to=12&year_to=2026', access_token
            )
            Checking.check_statuscode(result_get, 200)

            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields_get(result_get, Payloads.get_payloads)

        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля year_from - Год = 2100')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета"""
        result_create = PersonalBudgetMethods.create_personal_budget(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, 2100, Variables.date_reminder, Variables.title, Variables.have_to_remind,
            Variables.remind_in_days, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_id = data['data']['id']

        try:
            """Запрос на отображение персональных бюджетов"""
            result_get = PersonalBudgetMethods.get_personal_budget_with_params(
                '?month_from=1&year_from=2100&month_to=12&year_to=2100', access_token
            )
            Checking.check_statuscode(result_get, 200)

            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields_get(result_get, Payloads.get_payloads)

        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля year_from - Поле отсутствует')
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
            """Запрос на отображение персональных бюджетов"""
            result_get = PersonalBudgetMethods.get_personal_budget_with_params(
                '?month_from=1&month_to=12&year_to=2026', access_token
            )
            Checking.check_statuscode(result_get, 200)

            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields_get(result_get, Payloads.get_payloads)

        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля year_from - Год = 2019')
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
            """Запрос на отображение персональных бюджетов"""
            result_get = PersonalBudgetMethods.get_personal_budget_with_params(
                '?month_from=1&year_from=2019&month_to=12&year_to=2100', access_token
            )
            Checking.check_statuscode(result_get, 422)

        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля year_from - Год = 2101')
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
            """Запрос на отображение персональных бюджетов"""
            result_get = PersonalBudgetMethods.get_personal_budget_with_params(
                '?month_from=1&year_from=2101&month_to=12&year_to=2100', access_token
            )
            Checking.check_statuscode(result_get, 422)

        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля year_from - Год в формате гг')
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
            """Запрос на отображение персональных бюджетов"""
            result_get = PersonalBudgetMethods.get_personal_budget_with_params(
                '?month_from=1&year_from=25&month_to=12&year_to=2100', access_token
            )
            Checking.check_statuscode(result_get, 422)

        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля year_from - Отрицательное значение')
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
            """Запрос на отображение персональных бюджетов"""
            result_get = PersonalBudgetMethods.get_personal_budget_with_params(
                '?month_from=1&year_from=-2026&month_to=12&year_to=2100', access_token
            )
            Checking.check_statuscode(result_get, 422)

        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля year_from - Пустое поле')
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
            """Запрос на отображение персональных бюджетов"""
            result_get = PersonalBudgetMethods.get_personal_budget_with_params(
                '?month_from=1&year_from=""&month_to=12&year_to=2100', access_token
            )
            Checking.check_statuscode(result_get, 422)

        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля year_from - Null')
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

        try:
            """Запрос на отображение персональных бюджетов"""
            result_get = PersonalBudgetMethods.get_personal_budget_with_params(
                '?month_from=1&year_from=null&month_to=12&year_to=2100', access_token
            )
            Checking.check_statuscode(result_get, 422)

        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля year_from - Недопустимые символы')
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

        try:
            """Запрос на отображение персональных бюджетов"""
            result_get = PersonalBudgetMethods.get_personal_budget_with_params(
                '?month_from=1&year_from=@#$%&month_to=12&year_to=2100', access_token
            )
            Checking.check_statuscode(result_get, 422)

        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)