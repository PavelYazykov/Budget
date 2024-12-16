# import allure
# from common_methods.checking import Checking
# from common_methods.variables import CommonVariables, AuthVariables
# from Users.methods.users_methods import UsersMethods
# from Users.methods.user_payloads import UserResponse
# from Auth.methods.auth_methods import AuthMethods
#
#
# @allure.epic('Patch/users/id Изменение информации текущий пользователь Проверка поля lastname')
# class TestPatchUsersByIdLastname:
#
#     @allure.description('lastname - 1 символ')
#     def test_01(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'M', AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'M'
#
#     @allure.description('lastname - 2 символa')
#     def test_02(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'Mm', AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Mm'
#
#     @allure.description('lastname - Кириллица')
#     def test_03(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'Ммм', AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Ммм'
#
#     @allure.description('lastname - Латиница')
#     def test_04(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'Vvv', AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Vvv'
#
#     @allure.description('lastname - Пробел')
#     def test_05(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'Vv v', AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Vv V'
#
#     @allure.description('lastname - Тире')
#     def test_06(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'Vv-v', AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Vv-V'
#
#     @allure.description('lastname - 63 символа')
#     def test_07(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'Vvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqwww',
#             AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Vvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqwww'
#
#     @allure.description('lastname - 64 символа')
#     def test_08(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'Vvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqwwww',
#             AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Vvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqwwww'
#
#     @allure.description('lastname - Текст в верхнем регистре')
#     def test_09(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'VVV', AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Vvv'
#
#     @allure.description('lastname - Текст в нижнем регистре')
#     def test_10(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'vvv', AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Vvv'
#
#     @allure.description('lastname - Текст в верхнем и нижнем регистре')
#     def test_11(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'Vvv', AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Vvv'
#
#     @allure.description('lastname - 2 пробела подряд')
#     def test_12(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'Vv  v', AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Vv V'
#
#     @allure.description('lastname - 2 тире подряд')
#     def test_13(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'Vv--v', AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Vv-V'
#
#     @allure.description('lastname - Поле отсутствует')
#     def test_14(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone_lastname(
#             AuthVariables.first_name,
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
#     @allure.description('lastname - Пустое поле')
#     def test_15(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             '', AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#     @allure.description('lastname - 65 Символов')
#     def test_16(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'Vvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqwwwwr',
#             AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#     @allure.description('lastname - Латиница + Кириллица')
#     def test_17(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'Vvмм', AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#     @allure.description('lastname - 3 пробела подряд')
#     def test_18(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'Vv   v', AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Vv V'
#
#     @allure.description('lastname - 3 тире подряд')
#     def test_19(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'Vv---v', AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Vv-V'
#
#     @allure.description('lastname - Цифры')
#     def test_20(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             '123456', AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#     @allure.description('lastname - Спецсимволы')
#     def test_21(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             '@#$%^&&*', AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#     @allure.description('lastname - Начинается пробелом')
#     def test_22(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             ' Vvv', AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Vvv'
#
#     @allure.description('lastname - Заканчивается пробелом')
#     def test_23(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'Vvv ', AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Vvv'
#
#     @allure.description('lastname - Начинается с "тире"')
#     def test_24(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             '-Vvv', AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Vvv'
#
#     @allure.description('lastname - Заканчивается "тире"')
#     def test_25(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             'Vvv-', AuthVariables.first_name,
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
#         """Проверка значения поля lastname"""
#         data = Checking.get_data(result)
#         assert data['last_name'] == 'Vvv'
#
#     @allure.description('lastname - Null')
#     def test_26(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             None, AuthVariables.first_name,
#             AuthVariables.middle_name, AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#
#
