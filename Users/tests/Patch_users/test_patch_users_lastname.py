import allure
import pytest

from common_methods.checking import Checking
from common_methods.variables import CommonVariables, AuthVariables
from Users.methods.users_methods import UsersMethods
from Users.methods.user_payloads import UserResponse


@pytest.mark.User
@allure.epic('Patch/users/me Проверка поля lastname')
class TestPatchUsersEmail:

    @allure.description('lastname - 1 символ')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'M', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'M'

    @allure.description('lastname - 2 символa')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'Mm', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Mm'

    @allure.description('lastname - Кириллица')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'Мммв', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Мммв'

    @allure.description('lastname - Латиница')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'Llll', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Llll'

    @allure.description('lastname - Пробел')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'Lll L', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Lll L'

    @allure.description('lastname - Пробел')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'Lll L', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Lll L'

    @allure.description('lastname - Тире')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'Lll-L', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Lll-L'

    @allure.description('lastname - 63 символа')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'Lllllllllwlllllllllwlllllllllwlllllllllwlllllllllwlllllllllwqqq',
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Lllllllllwlllllllllwlllllllllwlllllllllwlllllllllwlllllllllwqqq'

    @allure.description('lastname - 64 символа')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'Lllllllllwlllllllllwlllllllllwlllllllllwlllllllllwlllllllllwqqqq',
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Lllllllllwlllllllllwlllllllllwlllllllllwlllllllllwlllllllllwqqqq'

    @allure.description('lastname - Текст в верхнем регистре')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'LLLL', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Llll'

    @allure.description('lastname - Текст в нижнем регистре')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'llll', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Llll'

    @allure.description('lastname - Текст в верхнем и нижнем регистре')
    def test_12(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'Llll', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Llll'

    @allure.description('lastname - 2 пробела подряд')
    def test_13(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'Lll  l', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Lll L'

    @allure.description('lastname - 2 тире подряд')
    def test_14(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'Lll--l', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Lll-L'

    @allure.description('lastname - Поле отсутствует')
    def test_15(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone_lastname(
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

    @allure.description('lastname - Пустое поле')
    def test_16(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            '', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('lastname - 65 Символов')
    def test_17(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'LllllllllwLllllllllwLllllllllwLllllllllwLllllllllwLllllllllwqqqqu',
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('lastname - Латиница + Кириллица')
    def test_17(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'Qweфыв', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('lastname - 3 пробела подряд')
    def test_18(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'Qw   e', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Qw E'

    @allure.description('lastname - 3 тире подряд')
    def test_19(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'Qw---e', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Qw-E'

    @allure.description('lastname - Цифры')
    def test_20(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            '123456', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 422)

    @allure.description('lastname - Спецсимволы')
    def test_21(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            '@##%^&*', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 422)

    @allure.description('lastname - Начинается пробелом')
    def test_22(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            ' Rrrr', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Rrrr'

    @allure.description('lastname - Заканчивается пробелом')
    def test_23(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'Rrrr ', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Rrrr'

    @allure.description('lastname - Начинается с "тире"')
    def test_24(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            '-Rrrr', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Rrrr'

    @allure.description('lastname - Заканчивается "тире"')
    def test_25(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            'Rrrr-', AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля lastname"""
        data = Checking.get_data(result)
        assert data['last_name'] == 'Rrrr'

    @allure.description('lastname - Null')
    def test_26(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            None, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 422)



