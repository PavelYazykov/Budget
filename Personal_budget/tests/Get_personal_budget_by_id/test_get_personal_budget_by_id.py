import allure
import pytest

from common_methods.checking import Checking
from Personal_budget.methods.personal_budget_methods import PersonalBudgetMethods
from Personal_budget.methods.payloads import Variables, Payloads


@pytest.mark.personal_budget
@allure.epic('Get/api/v1/personal_budget/{personal_budget_id}/ - Запрос объекта бюджета по id')
class TestGetPersonalBudgetById:

    @allure.description('Получение бюджета с существующим id')
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
            """Запрос персонального бюджета"""
            result_get = PersonalBudgetMethods.get_personal_budget_by_id(
                personal_budget_id, access_token
            )
            Checking.check_statuscode(result_get, 200)

            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields(result_get, Payloads.get_payloads)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)

    @allure.description('Получение бюджета с несуществующим id')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос персонального бюджета"""
        result_get = PersonalBudgetMethods.get_personal_budget_by_id(1000, access_token)
        Checking.check_statuscode(result_get, 404)

    @allure.description('Получение бюджета с Отрицательное значением id')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос персонального бюджета"""
        result_get = PersonalBudgetMethods.get_personal_budget_by_id(-5, access_token)
        Checking.check_statuscode(result_get, 422)

    @allure.description('Получение бюджета со значением id = Пустое поле')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос персонального бюджета"""
        result_get = PersonalBudgetMethods.get_personal_budget_by_id('', access_token)
        Checking.check_statuscode(result_get, 404)

    @allure.description('Получение бюджета - Поле id = Null')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос персонального бюджета"""
        result_get = PersonalBudgetMethods.get_personal_budget_by_id(None, access_token)
        Checking.check_statuscode(result_get, 422)

    @allure.description('Получение бюджета - Поле id - Недопустимые символы')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос персонального бюджета"""
        result_get = PersonalBudgetMethods.get_personal_budget_by_id('string', access_token)
        Checking.check_statuscode(result_get, 422)

    @allure.description('Получение бюджета - Поле id - Вещественное число')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос персонального бюджета"""
        result_get = PersonalBudgetMethods.get_personal_budget_by_id(6.6, access_token)
        Checking.check_statuscode(result_get, 422)

