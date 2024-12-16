# import allure
# from common_methods.checking import Checking
# from common_methods.variables import AuthVariables
# from Users.methods.users_methods import UsersMethods
#
#
# @allure.epic('Patch/users/id Изменение информации текущий пользователь Проверка поля id')
# class TestPatchUsersByIdFieldId:
#
#     @allure.description('Несуществующий id')
#     def test_01(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.date_of_birth, AuthVariables.user_id_not_exist,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 404)
#
#     @allure.description('Поле id отсутствует')
#     def test_02(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone_user_id(
#             AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.date_of_birth,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 404)
#
#     @allure.description('id - Пустое поле')
#     def test_03(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.date_of_birth, '',
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 404)
#
#     @allure.description('id - Null')
#     def test_04(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.date_of_birth, 'null',
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 404)
#
