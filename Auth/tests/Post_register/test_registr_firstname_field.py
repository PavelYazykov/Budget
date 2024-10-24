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


@allure.epic('Post/registration Проверка поля firstname')
class TestRegistrationFirstnameField:

    @allure.description('1 символ')
    def test_01(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, 'A', middle_name, phone, date_of_birth
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
                "first_name": 'A',
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
            assert result_db[2] == 'A', f'Неверное значение в поле first_name'
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

    @allure.description('2 символa')
    def test_02(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, 'Aa', middle_name, phone, date_of_birth
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
                "first_name": 'Aa',
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
            assert result_db[2] == 'Aa', f'Неверное значение в поле first_name'
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

    @allure.description('Кириллица')
    def test_03(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, 'йцукен', middle_name, phone, date_of_birth
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
                "first_name": 'йцукен',
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
            assert result_db[2] == 'йцукен', f'Неверное значение в поле first_name'
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

    @allure.description('Латиница')
    def test_04(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, 'qwert', middle_name, phone, date_of_birth
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
                "first_name": 'qwert',
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
            assert result_db[2] == 'qwert', f'Неверное значение в поле first_name'
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

    @allure.description('63 символа')
    def test_05(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            'AaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqwww',
            middle_name,
            phone,
            date_of_birth
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
                "first_name": 'AaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqwww',
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
            assert result_db[2] == 'AaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqwww', \
                f'Неверное значение в поле first_name'
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

    @allure.description('64 символа')
    def test_06(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            'AaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqwwww',
            middle_name,
            phone,
            date_of_birth
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
                "first_name": 'AaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqwwww',
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
            assert result_db[2] == 'AaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqwwww', \
                f'Неверное значение в поле first_name'
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

    @allure.description('Пробел')
    def test_07(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            'Aaa Q',
            middle_name,
            phone,
            date_of_birth
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
                "first_name": 'Aaa Q',
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
            assert result_db[2] == 'Aaa Q', f'Неверное значение в поле first_name'
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

    @allure.description('Тире')
    def test_08(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            'Aaa-Q',
            middle_name,
            phone,
            date_of_birth
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
                "first_name": 'Aaa-Q',
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
            assert result_db[2] == 'Aaa-Q', f'Неверное значение в поле first_name'
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

    @allure.description('Текст в верхнем регистре')
    def test_09(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            'AQQ',
            middle_name,
            phone,
            date_of_birth
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
                "first_name": 'AQQ',
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
            assert result_db[2] == 'AQQ', f'Неверное значение в поле first_name'
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

    @allure.description('Текст в нижнем регистре')
    def test_10(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            'asdf',
            middle_name,
            phone,
            date_of_birth
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
                "first_name": 'Asdf',
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
            assert result_db[2] == 'Asdf', f'Неверное значение в поле first_name'
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

    @allure.description('Текст в верхнем и нижнем регистре')
    def test_11(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            'Asdf',
            middle_name,
            phone,
            date_of_birth
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
                "first_name": 'Asdf',
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
            assert result_db[2] == 'Asdf', f'Неверное значение в поле first_name'
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

    @allure.description('2 пробела подряд')
    def test_12(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            'A  sdf',
            middle_name,
            phone,
            date_of_birth
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
                "first_name": 'A Sdf',
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
            assert result_db[2] == 'A Sdf', f'Неверное значение в поле first_name'
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

    @allure.description('2 тире подряд')
    def test_13(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            'A--sdf',
            middle_name,
            phone,
            date_of_birth
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
                "first_name": 'A-sdf',
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
            assert result_db[2] == 'A-sdf', f'Неверное значение в поле first_name'
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

    @allure.description('Пустое поле')
    def test_14(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            '',
            middle_name,
            phone,
            date_of_birth
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
                "first_name": '',
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
            assert result_db[2] == '', f'Неверное значение в поле first_name'
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

    @allure.description('65 Символов')
    def test_15(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            'AaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqwwwww',
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('Латиница + Кириллица')
    def test_16(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            'Asdфвв',
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('3 пробела подряд')
    def test_17(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            'A   sdf',
            middle_name,
            phone,
            date_of_birth
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
                "first_name": 'A Sdf',
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
            assert result_db[2] == 'A Sdf', f'Неверное значение в поле first_name'
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

    @allure.description('3 тире подряд')
    def test_18(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            'A---sdf',
            middle_name,
            phone,
            date_of_birth
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
                "first_name": 'A---sdf',
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
            assert result_db[2] == 'A---sdf', f'Неверное значение в поле first_name'
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

    @allure.description('Цифры')
    def test_19(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            '12345678',
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('Спецсимволы:')
    def test_20(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            '@#$%^',
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('Начинается пробелом')
    def test_21(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            ' Asdf',
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('Заканчивается пробелом')
    def test_22(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            'Asdf ',
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('Начинается с "тире"')
    def test_23(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            '-Asdf',
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('Заканчивается "тире"')
    def test_24(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            'Asdf-',
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('Null')
    def test_24(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            None,
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)



