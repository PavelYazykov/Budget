import json
import time
import allure
from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking

email = 'qaa@mail.ru'
password = 'Samsung@9@9@9'
last_name = 'Иванов'
first_name = 'Иван'
middle_name = 'Иванович'
phone = '89261111100'
date_of_birth = '2000-01-01'


@allure.epic('Post/registration Общие проверки')
class TestRegistrationCommonCheck:

    @allure.description('Регистрация пользователя с валидными данными')
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

    @allure.description('Запрос без body')
    def test_02(self):
        """Регистрация"""
        result = AuthMethods.registration_without_body()

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)


