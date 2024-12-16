# import allure
# from common_methods.checking import Checking
# from common_methods.variables import AuthVariables
# from Users.methods.users_methods import UsersMethods
# from Users.methods.user_payloads import UserResponse
#
#
# @allure.epic('Patch/users/id Изменение информации текущий пользователь Проверка поля phone')
# class TestPatchUsersByIdPhone:
#
#     @allure.description('phone - 11 символов')
#     def test_01(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email(
#             AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 200)
#
#         """Проверка наличия обязательных полей"""
#         UserResponse.check_required_fields(result)
#
#         """Проверка значения поля middlename"""
#         data = Checking.get_data(result)
#         assert data['phone_number'] == AuthVariables.phone_for_create_user
#
#     @allure.description('phone - Null')
#     def test_02(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email(
#             AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, None, AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 200)
#
#         """Проверка наличия обязательных полей"""
#         UserResponse.check_required_fields(result)
#
#     @allure.description('phone - 10 символов')
#     def test_03(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email(
#             AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, '8000000000', AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#     @allure.description('phone - 12 символов')
#     def test_04(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email(
#             AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, '800000000000', AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#     @allure.description('phone - Буквы')
#     def test_05(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email(
#             AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, 'qqqqqqqqqqq', AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#     @allure.description('phone - Спецсимволы')
#     def test_06(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email(
#             AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, '@#$%^^&@@@#', AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#     @allure.description('phone - Поле отсутствует')
#     def test_07(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 200)
#
#         """Проверка наличия обязательных полей"""
#         UserResponse.check_required_fields(result)
#
#     @allure.description('phone - Пустое поле')
#     def test_08(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email(
#             AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, '', AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#     @allure.description('phone - Неверный тип данных (integer)')
#     def test_09(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email(
#             AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, 89260000000, AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
