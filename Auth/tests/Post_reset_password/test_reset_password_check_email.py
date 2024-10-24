import time
import allure
from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking

email = 'pawel_test_1@rambler.ru'
password = 'Ohranatruda@1'
phone = '89260000002'


@allure.epic('Post/reset_password Проверка поля email')
class TestResetPasswordCheckEmail:

    @allure.description('email адрес запроса кода и email при проверке пароля совпадают')
    def test_01(self):
        """Запрос кода"""
        time.sleep(61)
        result = AuthMethods.forgot_password(None, email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(None, email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)

        """Изменение пароля"""
        result_change = AuthMethods.reset_password(None, email, password)
        Checking.check_statuscode(result_change, 200)

    @allure.description('Поле отсутствует')
    def test_02(self):
        """Запрос кода"""
        time.sleep(61)
        result = AuthMethods.forgot_password(phone, None)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(phone, None, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)

        """Изменение пароля"""
        result_change = AuthMethods.reset_password_without_email(phone, password)
        Checking.check_statuscode(result_change, 200)

    @allure.description('Null')
    def test_03(self):
        """Запрос кода"""
        time.sleep(61)
        result = AuthMethods.forgot_password(phone, None)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(phone, None, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)

        """Изменение пароля"""
        result_change = AuthMethods.reset_password(phone, None, password)
        Checking.check_statuscode(result_change, 200)

    @allure.description('email адрес запроса кода и email при проверке пароля не совпадают')
    def test_04(self):
        """Запрос кода"""
        time.sleep(61)
        result = AuthMethods.forgot_password(None, email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(None, email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)

        """Изменение пароля"""
        result_change = AuthMethods.reset_password(None, 'y.pawel_test1@mail.ru', password)
        Checking.check_statuscode(result_change, 404)

    @allure.description('Неверный формат email')
    def test_05(self):
        """Запрос кода"""
        time.sleep(61)
        result = AuthMethods.forgot_password(None, email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(None, email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)

        """Изменение пароля"""
        result_change = AuthMethods.reset_password(None, 'pawel_test_1rambler.ru', password)
        Checking.check_statuscode(result_change, 422)

    @allure.description('Пустое поле')
    def test_06(self):
        """Запрос кода"""
        time.sleep(61)
        result = AuthMethods.forgot_password(None, email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(None, email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)

        """Изменение пароля"""
        result_change = AuthMethods.reset_password(None, '', password)
        Checking.check_statuscode(result_change, 422)


