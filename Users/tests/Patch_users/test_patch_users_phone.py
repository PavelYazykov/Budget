import allure
import pytest

from common_methods.checking import Checking
from common_methods.variables import CommonVariables, AuthVariables
from Users.methods.users_methods import UsersMethods
from Users.methods.user_payloads import UserResponse


@pytest.mark.Users
@allure.epic('Patch/users/me Проверка поля phone')
class TestPatchUsersPhone:

    @allure.description('phone - 11 цифр ')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '80000000002', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля phone"""
        data = Checking.get_data(result)
        assert data['phone_number'] == '80000000002'

    @allure.description('phone - Null')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, None, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('phone - 10 символов')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '8000000000', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('phone - 12 символов')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '800000000000', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('phone - Буквы')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, 'фывапроывап', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('phone - спецсимволы')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '@#$%^&*@#$%', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('phone - Поле отсутствует')
    def test_07(self, auth_fixture):
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

    @allure.description('phone - Пустое поле')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('phone - Неверный тип данных (integer)')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, 80000000002, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Номер телефона по умолчанию - 80000000002 ')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Получение user id"""
        user_id = UsersMethods.get_user_id(access_token)

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email(
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        UsersMethods.connect_db('y.pawel_test1@mail.ru', user_id)



