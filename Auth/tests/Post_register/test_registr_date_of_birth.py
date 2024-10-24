import allure
from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking, AuthUser
from Auth.methods.payloads import Payloads

email = 'qa@mail.ru'
password = 'Samsung@9@9@9'
last_name = 'Иванов'
first_name = 'Иван'
middle_name = 'Иванович'
phone = '89261111111'
date_of_birth = '2000-01-01'


@allure.epic('Post/registration Проверка поля date of birth')
class TestRegistrationDate:

    @allure.description('Валидная дата')
    def test_01(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, last_name, first_name, middle_name, phone, '2000-01-01'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            check_required_fields = AuthUser()
            data, user_id = AuthMethods.get_id(result)

            """Проверка значений обязательных полей"""
            check_fields = Payloads.required_fields_value(
                email, last_name, first_name, middle_name, phone, '2000-01-01', data
            )

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
