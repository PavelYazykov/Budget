import time
import allure
from Auth.methods.auth_methods import AuthMethods
from common_methods.auth import Auth
from common_methods.checking import Checking
from Personal_budget.methods.personal_budget_methods import PersonalBudgetMethods
from Personal_budget.methods.payloads import Variables
from Personal_budget_auto_use.methods.personal_budget_auto_use_methods import PersonalBudgetAutoUseMethods
from common_methods.variables import AuthVariables


@allure.epic('Patch/api/v1/personal_budget/{personal_budget_id}/ - Редактирование единоразового и регулярного бюджета -'
             'Проверка поля personal_budget_id')
class TestPatchPersonalBudgePersonalBudgetId:

    @allure.description('Проверка поля personal_budget_id - С существующим id')
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
                30, user_id, 'IN', 12, 2026, None,
                '12345', '54321', 10, '2026-01-12'
            )

            """Запрос на редактирование регулярного бюджета"""
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use(
                '54321', Variables.transaction_type, Variables.category_id,
                Variables.subcategory_id, 1000, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            result_get = PersonalBudgetAutoUseMethods.get_personal_budget_auto_use_by_id(
                '12345', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка значения поля amount"""
            data = Checking.get_data(result_get)
            assert data['data']['amount'] == '1000.00'
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля personal_budget_id - С несуществующим id')
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

            """Запрос на редактирование регулярного бюджета"""
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use(
                '543200', Variables.transaction_type, Variables.category_id,
                Variables.subcategory_id, 1000, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 404)
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля personal_budget_id - С oтрицательное значение')
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

            """Запрос на редактирование регулярного бюджета"""
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use(
                -532, Variables.transaction_type, Variables.category_id,
                Variables.subcategory_id, 1000, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля personal_budget_id - Пустое поле')
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

            """Запрос на редактирование регулярного бюджета"""
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use(
                '', Variables.transaction_type, Variables.category_id,
                Variables.subcategory_id, 1000, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 404)
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля personal_budget_id - Null')
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

            """Запрос на редактирование регулярного бюджета"""
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use(
                None, Variables.transaction_type, Variables.category_id,
                Variables.subcategory_id, 1000, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля personal_budget_id - Недопустимые символы')
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

            """Запрос на редактирование регулярного бюджета"""
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use(
                'string', Variables.transaction_type, Variables.category_id,
                Variables.subcategory_id, 1000, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля personal_budget_id - Вещественное число')
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

            """Запрос на редактирование регулярного бюджета"""
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use(
                3.3, Variables.transaction_type, Variables.category_id,
                Variables.subcategory_id, 1000, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)


