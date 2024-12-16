# import allure
# from common_methods.checking import Checking
# from common_methods.variables import CommonVariables, AuthVariables
# from Users.methods.users_methods import UsersMethods
# from Users.methods.user_payloads import UserResponse
# from Auth.methods.auth_methods import AuthMethods
#
#
# @allure.epic('Patch/users/id Изменение информации текущий пользователь Общие проверки')
# class TestPatchUsersByIdCommon:
#
#     @allure.description('Изменение информации о пользователе с валидными данными')
#     def test_01(self, auth_fixture):
#         """Создание пользователя"""
#         result = AuthMethods.registration(
#             'my_email@mail.ru', 'Ohranatruda@11', 'Иванов', 'Иван',
#             'Иванович', '80000000000', '2000-10-10'
#         )
#         data = Checking.get_data(result)
#         user_id = data['id']
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id(
#             AuthVariables.email_for_create_user, AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 200)
#         try:
#             """Проверка наличия обязательных полей"""
#             UserResponse.check_required_fields(result)
#
#             """Проверка значений обязательных полей"""
#             UserResponse.check_required_fields_value(
#                 result, AuthVariables.email_for_create_user, AuthVariables.last_name, AuthVariables.first_name,
#                 AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
#             )
#         except AssertionError:
#             raise AssertionError
#         finally:
#             """Удаление пользователя"""
#             UsersMethods.delete_users(user_id)
#
#     @allure.description('Изменение информации  с валидными данными (Обычный пользователь)')
#     def test_02(self, create_and_delete_users):
#         """Создание пользователя"""
#         user_id = create_and_delete_users
#
#         """Верификация пользователя"""
#         result = AuthMethods.request_verify_code(
#             'email', user_id
#         )
#         Checking.check_statuscode(result, 200)
#         code = AuthMethods.get_verify_code(result)
#         result_check = AuthMethods.verify(user_id, 'email', code)
#         Checking.check_statuscode(result_check, 200)
#
#         """Авторизация"""
#         result_auth = AuthMethods.login('010101', 'username=my_email@mail.ru&password=Ohranatruda@11')
#         Checking.check_statuscode(result_auth, 200)
#         data = Checking.get_data(result_auth)
#         access_token = data['access_token']
#
#         """Запрос на изменение информации"""
#         result_change = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.date_of_birth,
#             AuthVariables.user_id_verify, access_token
#         )
#
#         """проверка статус кода"""
#         Checking.check_statuscode(result_change, 403)
#
