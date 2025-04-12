import time

import allure
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.auth import Auth
from common_methods.checking import Checking
from common_methods.variables import AuthVariables
from Users.methods.users_methods import UsersMethods
from Users.methods.user_payloads import UserResponse


@pytest.mark.User
@allure.epic('Patch/users/me Проверка поля email')
class TestPatchUsersEmail:

    @allure.description('Проверка поля email - Валидный email')
    def test_01(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)
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

            """Изменение информации"""
            result = UsersMethods.change_user_info_without_phone(
                AuthVariables.email_for_create_user_2, AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значения поля email"""
            data = Checking.get_data(result)
            assert data['email'] == AuthVariables.email_for_create_user_2

        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - email - 64 символа в локальной -> Mail use not real domain')
    def test_02(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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
            """Изменение информации"""
            result = UsersMethods.change_user_info_without_phone(
                'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@mail.ru',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значения поля email"""
            data = Checking.get_data(result)
            assert data['email'] == 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@mail.ru'
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - email содержит спецсимволы в локальной части')
    def test_03(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info_without_phone(
                'a#$%^&*q@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значения поля email"""
            data = Checking.get_data(result)
            assert data['email'] == 'a#$%^&*q@mail.ru'
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - email содержит цифры в локальной части')
    def test_04(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info_without_phone(
                '123456@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значения поля email"""
            data = Checking.get_data(result)
            assert data['email'] == '123456@mail.ru'
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - email Текст в верхнем регистре в локальной части')
    def test_05(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)
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

            """Изменение информации"""
            result = UsersMethods.change_user_info_without_phone(
                'MMM@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значения поля email"""
            data = Checking.get_data(result)
            assert data['email'] == 'MMM@mail.ru'
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - email Текст в нижнем регистре в локальной части')
    def test_06(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)
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

            """Изменение информации"""
            result = UsersMethods.change_user_info_without_phone(
                'mmm@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значения поля email"""
            data = Checking.get_data(result)
            assert data['email'] == 'mmm@mail.ru'
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - email Текст в нижнем и в верхнем регистре в локальной части')
    def test_07(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)
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

            """Изменение информации"""
            result = UsersMethods.change_user_info_without_phone(
                'MMmmm@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значения поля email"""
            data = Checking.get_data(result)
            assert data['email'] == 'MMmmm@mail.ru'
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email- 254 символа общая длина email -> Mail use not real domain')
    def test_08(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)
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

            """Изменение информации"""
            result = UsersMethods.change_user_info_without_phone(
                'Aa!1234560Aa!1234560Aa!1234560Aa!1234560AaQ1234560AaQ12345601234@AaQ1234560AaQ1234560AaQ1234560'
                'AaQ1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560123.'
                'AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ12345.ru',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значения поля email"""
            data = Checking.get_data(result)
            assert (data['email'] == 'Aa!1234560Aa!1234560Aa!1234560Aa!1234560AaQ1234560AaQ12345601234@AaQ1234560AaQ'
                                     '1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ12345'
                                     '60AaQ1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ'
                                     '1234560AaQ12345.ru'
                    )
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Поле отсутствует')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

    @allure.description('Проверка поля email - 65 символов в локальной части')
    def test_10(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)
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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                'ффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффыыыыв@почта.рф',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - 255 символов общая длина email -> Mail use not real domain')
    def test_11(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                'Aa!1234560Aa!1234560Aa!1234560Aa!1234560AaQ1234560AaQ12345601234@AaQ1234560AaQ1234560AaQ1234560'
                'AaQ1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560123.'
                'AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ12345.ru',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - email - Латиница + Кириллица')
    def test_12(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)
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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                'ффффффqq@mail.ru',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Пробелы')
    def test_13(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                'фффффф qq@mail.ru',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Содержит две точки подряд')
    def test_14(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                'qqq..q@mail.ru',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Содержит два тире подряд')
    def test_15(self):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                'qqq--q@mail.ru',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Отсутствие @ в email')
    def test_16(self, auth_fixture):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                'qqmail.ru',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Отсутствие локальной части')
    def test_17(self, auth_fixture):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                '@mail.ru',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Отсутствие доменной части')
    def test_18(self, auth_fixture):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                'qqqq@',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email- Локальная часть начинается  с точки')
    def test_19(self, auth_fixture):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                '.qqqq@mail.ru',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Локальная часть заканчивается точкой')
    def test_20(self, auth_fixture):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                'qqqq.@mail.ru',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Доменная часть начинается с точки')
    def test_21(self, auth_fixture):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                'qqqq@.mail.ru',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Доменная часть  заканчивается точкой')
    def test_22(self, auth_fixture):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                'qqqq@mail..ru',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Локальная часть начинается с - (дефиса)')
    def test_23(self, auth_fixture):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                '-qqqq@mail.ru',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Локальная часть заканчивается  - (дефисом)')
    def test_24(self, auth_fixture):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                'qqqq-@mail.ru',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Доменная часть начинается с - (дефиса)')
    def test_25(self, auth_fixture):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                'qqqq@-mail.ru',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Доменная часть заканчивается - (дефисом)')
    def test_26(self, auth_fixture):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                'qqqq@mail-.ru',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Пустое поле')
    def test_27(self, auth_fixture):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                '',
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Существующий email')
    def test_28(self, auth_fixture):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                AuthVariables.email_for_create_user,
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 400)
        finally:
            AuthMethods.delete_user(user_id)

    @allure.description('Проверка поля email - Null')
    def test_29(self, auth_fixture):
        """Создание пользователя"""
        result_create_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.middle_name, AuthVariables.phone_for_create_user,
            AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_user, 201)
        """Получение user id"""
        data, user_id = AuthMethods.get_id(result_create_user)
        time.sleep(2)

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

            """Изменение информации"""
            result = UsersMethods.change_user_info(
                None,
                AuthVariables.last_name, AuthVariables.first_name,
                AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            AuthMethods.delete_user(user_id)





