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
from Subcategory.methods.subcategory_methods import SubcategoryMethods


@pytest.mark.Personal_budget
@allure.epic('Patch/api/v1/personal_budget/{personal_budget_id}/ - Редактирование единоразового и регулярного бюджета -'
             'проверка поля subcategory id')
class TestPatchPersonalBudgetSubcategoryId:

    @allure.description('проверка поля subcategory id - Существующий id')
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

            """Создание подкатегории"""
            create_subcategory = SubcategoryMethods.create_subcategory(
                30, 'Pavel', access_token
            )
            Checking.check_statuscode(create_subcategory, 201)
            data = Checking.get_data(create_subcategory)
            subcategory_id = data['data']['id']

            """Создание второй подкатегории"""
            create_subcategory_2 = SubcategoryMethods.create_subcategory(
                30, 'Pavel_2', access_token
            )
            Checking.check_statuscode(create_subcategory_2, 201)
            data_2 = Checking.get_data(create_subcategory_2)
            subcategory_id_2 = data_2['data']['id']

            """Cоздание персонального и регулярного объектов бюджета"""
            PersonalBudgetMethods.create_pb_and_pb_auto_use(
                30, user_id, 'IN', 12, 2026, subcategory_id,
                '12345', '54321', 10, '2026-01-12'
            )

            """Запрос на редактирование регулярного бюджета"""
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use(
                '54321', Variables.transaction_type, Variables.category_id,
                subcategory_id_2, 1000, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            result_get = PersonalBudgetAutoUseMethods.get_personal_budget_auto_use_by_id(
                '12345', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка значения поля subcategory_id"""
            data = Checking.get_data(result_get)
            assert data['data']['subcategory_id'] == subcategory_id_2
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('проверка поля subcategory id - Поле отсутствует')
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
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use_without_subcategory_id(
                '54321', Variables.transaction_type, Variables.category_id,
                1000, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            result_get = PersonalBudgetAutoUseMethods.get_personal_budget_auto_use_by_id(
                '12345', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка значения поля subcategory_id"""
            data = Checking.get_data(result_get)
            assert data['data']['subcategory_id'] is None
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('проверка поля subcategory id - Null')
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

            """Создание подкатегории"""
            create_subcategory = SubcategoryMethods.create_subcategory(
                30, 'Pavel', access_token
            )
            Checking.check_statuscode(create_subcategory, 201)
            data = Checking.get_data(create_subcategory)
            subcategory_id = data['data']['id']

            """Cоздание персонального и регулярного объектов бюджета"""
            PersonalBudgetMethods.create_pb_and_pb_auto_use(
                30, user_id, 'IN', 12, 2026, subcategory_id,
                '12345', '54321', 10, '2026-01-12'
            )

            """Запрос на редактирование регулярного бюджета"""
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use(
                '54321', Variables.transaction_type, Variables.category_id, None,
                1000, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            result_get = PersonalBudgetAutoUseMethods.get_personal_budget_auto_use_by_id(
                '12345', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка значения поля subcategory_id"""
            data = Checking.get_data(result_get)
            assert data['data']['subcategory_id'] is None
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('проверка поля subcategory id - Несуществующий id')
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
            result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use(
                '54321', Variables.transaction_type, Variables.category_id, 555,
                1000, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 404)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('проверка поля subcategory id - Отрицательное значение')
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
                '54321', Variables.transaction_type, Variables.category_id, -20,
                1000, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('проверка поля subcategory id - Пустое поле')
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
                '54321', Variables.transaction_type, Variables.category_id, '',
                1000, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('проверка поля subcategory id - Неверный тип данных string')
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
                '54321', Variables.transaction_type, Variables.category_id, 'string',
                1000, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

    @allure.description('проверка поля subcategory id - Вещественное число')
    def test_08(self):
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
                '54321', Variables.transaction_type, Variables.category_id, 1.1,
                1000, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)


