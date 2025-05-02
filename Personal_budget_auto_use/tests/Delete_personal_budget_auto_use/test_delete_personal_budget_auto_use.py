import allure

from common_methods.checking import Checking
from Personal_budget_auto_use.methods.personal_budget_auto_use_methods import PersonalBudgetAutoUseMethods
from Personal_budget_auto_use.methods.payloads_variables import Variables


@allure.epic('Delete/api/v1/personal_budget_auto_use/{personal_budget_auto_use_id}/ - Удаление регулярного бюджета')
class TestDeleteAutoUse:

    @allure.description('Удаление существующего регулярного бюджета')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание ежемесячного объекта бюджета"""
        result_create = PersonalBudgetAutoUseMethods.create_personal_budget_auto_use(
            Variables.transaction_type, Variables.category_id, Variables.subcategory_id, Variables.amount,
            Variables.date_reminder, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        personal_budget_auto_use_id = data['data']['id']

        """Удаление бюджета"""
        result_delete = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
            personal_budget_auto_use_id, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 204)

        """Проверка удаления"""
        result_delete = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
            personal_budget_auto_use_id, access_token
        )
        Checking.check_statuscode(result_delete, 404)

    @allure.description('Удаление несуществующего регулярного бюджета')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление бюджета"""
        result_delete = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
            123, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 404)

    @allure.description('Удаление регулярного бюджета - Значение id = 0')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление бюджета"""
        result_delete = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
            0, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление регулярного бюджета - Отрицательное значение')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление бюджета"""
        result_delete = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
            -5, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление регулярного бюджета - Пустое поле ""')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление бюджета"""
        result_delete = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
            "", access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 404)

    @allure.description('Удаление регулярного бюджета - Поле отсутствует')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление бюджета"""
        result_delete = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use_without_id(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 405)

    @allure.description('Удаление регулярного бюджета - Null')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление бюджета"""
        result_delete = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
            None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление регулярного бюджета - Вещественное число')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление бюджета"""
        result_delete = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
            1.1, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)
