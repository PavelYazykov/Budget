# import allure
# from common_methods.checking import Checking
# from common_methods.variables import CommonVariables, AuthVariables
# from Users.methods.users_methods import UsersMethods
# from Users.methods.user_payloads import UserResponse
# from Auth.methods.auth_methods import AuthMethods
#
#
# @allure.epic('Patch/users/id Изменение информации текущий пользователь Проверка поля middlename')
# class TestPatchUsersByIdMiddlename:
#
#     @allure.description('middlename - 4 символa')
#     def test_01(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'Mmmm', AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Mmmm'
#
#     @allure.description('middlename - 5 символов')
#     def test_02(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'Mmmmm', AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Mmmmm'
#
#     @allure.description('middlename - Кириллица')
#     def test_03(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'Ммммм', AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Ммммм'
#
#     @allure.description('middlename - Латиница')
#     def test_04(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'Vvvvv', AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Vvvvv'
#
#     @allure.description('middlename - Пробел')
#     def test_05(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'Vv v', AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Vv V'
#
#     @allure.description('middlename - Тире')
#     def test_06(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'Vv-v', AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Vv-V'
#
#     @allure.description('middlename - 63 символа')
#     def test_07(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name,
#             AuthVariables.first_name,
#             'Vvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqwww',
#             AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Vvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqwww'
#
#     @allure.description('middlename - 64 символа')
#     def test_08(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name,
#             AuthVariables.first_name,
#             'Vvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqwwww',
#             AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Vvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqwwww'
#
#     @allure.description('middlename - Текст в верхнем регистре')
#     def test_09(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'VVVVV', AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Vvvvv'
#
#     @allure.description('middlename - Текст в нижнем регистре')
#     def test_10(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'vvvvv', AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Vvvvv'
#
#     @allure.description('middlename - Текст в верхнем и нижнем регистре')
#     def test_11(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'Vvvvv', AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Vvvvv'
#
#     @allure.description('middlename - 2 пробела подряд')
#     def test_12(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'Vv  vv', AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Vv Vv'
#
#     @allure.description('middlename - 2 тире подряд')
#     def test_13(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'Vv--vvv', AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Vv-Vvv'
#
#     @allure.description('middlename - Поле отсутствует')
#     def test_14(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone_middlename(
#             AuthVariables.last_name, AuthVariables.first_name,
#             AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 200)
#
#         """Проверка наличия обязательных полей"""
#         UserResponse.check_required_fields(result)
#
#     @allure.description('middlename - Пустое поле')
#     def test_15(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             '', AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 200)
#
#     @allure.description('middlename - 65 Символов')
#     def test_16(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name,
#             AuthVariables.first_name,
#             'Vvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqvvvvvvvvvqwwwwr',
#             AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#     @allure.description('middlename - Латиница + Кириллица')
#     def test_17(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'Vvммvv', AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#     @allure.description('middlename - 3 пробела подряд')
#     def test_18(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'Vv   vvv', AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Vv Vvv'
#
#     @allure.description('middlename - 3 тире подряд')
#     def test_19(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'Vv---vvv', AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Vv-Vvv'
#
#     @allure.description('middlename - Цифры')
#     def test_20(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             '123456', AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#     @allure.description('middlename - Спецсимволы')
#     def test_21(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             '@#$%^&&*', AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#     @allure.description('middlename - Начинается пробелом')
#     def test_22(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             ' Vvvvv', AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Vvvvv'
#
#     @allure.description('middlename - Заканчивается пробелом')
#     def test_23(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'Vvvvv ', AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Vvvvv'
#
#     @allure.description('middlename - Начинается с "тире"')
#     def test_24(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             '-Vvvvv', AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Vvvvv'
#
#     @allure.description('middlename - Заканчивается "тире"')
#     def test_25(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'Vvvvv-', AuthVariables.date_of_birth, user_id,
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
#         assert data['middle_name'] == 'Vvvvv'
#
#     @allure.description('middlename - Null')
#     def test_26(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             None, AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 200)
#
#         """Проверка наличия обязательных полей"""
#         UserResponse.check_required_fields(result)
#
#     @allure.description('middlename - не менее 4 символов после удаления лишних пробелов')
#     def test_27(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'V  vv', AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#     @allure.description('middlename - не менее 4 символов после удаления лишних тире')
#     def test_28(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'V---v', AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#     @allure.description('middlename - 3 символa')
#     def test_29(self, auth_fixture, create_and_delete_users):
#         """Регистрация пользователя"""
#         user_id = create_and_delete_users
#
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Изменение информации"""
#         result = UsersMethods.change_user_info_by_id_without_email_phone(
#             AuthVariables.last_name, AuthVariables.first_name,
#             'Mmm', AuthVariables.date_of_birth, user_id,
#             access_token
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 422)
#
#
