import allure
import pytest

from common_methods.checking import Checking
from common_methods.variables import AuthVariables
from Users.methods.users_methods import UsersMethods
from Users.methods.user_payloads import UserResponse


@pytest.mark.User
@allure.epic('Patch/users/me Проверка поля middlename')
class TestPatchUsersEmail:

    @allure.description('middlename - 1 символ')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            'A', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'A'

    @allure.description('middlename - 2 символа')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            'Aa', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Aa'

    @allure.description('middlename - Кириллица')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            'Фыыы', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Фыыы'

    @allure.description('middlename - Латиница')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            'Llll', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Llll'

    @allure.description('middlename - Пробел')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            'Lll L', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Lll L'

    @allure.description('middlename - Тире')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            'Lll-L', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Lll-L'

    @allure.description('middlename - 63 символа')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name,
            AuthVariables.first_name,
            'Lllllllllwlllllllllwlllllllllwlllllllllwlllllllllwlllllllllwqqq',
            AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Lllllllllwlllllllllwlllllllllwlllllllllwlllllllllwlllllllllwqqq'

    @allure.description('middlename - 64 символа')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name,
            AuthVariables.first_name,
            'Lllllllllwlllllllllwlllllllllwlllllllllwlllllllllwlllllllllwqqqq',
            AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Lllllllllwlllllllllwlllllllllwlllllllllwlllllllllwlllllllllwqqqq'

    @allure.description('middlename - Текст в верхнем регистре')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            'LLLL', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Llll'

    @allure.description('middlename - Текст в нижнем регистре')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            'llll', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Llll'

    @allure.description('middlename - Текст в верхнем и нижнем регистре')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            'Llll', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Llll'

    @allure.description('middlename - 2 пробела подряд')
    def test_12(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            'Lll  l', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Lll L'

    @allure.description('middlename - 2 тире подряд')
    def test_13(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            'Lll--l', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Lll-L'

    @allure.description('middlename - Поле отсутствует')
    def test_14(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone_middlename(
            AuthVariables.last_name,
            AuthVariables.first_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

    @allure.description('middlename - Пустое поле')
    def test_15(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            '', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

    @allure.description('middlename - 65 Символов')
    def test_16(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name,
            AuthVariables.first_name,
            'LllllllllwLllllllllwLllllllllwLllllllllwLllllllllwLllllllllwqqqqu',
            AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('middlename - Латиница + Кириллица')
    def test_17(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            'Qweфыв', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('middlename - 3 пробела подряд')
    def test_18(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            'Qw   e', AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Qw E'

    @allure.description('middlename - 3 тире подряд')
    def test_19(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            'Qw---e', AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Qw-E'

    @allure.description('middlename - Цифры')
    def test_20(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            '123456', AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 422)

    @allure.description('middlename - Спецсимволы')
    def test_21(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            '@##%^&*', AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 422)

    @allure.description('middlename - Начинается пробелом')
    def test_22(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            ' Rrrr', AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Rrrr'

    @allure.description('middlename - Заканчивается пробелом')
    def test_23(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            'Rrrr ', AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Rrrr'

    @allure.description('middlename - Начинается с "тире"')
    def test_24(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            '-Rrrr', AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Rrrr'

    @allure.description('middlename - Заканчивается "тире"')
    def test_25(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            'Rrrr-', AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля middlename"""
        data = Checking.get_data(result)
        assert data['middle_name'] == 'Rrrr'

    @allure.description('middlename - Null')
    def test_26(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, AuthVariables.first_name,
            None, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)
