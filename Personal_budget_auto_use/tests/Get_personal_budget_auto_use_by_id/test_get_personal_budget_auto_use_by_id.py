import allure
import pytest

from common_methods.checking import Checking
from Personal_budget_auto_use.methods.personal_budget_auto_use_methods import PersonalBudgetAutoUseMethods
from Personal_budget_auto_use.methods.payloads_variables import Variables, Payloads


@pytest.mark.Personal_budget_auto_use
@allure.epic('Get/api/v1/personal_budget_auto_use/{personal_budget_auto_use_id}/ - Запрос ежемесячных объектов бюджета'
             'по id')
class TestGetAutoUseById:

    @allure.description('Запрос регулярного бюджета с существующим id')
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
        try:
            """Запрос регулярного бюджета"""
            result_get = PersonalBudgetAutoUseMethods.get_personal_budget_auto_use_by_id(
                personal_budget_auto_use_id, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка наличия обязательных полей"""
            Payloads.check_req_fields_post(result_create, Payloads.post_payloads)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            if personal_budget_auto_use_id is not None:
                delete_result = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
                    personal_budget_auto_use_id, access_token
                )
                Checking.check_statuscode(delete_result, 204)

    @allure.description('Запрос регулярного бюджета с несуществующим id')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос регулярного бюджета"""
        result_get = PersonalBudgetAutoUseMethods.get_personal_budget_auto_use_by_id(
            123, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 404)

    @allure.description('Запрос регулярного бюджета с отрицательным id')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос регулярного бюджета"""
        result_get = PersonalBudgetAutoUseMethods.get_personal_budget_auto_use_by_id(
            -123, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Запрос регулярного бюджета с id = пустое поле')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос регулярного бюджета"""
        result_get = PersonalBudgetAutoUseMethods.get_personal_budget_auto_use_by_id(
            "", access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 404)

    @allure.description('Запрос регулярного бюджета с id = Null')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос регулярного бюджета"""
        result_get = PersonalBudgetAutoUseMethods.get_personal_budget_auto_use_by_id(
            None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Запрос регулярного бюджета с id = Недопустимые символы')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос регулярного бюджета"""
        result_get = PersonalBudgetAutoUseMethods.get_personal_budget_auto_use_by_id(
            'string', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Запрос регулярного бюджета с id = Вещественное число')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос регулярного бюджета"""
        result_get = PersonalBudgetAutoUseMethods.get_personal_budget_auto_use_by_id(
            1.1, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
