import allure
import pytest

from common_methods.checking import Checking
from common_methods.variables import CommonVariables, AuthVariables
from Users.methods.users_methods import UsersMethods
from Users.methods.user_payloads import UserResponse


@pytest.mark.User
@allure.epic('Patch/users/me Проверка поля firstname')
class TestPatchUsersEmail:

    @allure.description('firstname - 2 символа')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, 'Mm',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Mm'

    @allure.description('firstname - 3 символa')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, 'Mmm',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Mmm'

    @allure.description('firstname - Кириллица')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, 'Мммв',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Мммв'

    @allure.description('firstname - Латиница')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, 'Llll',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Llll'

    @allure.description('firstname - Пробел')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, 'Lll L',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Lll L'

    @allure.description('firstname - Тире')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, 'Lll-L',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Lll-L'

    @allure.description('firstname - 63 символа')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name,
            'Lllllllllwlllllllllwlllllllllwlllllllllwlllllllllwlllllllllwqqq',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Lllllllllwlllllllllwlllllllllwlllllllllwlllllllllwlllllllllwqqq'

    @allure.description('firstname - 64 символа')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name,
            'Lllllllllwlllllllllwlllllllllwlllllllllwlllllllllwlllllllllwqqqq',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Lllllllllwlllllllllwlllllllllwlllllllllwlllllllllwlllllllllwqqqq'

    @allure.description('firstname - Текст в верхнем регистре')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, 'LLLL',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Llll'

    @allure.description('firstname - Текст в нижнем регистре')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, 'llll',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Llll'

    @allure.description('firstname - Текст в верхнем и нижнем регистре')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, 'Llll',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Llll'

    @allure.description('firstname - 2 пробела подряд')
    def test_12(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, 'Lll  l',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Lll L'

    @allure.description('firstname - 2 тире подряд')
    def test_13(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, 'Lll--l',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Lll-L'

    @allure.description('firstname - Поле отсутствует')
    def test_14(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone_firstname(
            AuthVariables.last_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

    @allure.description('firstname - Пустое поле')
    def test_15(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, '',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('firstname - 65 Символов')
    def test_16(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name,
            'LllllllllwLllllllllwLllllllllwLllllllllwLllllllllwLllllllllwqqqqu',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('firstname - Латиница + Кириллица')
    def test_17(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, 'Qweфыв',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('firstname - 3 пробела подряд')
    def test_18(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, 'Qw   e',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Qw E'

    @allure.description('firstname - 3 тире подряд')
    def test_19(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, 'Qw---e',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Qw-E'

    @allure.description('firstname - Цифры')
    def test_20(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, '123456',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 422)

    @allure.description('firstname - Спецсимволы')
    def test_21(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, '@##%^&*',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 422)

    @allure.description('firstname - Начинается пробелом')
    def test_22(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, ' Rrrr',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Rrrr'

    @allure.description('firstname - Заканчивается пробелом')
    def test_23(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, 'Rrrr ',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Rrrr'

    @allure.description('firstname - Начинается с "тире"')
    def test_24(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, '-Rrrr',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Rrrr'

    @allure.description('firstname - Заканчивается "тире"')
    def test_25(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, 'Rrrr-',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        UserResponse.check_required_fields(result)

        """Проверка значения поля firstname"""
        data = Checking.get_data(result)
        assert data['first_name'] == 'Rrrr'

    @allure.description('firstname - Null')
    def test_26(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, None,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        Checking.check_statuscode(result, 422)

    @allure.description('firstname - 1 символ')
    def test_27(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_email_phone(
            AuthVariables.last_name, 'M',
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)
