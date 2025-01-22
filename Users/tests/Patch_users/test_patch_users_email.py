import allure
import pytest

from common_methods.checking import Checking
from common_methods.variables import AuthVariables
from Users.methods.users_methods import UsersMethods
from Users.methods.user_payloads import UserResponse


@pytest.mark.User
@allure.epic('Patch/users/me Проверка поля email')
class TestPatchUsersEmail:

    @allure.description('Валидный email')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Получение user id"""
        user_id = UsersMethods.get_user_id(access_token)

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_phone(
            AuthVariables.email_for_create_user, AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)
        try:
            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значения поля email"""
            data = Checking.get_data(result)
            assert data['email'] == AuthVariables.email_for_create_user
        except AssertionError:
            raise AssertionError
        finally:
            """Изменение информации"""
            UsersMethods.connect_db('y.pawel_test1@mail.ru', user_id)
            print('информация о пользлвателе восстановлена')

    @allure.description('email - 64 символа в локальной')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Получение user id"""
        user_id = UsersMethods.get_user_id(access_token)

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_phone(
            'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@nowni.com',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )
        try:
            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значения поля email"""
            data = Checking.get_data(result)
            assert data['email'] == 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@nowni.com'
        except AssertionError:
            raise AssertionError
        finally:
            """Изменение информации"""
            UsersMethods.connect_db('y.pawel_test1@mail.ru', user_id)
            print('информация о пользлвателе восстановлена')

    @allure.description('email содержит спецсимволы в локальной части')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Получение user id"""
        user_id = UsersMethods.get_user_id(access_token)

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_phone(
            'a#$%^&*q@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)
        try:
            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значения поля email"""
            data = Checking.get_data(result)
            assert data['email'] == 'a#$%^&*q@mail.ru'
        except AssertionError:
            raise AssertionError
        finally:
            """Изменение информации"""
            UsersMethods.connect_db('y.pawel_test1@mail.ru', user_id)
            print('информация о пользлвателе восстановлена')

    @allure.description('email содержит цифры в локальной части')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Получение user id"""
        user_id = UsersMethods.get_user_id(access_token)

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_phone(
            '123456@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)
        try:
            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значения поля email"""
            data = Checking.get_data(result)
            assert data['email'] == '123456@mail.ru'
        except AssertionError:
            raise AssertionError
        finally:
            """Изменение информации"""
            UsersMethods.connect_db('y.pawel_test1@mail.ru', user_id)
            print('информация о пользлвателе восстановлена')

    @allure.description('email Текст в верхнем регистре в локальной части')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Получение user id"""
        user_id = UsersMethods.get_user_id(access_token)

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_phone(
            'MMM@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)
        try:
            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значения поля email"""
            data = Checking.get_data(result)
            assert data['email'] == 'MMM@mail.ru'
        except AssertionError:
            raise AssertionError
        finally:
            """Изменение информации"""
            UsersMethods.connect_db('y.pawel_test1@mail.ru', user_id)
            print('информация о пользлвателе восстановлена')

    @allure.description('email Текст в нижнем регистре в локальной части')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Получение user id"""
        user_id = UsersMethods.get_user_id(access_token)

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_phone(
            'mmm@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)
        try:
            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значения поля email"""
            data = Checking.get_data(result)
            assert data['email'] == 'mmm@mail.ru'
        except AssertionError:
            raise AssertionError
        finally:
            """Изменение информации"""
            UsersMethods.connect_db('y.pawel_test1@mail.ru', user_id)
            print('информация о пользлвателе восстановлена')

    @allure.description('email Текст в нижнем и в верхнем регистре в локальной части')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Получение user id"""
        user_id = UsersMethods.get_user_id(access_token)

        """Изменение информации"""
        result = UsersMethods.change_user_info_without_phone(
            'MMmmm@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)
        try:
            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значения поля email"""
            data = Checking.get_data(result)
            assert data['email'] == 'MMmmm@mail.ru'
        except AssertionError:
            raise AssertionError
        finally:
            """Изменение информации"""
            UsersMethods.connect_db('y.pawel_test1@mail.ru', user_id)
            print('информация о пользлвателе восстановлена')

    @allure.description('254 символа общая длина email')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Получение user id"""
        user_id = UsersMethods.get_user_id(access_token)

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
        try:
            """Проверка наличия обязательных полей"""
            UserResponse.check_required_fields(result)

            """Проверка значения поля email"""
            data = Checking.get_data(result)
            assert (data['email'] == 'Aa!1234560Aa!1234560Aa!1234560Aa!1234560AaQ1234560AaQ12345601234@AaQ1234560AaQ'
                                     '1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ12345'
                                     '60AaQ1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ'
                                     '1234560AaQ12345.ru'
                    )
        except AssertionError:
            raise AssertionError
        finally:
            """Изменение информации"""
            """Изменение информации"""
            UsersMethods.connect_db('y.pawel_test1@mail.ru', user_id)
            print('информация о пользлвателе восстановлена')

    @allure.description('Поле отсутствует')
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

    @allure.description('65 символов в локальной части')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            'ффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффыыыыв@почта.рф',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('255 символов общая длина email')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            'Aa!1234560Aa!1234560Aa!1234560Aa!1234560AaQ1234560AaQ12345601234@AaQ1234560AaQ1234560AaQ1234560'
            'AaQ1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560123.'
            'AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ12345.ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('email - Латиница + Кириллица')
    def test_12(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            'ффффффqq@mail.ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('email - Пробелы')
    def test_13(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            'фффффф qq@mail.ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('email - Пробелы')
    def test_14(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            'q qq@mail.ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('email - Содержит две точки подряд')
    def test_15(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            'q..qq@mail.ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('email - Содержит два тире подряд')
    def test_16(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            'q--qq@mail.ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('Отсутствие @ в email')
    def test_17(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            'q--qqmail.ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('Отсутствие локальной части')
    def test_18(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            '@mail.ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('Отсутствие доменной части')
    def test_19(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            'qqqq@.ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('Локальная часть начинается  с точки')
    def test_20(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            '.qqqq@mail.ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('Локальная часть заканчивается точкой')
    def test_21(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            'qqqq.@mail.ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('Доменная часть начинается с точки')
    def test_22(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            'qqqq@.mail.ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('Доменная часть  заканчивается точкой')
    def test_23(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            'qqqq@mail..ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('Локальная часть начинается с - (дефиса)')
    def test_24(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            '-qqqq@mail.ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('Локальная часть заканчивается  - (дефисом)')
    def test_25(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            'qqqq-@mail.ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('Доменная часть начинается с - (дефиса)')
    def test_26(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            'qqqq@-mail.ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('Доменная часть заканчивается - (дефисом)')
    def test_27(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            'qqqq@mail-.ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('Пустое поле')
    def test_28(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            '',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)

    @allure.description('Существующий email')
    def test_29(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            'y.pawel_test1@mail.ru',
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 400)

    @allure.description('Null')
    def test_30(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Изменение информации"""
        result = UsersMethods.change_user_info(
            None,
            AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth, access_token
        )

        """Проверка статус кода"""
        UsersMethods.recover_user_info_if_bag(
            result, 'y.pawel_test1@mail.ru', AuthVariables.last_name, AuthVariables.first_name,
            AuthVariables.middle_name, '89260000002', AuthVariables.date_of_birth, access_token
        )
        Checking.check_statuscode(result, 422)





