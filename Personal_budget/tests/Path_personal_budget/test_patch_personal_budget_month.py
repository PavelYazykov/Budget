import allure

from common_methods.checking import Checking
from Personal_budget.methods.personal_budget_methods import PersonalBudgetMethods
from Personal_budget.methods.payloads import Variables


@allure.epic('Patch/api/v1/personal_budget/{personal_budget_id}/ - Редактирование персонального бюджета - '
             'проверка поля month')
class TestPatchPersonalBudgetMonth:

    @allure.description('Проверка поля month - Месяц = 1')
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
                Variables.amount, 1, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля month"""
            data = Checking.get_data(result_patch)
            assert data['data']['month'] == 1
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля month - Месяц = 12')
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
                Variables.amount, 12, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля month"""
            data = Checking.get_data(result_patch)
            assert data['data']['month'] == 12
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля month - Поле отсутствует')
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
            result_patch = PersonalBudgetMethods.change_personal_budget_without_month(
                personal_budget_id, Variables.transaction_type, Variables.category_id, Variables.subcategory_id,
                Variables.amount, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля month"""
            data = Checking.get_data(result_patch)
            assert data['data']['month'] == 12
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля month - Вещественное число -> 11.0')
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
            result_patch = PersonalBudgetMethods.change_personal_budget(
                personal_budget_id, Variables.transaction_type, Variables.category_id, Variables.subcategory_id,
                Variables.amount, 12.0, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля month"""
            data = Checking.get_data(result_patch)
            assert data['data']['month'] == 12
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля month - Месяц = 0')
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
                Variables.amount, 0, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля month - Месяц = 13')
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
                Variables.amount, 13, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля month - Отрицательное значение')
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
                Variables.amount, -11, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля month - Пустое поле')
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
                Variables.amount, "", Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля month - Null')
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
                Variables.amount, None, Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Проверка поля month - Недопустимые символы')
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
                Variables.amount, "string", Variables.year, access_token
            )
            Checking.check_statuscode(result_patch, 422)
        finally:
            if personal_budget_id is not None:
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)


