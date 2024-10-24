import allure
from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking

email = 'qa@mail.ru'
password = 'Samsung@9@9@9'
last_name = 'Иванов'
first_name = 'Иван'
middle_name = 'Иванович'
phone = '89261111111'
date_of_birth = '2000-01-01'


@allure.epic('Post/registration Проверка поля email')
class TestRegistrationEmailField:

    @allure.description('Валидный email')
    def test_01(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            required_fields = {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "email": "user@example.com",
                "is_active": True,
                "is_email_verified": False,
                "is_phone_verified": False,
                "last_name": "Иванов",
                "first_name": "Иван",
                "middle_name": "Иванович",
                "phone_number": "88005555535",
                "date_of_birth": "2024-10-09",
                "avatar": "string"
            }
            data, user_id = AuthMethods.check_required_fields(result, required_fields)

            """Проверка значений обязательных полей"""
            required_fields_values = {
                "email": email,
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "phone_number": phone,
                "date_of_birth": date_of_birth
            }
            for field, value in required_fields_values.items():
                assert field, value in data

            """Проверка наличия пользователя в БД"""
            cursor = AuthMethods.connect_db()
            cursor.execute(f"""SELECT * FROM users WHERE id= '{user_id}'""")
            result_db = cursor.fetchone()
            print(result_db)
            assert result_db[1] == last_name, f'Неверное значение в поле {last_name}'
            assert result_db[2] == first_name, f'Неверное значение в поле {first_name}'
            assert result_db[3] == middle_name, f'Неверное значение в поле {middle_name}'
            assert result_db[5] == phone, f'Неверное значение в поле {phone}'
            assert result_db[6] == email, f'Неверное значение в поле {email}'
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('64 символа в локальной части')
    def test_02(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz10123@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            required_fields = {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "email": "user@example.com",
                "is_active": True,
                "is_email_verified": False,
                "is_phone_verified": False,
                "last_name": "Иванов",
                "first_name": "Иван",
                "middle_name": "Иванович",
                "phone_number": "88005555535",
                "date_of_birth": "2024-10-09",
                "avatar": "string"
            }
            data, user_id = AuthMethods.check_required_fields(result, required_fields)

            """Проверка значений обязательных полей"""
            required_fields_values = {
                "email": 'zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz10123@mail.ru',
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "phone_number": phone,
                "date_of_birth": date_of_birth
            }
            for field, value in required_fields_values.items():
                assert field, value in data

            """Проверка наличия пользователя в БД"""
            cursor = AuthMethods.connect_db()
            cursor.execute(f"""SELECT * FROM users WHERE id= '{user_id}'""")
            result_db = cursor.fetchone()
            print(result_db)
            assert result_db[1] == last_name, f'Неверное значение в поле {last_name}'
            assert result_db[2] == first_name, f'Неверное значение в поле {first_name}'
            assert result_db[3] == middle_name, f'Неверное значение в поле {middle_name}'
            assert result_db[5] == phone, f'Неверное значение в поле {phone}'
            assert result_db[6] == 'zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz10123@mail.ru', \
                'Неверное значение в поле email'
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(
                'zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz10123@mail.ru'
            )

    @allure.description('спецсимволы в локальной части email')
    def test_03(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'z!2$%^&*qa@mail.ru', password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            required_fields = {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "email": "user@example.com",
                "is_active": True,
                "is_email_verified": False,
                "is_phone_verified": False,
                "last_name": "Иванов",
                "first_name": "Иван",
                "middle_name": "Иванович",
                "phone_number": "88005555535",
                "date_of_birth": "2024-10-09",
                "avatar": "string"
            }
            data, user_id = AuthMethods.check_required_fields(result, required_fields)

            """Проверка значений обязательных полей"""
            required_fields_values = {
                "email": 'z!2$%^&*qa@mail.ru',
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "phone_number": phone,
                "date_of_birth": date_of_birth
            }
            for field, value in required_fields_values.items():
                assert field, value in data

            """Проверка наличия пользователя в БД"""
            cursor = AuthMethods.connect_db()
            cursor.execute(f"""SELECT * FROM users WHERE id= '{user_id}'""")
            result_db = cursor.fetchone()
            print(result_db)
            assert result_db[1] == last_name, f'Неверное значение в поле {last_name}'
            assert result_db[2] == first_name, f'Неверное значение в поле {first_name}'
            assert result_db[3] == middle_name, f'Неверное значение в поле {middle_name}'
            assert result_db[5] == phone, f'Неверное значение в поле {phone}'
            assert result_db[6] == 'z!2$%^&*qa@mail.ru', 'Неверное значение в поле email'
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('z!2$%^&*qa@mail.ru')

    @allure.description('Цифры')
    def test_04(self):
        """Регистрация"""
        result = AuthMethods.registration(
            '123456789@mail.ru', password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            required_fields = {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "email": "user@example.com",
                "is_active": True,
                "is_email_verified": False,
                "is_phone_verified": False,
                "last_name": "Иванов",
                "first_name": "Иван",
                "middle_name": "Иванович",
                "phone_number": "88005555535",
                "date_of_birth": "2024-10-09",
                "avatar": "string"
            }
            data, user_id = AuthMethods.check_required_fields(result, required_fields)

            """Проверка значений обязательных полей"""
            required_fields_values = {
                "email": '123456789@mail.ru',
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "phone_number": phone,
                "date_of_birth": date_of_birth
            }
            for field, value in required_fields_values.items():
                assert field, value in data

            """Проверка наличия пользователя в БД"""
            cursor = AuthMethods.connect_db()
            cursor.execute(f"""SELECT * FROM users WHERE id= '{user_id}'""")
            result_db = cursor.fetchone()
            print(result_db)
            assert result_db[1] == last_name, f'Неверное значение в поле {last_name}'
            assert result_db[2] == first_name, f'Неверное значение в поле {first_name}'
            assert result_db[3] == middle_name, f'Неверное значение в поле {middle_name}'
            assert result_db[5] == phone, f'Неверное значение в поле {phone}'
            assert result_db[6] == '123456789@mail.ru', 'Неверное значение в поле email'
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('123456789@mail.ru')

    @allure.description('Текст в верхнем регистре')
    def test_05(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'QWERTYUIOP@mail.ru', password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            required_fields = {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "email": "user@example.com",
                "is_active": True,
                "is_email_verified": False,
                "is_phone_verified": False,
                "last_name": "Иванов",
                "first_name": "Иван",
                "middle_name": "Иванович",
                "phone_number": "88005555535",
                "date_of_birth": "2024-10-09",
                "avatar": "string"
            }
            data, user_id = AuthMethods.check_required_fields(result, required_fields)

            """Проверка значений обязательных полей"""
            required_fields_values = {
                "email": 'QWERTYUIOP@mail.ru',
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "phone_number": phone,
                "date_of_birth": date_of_birth
            }
            for field, value in required_fields_values.items():
                assert field, value in data

            """Проверка наличия пользователя в БД"""
            cursor = AuthMethods.connect_db()
            cursor.execute(f"""SELECT * FROM users WHERE id= '{user_id}'""")
            result_db = cursor.fetchone()
            print(result_db)
            assert result_db[1] == last_name, f'Неверное значение в поле {last_name}'
            assert result_db[2] == first_name, f'Неверное значение в поле {first_name}'
            assert result_db[3] == middle_name, f'Неверное значение в поле {middle_name}'
            assert result_db[5] == phone, f'Неверное значение в поле {phone}'
            assert result_db[6] == 'QWERTYUIOP@mail.ru', 'Неверное значение в поле email'
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('QWERTYUIOP@mail.ru')

    @allure.description('Текст в нижнем регистре')
    def test_06(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwertyuiop@mail.ru', password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            required_fields = {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "email": "user@example.com",
                "is_active": True,
                "is_email_verified": False,
                "is_phone_verified": False,
                "last_name": "Иванов",
                "first_name": "Иван",
                "middle_name": "Иванович",
                "phone_number": "88005555535",
                "date_of_birth": "2024-10-09",
                "avatar": "string"
            }
            data, user_id = AuthMethods.check_required_fields(result, required_fields)

            """Проверка значений обязательных полей"""
            required_fields_values = {
                "email": 'qwertyuiop@mail.ru',
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "phone_number": phone,
                "date_of_birth": date_of_birth
            }
            for field, value in required_fields_values.items():
                assert field, value in data

            """Проверка наличия пользователя в БД"""
            cursor = AuthMethods.connect_db()
            cursor.execute(f"""SELECT * FROM users WHERE id= '{user_id}'""")
            result_db = cursor.fetchone()
            print(result_db)
            assert result_db[1] == last_name, f'Неверное значение в поле {last_name}'
            assert result_db[2] == first_name, f'Неверное значение в поле {first_name}'
            assert result_db[3] == middle_name, f'Неверное значение в поле {middle_name}'
            assert result_db[5] == phone, f'Неверное значение в поле {phone}'
            assert result_db[6] == 'qwertyuiop@mail.ru', 'Неверное значение в поле email'
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('qwertyuiop@mail.ru')

    @allure.description('254 символа общая длина email')  # Будет падать: "Mail use not real domain"
    def test_07(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'Aa!1234560Aa!1234560Aa!1234560Aa!1234560AaQ1234560AaQ12345601234@AaQ1234560AaQ1234560AaQ1234560'
            'AaQ1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560123.'
            'AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ12345.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            required_fields = {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "email": "user@example.com",
                "is_active": True,
                "is_email_verified": False,
                "is_phone_verified": False,
                "last_name": "Иванов",
                "first_name": "Иван",
                "middle_name": "Иванович",
                "phone_number": "88005555535",
                "date_of_birth": "2024-10-09",
                "avatar": "string"
            }
            data, user_id = AuthMethods.check_required_fields(result, required_fields)

            """Проверка значений обязательных полей"""
            required_fields_values = {
                "email": 'Aa!1234560Aa!1234560Aa!1234560Aa!1234560AaQ1234560AaQ12345601234@AaQ1234560AaQ1234560'
                         'AaQ1234560AaQ1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ1234560AaQ1234560'
                         'AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ12345.ru',
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "phone_number": phone,
                "date_of_birth": date_of_birth
            }
            for field, value in required_fields_values.items():
                assert field, value in data

            """Проверка наличия пользователя в БД"""
            cursor = AuthMethods.connect_db()
            cursor.execute(f"""SELECT * FROM users WHERE id= '{user_id}'""")
            result_db = cursor.fetchone()
            print(result_db)
            assert result_db[1] == last_name, f'Неверное значение в поле {last_name}'
            assert result_db[2] == first_name, f'Неверное значение в поле {first_name}'
            assert result_db[3] == middle_name, f'Неверное значение в поле {middle_name}'
            assert result_db[5] == phone, f'Неверное значение в поле {phone}'
            assert result_db[6] == ('Aa!1234560Aa!1234560Aa!1234560Aa!1234560AaQ1234560AaQ12345601234@AaQ1234560'
                                    'AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560'
                                    'AaQ1234560AaQ1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ1234560'
                                    'AaQ1234560AaQ1234560AaQ12345.ru'), 'Неверное значение в поле email'
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('Aa!1234560Aa!1234560Aa!1234560'
                                                   'Aa!1234560AaQ1234560AaQ12345601234@AaQ1234560AaQ1234560AaQ1234560'
                                                   'AaQ1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ1234560'
                                                   'AaQ1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ1234560'
                                                   'AaQ1234560AaQ1234560AaQ12345.ru')

    @allure.description('Кириллица')
    def test_08(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'йцукенгшщз@почта.рф', password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            required_fields = {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "email": "user@example.com",
                "is_active": True,
                "is_email_verified": False,
                "is_phone_verified": False,
                "last_name": "Иванов",
                "first_name": "Иван",
                "middle_name": "Иванович",
                "phone_number": "88005555535",
                "date_of_birth": "2024-10-09",
                "avatar": "string"
            }
            data, user_id = AuthMethods.check_required_fields(result, required_fields)

            """Проверка значений обязательных полей"""
            required_fields_values = {
                "email": 'йцукенгшщз@почта.рф',
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "phone_number": phone,
                "date_of_birth": date_of_birth
            }
            for field, value in required_fields_values.items():
                assert field, value in data

            """Проверка наличия пользователя в БД"""
            cursor = AuthMethods.connect_db()
            cursor.execute(f"""SELECT * FROM users WHERE id= '{user_id}'""")
            result_db = cursor.fetchone()
            print(result_db)
            assert result_db[1] == last_name, f'Неверное значение в поле {last_name}'
            assert result_db[2] == first_name, f'Неверное значение в поле {first_name}'
            assert result_db[3] == middle_name, f'Неверное значение в поле {middle_name}'
            assert result_db[5] == phone, f'Неверное значение в поле {phone}'
            assert result_db[6] == 'йцукенгшщз@почта.рф', f'Неверное значение в поле {email}'
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('йцукенгшщз@почта.рф')

    @allure.description('Латиница')
    def test_09(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'asdfghjkl@mail.ru', password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            required_fields = {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "email": "user@example.com",
                "is_active": True,
                "is_email_verified": False,
                "is_phone_verified": False,
                "last_name": "Иванов",
                "first_name": "Иван",
                "middle_name": "Иванович",
                "phone_number": "88005555535",
                "date_of_birth": "2024-10-09",
                "avatar": "string"
            }
            data, user_id = AuthMethods.check_required_fields(result, required_fields)

            """Проверка значений обязательных полей"""
            required_fields_values = {
                "email": 'asdfghjkl@mail.ru',
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "phone_number": phone,
                "date_of_birth": date_of_birth
            }
            for field, value in required_fields_values.items():
                assert field, value in data

            """Проверка наличия пользователя в БД"""
            cursor = AuthMethods.connect_db()
            cursor.execute(f"""SELECT * FROM users WHERE id= '{user_id}'""")
            result_db = cursor.fetchone()
            print(result_db)
            assert result_db[1] == last_name, f'Неверное значение в поле {last_name}'
            assert result_db[2] == first_name, f'Неверное значение в поле {first_name}'
            assert result_db[3] == middle_name, f'Неверное значение в поле {middle_name}'
            assert result_db[5] == phone, f'Неверное значение в поле {phone}'
            assert result_db[6] == 'asdfghjkl@mail.ru', f'Неверное значение в поле {email}'
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('asdfghjkl@mail.ru')

    @allure.description('159 символов доменная часть')
    def test_10(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'testtest12@testtest12testtest12testtest12testtest12testtest12testtest12123.testtest12testtest12test'
            'test12testtest12testtest12testtest12123.com',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)  # Будет падать: "Mail use not real domain"

        """Проверка наличия обязательных полей в ответе"""
        try:
            required_fields = {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "email": "user@example.com",
                "is_active": True,
                "is_email_verified": False,
                "is_phone_verified": False,
                "last_name": "Иванов",
                "first_name": "Иван",
                "middle_name": "Иванович",
                "phone_number": "88005555535",
                "date_of_birth": "2024-10-09",
                "avatar": "string"
            }
            data, user_id = AuthMethods.check_required_fields(result, required_fields)

            """Проверка значений обязательных полей"""
            required_fields_values = {
                "email": 'testtest12@testtest12testtest12testtest12testtest12testtest12testtest12123.testtest12testtes'
                         't12testtest12testtest12testtest12testtest12123.com',
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "phone_number": phone,
                "date_of_birth": date_of_birth
            }
            for field, value in required_fields_values.items():
                assert field, value in data

            """Проверка наличия пользователя в БД"""
            cursor = AuthMethods.connect_db()
            cursor.execute(f"""SELECT * FROM users WHERE id= '{user_id}'""")
            result_db = cursor.fetchone()
            print(result_db)
            assert result_db[1] == last_name, f'Неверное значение в поле {last_name}'
            assert result_db[2] == first_name, f'Неверное значение в поле {first_name}'
            assert result_db[3] == middle_name, f'Неверное значение в поле {middle_name}'
            assert result_db[5] == phone, f'Неверное значение в поле {phone}'
            assert result_db[6] == ('testtest12@testtest12testtest12testtest12testtest12testtest12testtest12123.'
                                    'testtest12testtest12testtest12testtest12testtest12testtest12123.com'), \
                f'Неверное значение в поле {email}'
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('testtest12@testtest12testtest12testtest12testtest12testtest12test'
                                                   'test12123.testtest12testtest12testtest12testtest12testtest12testtes'
                                                   't12123.com')

    @allure.description('65 символов в локальной части')
    def test_11(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz101234@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(
                'zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz1zzzzzzzzz101234@mail.ru'
            )
        Checking.check_statuscode(result, 422)

    @allure.description('255 символа общая длина email')
    def test_12(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'Aa!1234560Aa!1234560Aa!1234560Aa!1234560AaQ1234560AaQ12345601234@AaQ1234560AaQ1234560AaQ1234560Aa'
            'Q1234560AaQ1234560AaQ1234560123.AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560123.A'
            'aQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ123255.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('Aa!1234560Aa!1234560Aa!1234560Aa!1234560AaQ1234560AaQ12345601234@'
                                                   'AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560123.'
                                                   'AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560123.'
                                                   'AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ1234560AaQ123255.ru')
        Checking.check_statuscode(result, 422)

    @allure.description('Латиница + Кириллица')
    def test_13(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'йцукенг@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('йцукенг@mail.ru')
        Checking.check_statuscode(result, 422)

    @allure.description('Пробелы')
    def test_14(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwer @mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('qwer @mail.ru')
        Checking.check_statuscode(result, 422)

    @allure.description('Содержит две точки подряд')
    def test_15(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwer..@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('qwer..@mail.ru')
        Checking.check_statuscode(result, 422)

    @allure.description('Содержит две тире подряд')
    def test_16(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwer--@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('qwer--@mail.ru')
        Checking.check_statuscode(result, 422)

    @allure.description('Отсутствие @ в email')
    def test_17(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwermail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('qwermail.ru')
        Checking.check_statuscode(result, 422)

    @allure.description('Отсутствие локальной части')
    def test_18(self):
        """Регистрация"""
        result = AuthMethods.registration(
            '@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('@mail.ru')
        Checking.check_statuscode(result, 422)

    @allure.description('Отсутствие доменной части')
    def test_19(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwertyui@.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('qwertyui@.ru')
        Checking.check_statuscode(result, 422)

    @allure.description('Локальная часть начинается  с точки')
    def test_20(self):
        """Регистрация"""
        result = AuthMethods.registration(
            '.qwer@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('.qwer@mail.ru')
        Checking.check_statuscode(result, 422)

    @allure.description('Локальная часть заканчивается точкой')
    def test_21(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwertyui.@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('.qwertyui.@mail.ru')
        Checking.check_statuscode(result, 422)

    @allure.description('Доменная часть начинается  с точки')
    def test_22(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwer@.mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('qwer@.mail.ru')
        Checking.check_statuscode(result, 422)

    @allure.description('Доменная часть заканчивается точкой')
    def test_23(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwer@mail..ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('qwer@mail..ru')
        Checking.check_statuscode(result, 422)

    @allure.description('Локальная часть начинается  с тире')
    def test_24(self):
        """Регистрация"""
        result = AuthMethods.registration(
            '-qwertyui@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('-qwertyui@mail.ru')
        Checking.check_statuscode(result, 422)

    @allure.description('Локальная часть заканчивается тире')
    def test_25(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'aaqwertyui-@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('aaqwertyui-@mail.ru')
        Checking.check_statuscode(result, 422)

    @allure.description('Доменная часть начинается  с тире')
    def test_26(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwertyui@-mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('qwertyui@-mail.ru')
        Checking.check_statuscode(result, 422)

    @allure.description('Доменная часть заканчивается тире')
    def test_27(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'qwertyui@mail-.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user('qwertyui@mail-.ru')
        Checking.check_statuscode(result, 422)

    @allure.description('Пустое поле')
    def test_28(self):
        """Регистрация"""
        result = AuthMethods.registration(
            '',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Существующий email')
    def test_29(self):
        """Регистрация"""
        result = AuthMethods.registration(
            'y.pawel_test1@mail.ru',
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 400)

    @allure.description('Null')
    def test_29(self):
        """Регистрация"""
        result = AuthMethods.registration(
            None,
            password, last_name, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

