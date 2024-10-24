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


@allure.epic('Post/registration Проверка поля middle name')
class TestRegistrationMiddlenameField:

    @allure.description('4 символа')
    def test_01(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, 'Aaaa', phone, date_of_birth
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
                "middle_name": 'Aaaa',
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
            assert result_db[3] == 'Aaaa', f'Неверное значение в поле middle_name'
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

    @allure.description('5 символов')
    def test_02(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, 'Aaaaa', phone, date_of_birth
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
                "middle_name": 'Aaaaa',
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
            assert result_db[3] == 'Aaaaa', f'Неверное значение в поле middle_name'
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
            email, password, last_name, first_name, 'Ффффф', phone, date_of_birth
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
                "middle_name": 'Ффффф',
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
            assert result_db[3] == 'Ффффф', f'Неверное значение в поле middle_name'
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
            email, password, last_name, first_name, 'Aaaaaa', phone, date_of_birth
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
                "middle_name": 'Aaaaaa',
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
            assert result_db[3] == 'Aaaaaa', f'Неверное значение в поле middle_name'
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
            first_name,
            'AaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqwww',
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
                "first_name": first_name,
                "middle_name": 'AaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqwww',
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
            assert result_db[3] == 'AaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqwww', \
                f'Неверное значение в поле middle_name'
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
            first_name,
            'AaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqwwww',
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
                "first_name": first_name,
                "middle_name": 'AaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqwwww',
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
            assert result_db[3] == 'AaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqwwww', \
                f'Неверное значение в поле middle_name'
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
            first_name,
            'Aaaaa A',
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
                "first_name": first_name,
                "middle_name": 'Aaaaa A',
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
            assert result_db[3] == 'Aaaaa A', f'Неверное значение в поле middle_name'
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
            first_name,
            'Aaaaa-A',
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
                "first_name": first_name,
                "middle_name": 'Aaaaa-A',
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
            assert result_db[3] == 'Aaaaa-A', f'Неверное значение в поле middle_name'
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
            first_name,
            'ВВВВВ',
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
                "first_name": first_name,
                "middle_name": 'ВВВВВ',
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
            assert result_db[3] == 'ВВВВВ', f'Неверное значение в поле middle_name'
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
            first_name,
            'ввввв',
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
                "first_name": first_name,
                "middle_name": 'ввввв',
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
            assert result_db[3] == 'ввввв', f'Неверное значение в поле middle_name'
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
            first_name,
            'Вввввв',
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
                "first_name": first_name,
                "middle_name": 'Вввввв',
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
            assert result_db[3] == 'Вввввв', f'Неверное значение в поле middle_name'
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
            first_name,
            'Ввввв  В',
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
                "first_name": first_name,
                "middle_name": 'Ввввв В',
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
            assert result_db[3] == 'Ввввв В', f'Неверное значение в поле middle_name'
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
            first_name,
            'Ввввв--В',
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
                "first_name": first_name,
                "middle_name": 'Ввввв-В',
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
            assert result_db[3] == 'Ввввв-В', f'Неверное значение в поле middle_name'
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

    @allure.description('Поле отсутствует')
    def test_14(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            '',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('65 Символов')
    def test_15(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            'ФффффффффйФффффффффйФффффффффйФффффффффйФффффффффйФффффффффйууууу',
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
            first_name,
            'Ффффaaa',
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
            first_name,
            'Ввввв   В',
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
                "first_name": first_name,
                "middle_name": 'Ввввв В',
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
            assert result_db[3] == 'Ввввв В', f'Неверное значение в поле middle_name'
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
            first_name,
            'Ввввв---В',
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
                "first_name": first_name,
                "middle_name": 'Ввввв-В',
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
            assert result_db[3] == 'Ввввв-В', f'Неверное значение в поле middle_name'
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
            first_name,
            '0123456',
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('Спецсимволы')
    def test_20(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            '@#$%^',
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
    def test_22(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            ' Aaaaa',
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
    def test_23(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            'Aaaaa ',
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
    def test_24(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            '-Aaaaa',
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
            first_name,
            'Aaaaa-',
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
    def test_25(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            last_name,
            first_name,
            None,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)
