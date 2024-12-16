# import allure
# from common_methods.checking import Checking
# from common_methods.variables import AuthVariables
# from Users.methods.users_methods import UsersMethods
# from Auth.methods.auth_methods import AuthMethods
#
#
# @allure.epic('Delete/users/id Удаление пользователя')
# class TestDeleteUsers:
#
#     @allure.description('Удаление существующего пользователя')
#     def test_01(self, auth_fixture, create_users):
#         """Создание пользователя"""
#         user_id = create_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Удаление пользователя"""
#         result_delete = UsersMethods.delete_user(user_id, access_token)
#         Checking.check_statuscode(result_delete, 204)
#
#         """Получение информации об удаленном пользователе"""
#         result_get = UsersMethods.get_user_by_id(user_id, access_token)
#         Checking.check_statuscode(result_get, 404)
#
#     @allure.description('Удаление пользователя обычным юзером')
#     def test_02(self, auth_fixture, create_and_delete_users):
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
#         """Удаление пользователя"""
#         result_delete = UsersMethods.delete_user(user_id, access_token)
#         Checking.check_statuscode(result_delete, 403)
#
#     @allure.description('user id - Несуществующее значение')
#     def test_03(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Удаление пользователя"""
#         result_delete = UsersMethods.delete_user(AuthVariables.user_id_not_exist, access_token)
#         Checking.check_statuscode(result_delete, 404)
#
#         """Получение информации об удаленном пользователе"""
#         result_get = UsersMethods.get_user_by_id(AuthVariables.user_id_not_exist, access_token)
#         Checking.check_statuscode(result_get, 404)
#
#     @allure.description('user id - Поле отсутсвует')
#     def test_04(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Удаление пользователя"""
#         result_delete = UsersMethods.delete_user_without_user_id(access_token)
#         Checking.check_statuscode(result_delete, 404)
#
#     @allure.description('user id - Пустое поле')
#     def test_05(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Удаление пользователя"""
#         result_delete = UsersMethods.delete_user('', access_token)
#         Checking.check_statuscode(result_delete, 404)
#
#     @allure.description('user id - Null')
#     def test_06(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Удаление пользователя"""
#         result_delete = UsersMethods.delete_user('', access_token)
#         Checking.check_statuscode(result_delete, 404)
#
#
#
