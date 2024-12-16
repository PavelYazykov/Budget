# import allure
# from common_methods.checking import Checking
# from common_methods.variables import AuthVariables
# from Users.methods.users_methods import UsersMethods
# from Users.methods.user_payloads import UserResponse
#
#
# @allure.epic('Patch/users/{id} Проверка поля email')  # для тестов нужен верифицированный пользователь
# class TestPatchUsersEmailById:
#
#     @allure.description('Валидный email')
#     def test_01(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_phone(
#             AuthVariables.email_for_create_user, AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.date_of_birth, AuthVariables.user_id_verify_2, access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 200)
#         try:
#             """Проверка наличия обязательных полей"""
#             UserResponse.check_required_fields(result)
#
#             """Проверка значения поля email"""
#             data = Checking.get_data(result)
#             assert data['email'] == AuthVariables.email_for_create_user
#         except AssertionError:
#             raise AssertionError
#         finally:
#             """Изменение информации"""
#             UsersMethods.connect_db('pawel_test_1@rambler.ru', AuthVariables.user_id_verify_2)
#             print('информация о пользлвателе восстановлена')
#
#     @allure.description('email - 64 символа в локальной')
#     def test_02(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_phone(
#             'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@nowni.com',
#             AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.date_of_birth, AuthVariables.user_id_verify_2, access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 200)
#         try:
#             """Проверка наличия обязательных полей"""
#             UserResponse.check_required_fields(result)
#
#             """Проверка значения поля email"""
#             data = Checking.get_data(result)
#             assert data['email'] == 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@nowni.com'
#         except AssertionError:
#             raise AssertionError
#         finally:
#             """Изменение информации"""
#             UsersMethods.connect_db('pawel_test_1@rambler.ru', AuthVariables.user_id_verify_2)
#             print('информация о пользлвателе восстановлена')
#
#     @allure.description('email содержит спецсимволы в локальной части')
#     def test_03(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_phone(
#             'a#$%^&*q@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.date_of_birth, AuthVariables.user_id_verify_2, access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 200)
#         try:
#             """Проверка наличия обязательных полей"""
#             UserResponse.check_required_fields(result)
#
#             """Проверка значения поля email"""
#             data = Checking.get_data(result)
#             assert data['email'] == 'a#$%^&*q@mail.ru'
#         except AssertionError:
#             raise AssertionError
#         finally:
#             """Изменение информации"""
#             UsersMethods.connect_db('pawel_test_1@rambler.ru', AuthVariables.user_id_verify_2)
#             print('информация о пользлвателе восстановлена')
#
#     @allure.description('email содержит цифры в локальной части')
#     def test_04(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_phone(
#             '123456@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.date_of_birth, AuthVariables.user_id_verify_2, access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 200)
#         try:
#             """Проверка наличия обязательных полей"""
#             UserResponse.check_required_fields(result)
#
#             """Проверка значения поля email"""
#             data = Checking.get_data(result)
#             assert data['email'] == '123456@mail.ru'
#         except AssertionError:
#             raise AssertionError
#         finally:
#             """Изменение информации"""
#             UsersMethods.connect_db('pawel_test_1@rambler.ru', AuthVariables.user_id_verify_2)
#             print('информация о пользлвателе восстановлена')
#
#     @allure.description('email Текст в верхнем регистре в локальной части')
#     def test_05(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_phone(
#             'MMM@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.date_of_birth, AuthVariables.user_id_verify_2, access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 200)
#         try:
#             """Проверка наличия обязательных полей"""
#             UserResponse.check_required_fields(result)
#
#             """Проверка значения поля email"""
#             data = Checking.get_data(result)
#             assert data['email'] == 'MMM@mail.ru'
#         except AssertionError:
#             raise AssertionError
#         finally:
#             """Изменение информации"""
#             UsersMethods.connect_db('pawel_test_1@rambler.ru', AuthVariables.user_id_verify_2)
#             print('информация о пользлвателе восстановлена')
#
#     @allure.description('email Текст в нижнем регистре в локальной части')
#     def test_06(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_phone(
#             'mmm@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.date_of_birth, AuthVariables.user_id_verify_2, access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 200)
#         try:
#             """Проверка наличия обязательных полей"""
#             UserResponse.check_required_fields(result)
#
#             """Проверка значения поля email"""
#             data = Checking.get_data(result)
#             assert data['email'] == 'MMM@mail.ru'
#         except AssertionError:
#             raise AssertionError
#         finally:
#             """Изменение информации"""
#             UsersMethods.connect_db('pawel_test_1@rambler.ru', AuthVariables.user_id_verify_2)
#             print('информация о пользлвателе восстановлена')
#
