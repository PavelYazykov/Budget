import time

import allure
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.auth import Auth
from common_methods.checking import Checking
from Personal_budget.methods.personal_budget_methods import PersonalBudgetMethods
from Personal_budget.methods.payloads import Variables
from Personal_budget_auto_use.methods.personal_budget_auto_use_methods import PersonalBudgetAutoUseMethods
from common_methods.variables import AuthVariables


@pytest.mark.personal_budget
@allure.epic('Patch/api/v1/personal_budget/{personal_budget_id}/ - Редактирование единоразового и регулярного бюджета -'
             'проверка поля transaction_type')
class TestPatchPersonalBudgeTransactionType:

    @allure.description('проверка поля transaction_type - Транзакция Income')
    def test_01(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Авторизация пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Cоздание персонального и регулярного объектов бюджета"""
            PersonalBudgetMethods.create_pb_and_pb_auto_use(
                20, user_id, 'OUT', 12, 2026, None,
                '12345', '54321', 10, '2026-01-12'
            )

            """Запрос на редактирование регулярного бюджета"""
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use(
                '54321', Variables.transaction_type, Variables.category_id,
                Variables.subcategory_id, 10, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            result_get = PersonalBudgetAutoUseMethods.get_personal_budget_auto_use_by_id(
                '12345', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка значения поля transaction_type"""
            data = Checking.get_data(result_get)
            assert data['data']['transaction_type'] == 'Income'
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('проверка поля transaction_type - Транзакция Consumption')
    def test_02(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Авторизация пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Cоздание персонального и регулярного объектов бюджета"""
            PersonalBudgetMethods.create_pb_and_pb_auto_use(
                30, user_id, 'IN', 12, 2026, None,
                '12345', '54321', 10, '2026-01-12'
            )

            """Запрос на редактирование регулярного бюджета"""
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use(
                '54321', 'Consumption', 20,
                Variables.subcategory_id, 10, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            result_get = PersonalBudgetAutoUseMethods.get_personal_budget_auto_use_by_id(
                '12345', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка значения поля transaction_type"""
            data = Checking.get_data(result_get)
            assert data['data']['transaction_type'] == 'Consumption'
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('проверка поля transaction_type - Транзакция Transfer between wallets')
    def test_03(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Авторизация пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Cоздание персонального и регулярного объектов бюджета"""
            PersonalBudgetMethods.create_pb_and_pb_auto_use(
                30, user_id, 'IN', 12, 2026, None,
                '12345', '54321', 10, '2026-01-12'
            )

            """Запрос на редактирование регулярного бюджета"""
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use(
                '54321', 'Transfer between wallets', 30,
                Variables.subcategory_id, 10, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('проверка поля transaction_type - Поле отсутствует')
    def test_04(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Авторизация пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Cоздание персонального и регулярного объектов бюджета"""
            PersonalBudgetMethods.create_pb_and_pb_auto_use(
                30, user_id, 'IN', 12, 2026, None,
                '12345', '54321', 10, '2026-01-12'
            )

            """Запрос на редактирование регулярного бюджета"""
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use_without_transaction_type(
                '54321', 30,
                Variables.subcategory_id, 10, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            result_get = PersonalBudgetAutoUseMethods.get_personal_budget_auto_use_by_id(
                '12345', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка значения поля transaction_type"""
            data = Checking.get_data(result_get)
            assert data['data']['transaction_type'] == 'Income'
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('проверка поля transaction_type - Null')
    def test_05(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Авторизация пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Cоздание персонального и регулярного объектов бюджета"""
            PersonalBudgetMethods.create_pb_and_pb_auto_use(
                30, user_id, 'IN', 12, 2026, None,
                '12345', '54321', 10, '2026-01-12'
            )

            """Запрос на редактирование регулярного бюджета"""
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use(
                '54321', None, 30,
                Variables.subcategory_id, 10, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('проверка поля transaction_type - Несуществующий тип транзакции')
    def test_06(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Авторизация пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Cоздание персонального и регулярного объектов бюджета"""
            PersonalBudgetMethods.create_pb_and_pb_auto_use(
                30, user_id, 'IN', 12, 2026, None,
                '12345', '54321', 10, '2026-01-12'
            )

            """Запрос на редактирование регулярного бюджета"""
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use(
                '54321', 'Transaction', 30,
                Variables.subcategory_id, 10, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('проверка поля transaction_type - Пустое поле')
    def test_07(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        data, user_id = AuthMethods.get_id(result_create_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Авторизация пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Cоздание персонального и регулярного объектов бюджета"""
            PersonalBudgetMethods.create_pb_and_pb_auto_use(
                30, user_id, 'IN', 12, 2026, None,
                '12345', '54321', 10, '2026-01-12'
            )

            """Запрос на редактирование регулярного бюджета"""
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use(
                '54321', '', 30,
                Variables.subcategory_id, 10, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)
