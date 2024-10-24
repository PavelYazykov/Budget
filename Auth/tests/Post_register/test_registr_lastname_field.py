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


@allure.epic('Post/registration Проверка поля lastname')
class TestRegistrationLastnameField:

    @allure.description('1 символ')
    def test_01(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Z', first_name, middle_name, phone, date_of_birth
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
                "last_name": 'Z',
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
            assert result_db[1] == 'Z', f'Неверное значение в поле last_name'
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

    @allure.description('2 символа')
    def test_02(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Zz', first_name, middle_name, phone, date_of_birth
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
                "last_name": 'Zz',
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
            assert result_db[1] == 'Zz', f'Неверное значение в поле last_name'
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

    @allure.description('Кириллица')
    def test_03(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Ффф', first_name, middle_name, phone, date_of_birth
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
                "last_name": 'Ффф',
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
            assert result_db[1] == 'Ффф', f'Неверное значение в поле last_name'
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

    @allure.description('Латиница')
    def test_04(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Aaa', first_name, middle_name, phone, date_of_birth
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
                "last_name": 'Aaa',
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
            assert result_db[1] == 'Aaa', f'Неверное значение в поле last_name'
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

    @allure.description('63 символа')
    def test_05(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            'Automationautomationautomationautomationautomationautomationasd',
            first_name,
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
                "last_name": 'Automationautomationautomationautomationautomationautomationasd',
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
            assert result_db[1] == 'Automationautomationautomationautomationautomationautomationasd'\
                , f'Неверное значение в поле last_name'
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

    @allure.description('64 символа')
    def test_06(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            'Automationautomationautomationautomationautomationautomationasdd',
            first_name,
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
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
                "last_name": 'Automationautomationautomationautomationautomationautomationasdd',
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
            assert result_db[1] == 'Automationautomationautomationautomationautomationautomationasdd' \
                , f'Неверное значение в поле last_name'
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

    @allure.description('Пробел')
    def test_07(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            'Automation Aut',
            first_name,
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
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
                "last_name": 'Automation Aut',
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
            assert result_db[1] == 'Automation Aut', f'Неверное значение в поле last_name'
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

    @allure.description('Тире')
    def test_08(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Фф-ф', first_name, middle_name, phone, date_of_birth
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
                "last_name": 'Фф-ф',
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
            assert result_db[1] == 'Фф-ф', f'Неверное значение в поле last_name'
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

    @allure.description('Текст в верхнем регистре')
    def test_09(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'QQQ', first_name, middle_name, phone, date_of_birth
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
                "last_name": 'QQQ',
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
            assert result_db[1] == 'QQQ', f'Неверное значение в поле last_name'
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

    @allure.description('Текст в нижнем регистре')
    def test_10(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'йййй', first_name, middle_name, phone, date_of_birth
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
                "last_name": 'Йййй',
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
            assert result_db[1] == 'Йййй', f'Неверное значение в поле last_name'
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

    @allure.description('Текст в верхнем и нижнем регистре')
    def test_11(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Фйййй', first_name, middle_name, phone, date_of_birth
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
                "last_name": 'Фйййй',
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
            assert result_db[1] == 'Фйййй', f'Неверное значение в поле last_name'
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

    @allure.description('2 пробела подряд')
    def test_12(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Фййй  й', first_name, middle_name, phone, date_of_birth
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
                "last_name": 'Фййй  Й',
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
            assert result_db[1] == 'Фййй  Й', f'Неверное значение в поле last_name'
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

    @allure.description('2 тире подряд')
    def test_13(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Фййй--й', first_name, middle_name, phone, date_of_birth
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
                "last_name": 'Фййй-й',
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
            assert result_db[1] == 'Фййй-й', f'Неверное значение в поле last_name'
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

    @allure.description('Пустое поле')
    def test_14(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, '', first_name, middle_name, phone, date_of_birth
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
            'AaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqzxcvb',
            first_name,
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
            email, password, 'AAAфффф', first_name, middle_name, phone, date_of_birth
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
            email, password, 'Фййй   Й', first_name, middle_name, phone, date_of_birth
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
                "last_name": 'Фййй   Й',
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
            assert result_db[1] == 'Фййй   й', f'Неверное значение в поле last_name'
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

    @allure.description('3 тире подряд')
    def test_18(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Фййй---й', first_name, middle_name, phone, date_of_birth
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
                "last_name": 'Фййй-й',
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
            assert result_db[1] == 'Фййй-й', f'Неверное значение в поле last_name'
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

    @allure.description('Цифры')
    def test_19(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, '0123456', first_name, middle_name, phone, date_of_birth
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
            email, password, '!№?%', first_name, middle_name, phone, date_of_birth
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
            email, password, ' Фывв', first_name, middle_name, phone, date_of_birth
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
            email, password, 'Фывв ', first_name, middle_name, phone, date_of_birth
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
            email, password, '-Фывв', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('Заканчивается "тире"')
    def test_23(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Фывв-', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('Null')
    def test_23(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, None, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        if result_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)
