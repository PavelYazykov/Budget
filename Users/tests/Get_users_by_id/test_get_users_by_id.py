# import allure
# from common_methods.checking import Checking
# from common_methods.variables import CommonVariables, AuthVariables
# from Users.methods.users_methods import UsersMethods
# from Users.methods.user_payloads import UserResponse
# from Auth.methods.auth_methods import AuthMethods
#
#
# @allure.epic('Get/users/{user_id} Получение информации о пользователе по id')
# class TestGetUserById:
#
#     @allure.description('Получить информацию о пользователе с существующим id (superuser)')
#     def test_01(self, auth_fixture, create_and_delete_users):
#         """Создание пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Оптправка Get запроса"""
#         result = UsersMethods.get_user_by_id(user_id, access_token)
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 200)
#
#         """Проверка наличия обязательных полей"""
#         UserResponse.check_required_fields(result)
#
#     @allure.description('Получение информации о пользователе по id - Обычный пользователь')
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
#         """Запрос информации о пользователе"""
#         result_get = UsersMethods.get_user_by_id(AuthVariables.user_id_verify, access_token)
#         Checking.check_statuscode(result_get, 403)
#
#     @allure.description('Получить информацию о пользователе с несуществующим id (superuser)')
#     def test_03(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Оптправка Get запроса"""
#         result = UsersMethods.get_user_by_id(AuthVariables.user_id_not_exist, access_token)
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 404)
#
#     @allure.description('Получить информацию о пользователе  - Поле id отсутствует')
#     def test_04(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Оптправка Get запроса"""
#         result = UsersMethods.get_user_by_id_without_id(access_token)
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 404)
#
#     @allure.description('Получить информацию о пользователе с полем id = Null')
#     def test_05(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Оптправка Get запроса"""
#         result = UsersMethods.get_user_by_id('null', access_token)
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 404)
#
