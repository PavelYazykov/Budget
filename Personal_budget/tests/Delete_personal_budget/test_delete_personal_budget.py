import allure

from common_methods.checking import Checking
from Personal_budget.methods.personal_budget_methods import PersonalBudgetMethods
from Personal_budget.methods.payloads import Variables


@allure.epic('Delete/api/v1/personal_budget/{personal_budget_id}/ - Удаление персонального бюджета')
class TestDeletePersonalBudget:

    @allure.description('Удаление существующего бюджета')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание персонального бюджета 1"""
        result_create = PersonalBudgetMethods.create_personal_budget_without_regular_outcome(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.month, Variables.year, access_token
        )

        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_id = data['data']['id']

        """Удаление персонального бюджета"""
        result_delete = PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 204)

        """Запрос информации об удаленном персональном бюджете"""
        result_get = PersonalBudgetMethods.get_personal_budget_by_id(personal_budget_id, access_token)
        Checking.check_statuscode(result_get, 404)

    @allure.description('Удаление несуществующего бюджета')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление персонального бюджета"""
        result_delete = PersonalBudgetMethods.delete_personal_budget(1000, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 404)

    @allure.description('Удаление персонального бюджета - Значение id = 0')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление персонального бюджета"""
        result_delete = PersonalBudgetMethods.delete_personal_budget(0, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление персонального бюджета - id - Отрицательное значение')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление персонального бюджета"""
        result_delete = PersonalBudgetMethods.delete_personal_budget(-5, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление персонального бюджета - Пустое поле')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление персонального бюджета"""
        result_delete = PersonalBudgetMethods.delete_personal_budget('', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 404)

    @allure.description('Удаление персонального бюджета - id - Поле отсутствует')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление персонального бюджета"""
        result_delete = PersonalBudgetMethods.delete_personal_budget_without_budget_id(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 405)

    @allure.description('Удаление персонального бюджета - id = Null')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление персонального бюджета"""
        result_delete = PersonalBudgetMethods.delete_personal_budget(None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление персонального бюджета - id - Вещественное число')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление персонального бюджета"""
        result_delete = PersonalBudgetMethods.delete_personal_budget(None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)
