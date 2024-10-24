import time
import allure
from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking

email = 'pawel_test_1@rambler.ru'
password = 'Ohranatruda@1'
phone = '89260000002'


@allure.epic('Post/reset_password Проверка поля password')
class TestResetPassword:

    @allure.description('12 символов')
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
        result_change = AuthMethods.reset_password(None, email, 'Aa1!tyhgvooa')
        Checking.check_statuscode(result_change, 200)

    @allure.description('100 символов')
    def test_02(self):
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
        result_change = AuthMethods.reset_password(
            None, email, 'Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa'
                         '1@111111Aa1@111111Aa1@111111'
        )
        Checking.check_statuscode(result_change, 200)

    @allure.description('Пробел')
    def test_03(self):
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
        result_change = AuthMethods.reset_password(
            None, email, 'Zx@1 kjgtreqpbd'
        )
        Checking.check_statuscode(result_change, 200)

    @allure.description('Ввод предыдущего пароля')
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
        result_change = AuthMethods.reset_password(
            None, email, 'Zx@1 kjgtreqpbd'
        )
        Checking.check_statuscode(result_change, 200)

    @allure.description('11 символов')
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
        result_change = AuthMethods.reset_password(
            None, email, 'Zx@1vbytrew'
        )
        Checking.check_statuscode(result_change, 422)

    @allure.description('101 символов')
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
        result_change = AuthMethods.reset_password(
            None, email, 'Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1@111111Aa1'
                         '@111111Aa1@111111Aa1@1111112'
        )
        Checking.check_statuscode(result_change, 422)

    @allure.description('Пустое поле')
    def test_07(self):
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
        result_change = AuthMethods.reset_password(
            None, email, ''
        )
        Checking.check_statuscode(result_change, 422)

    @allure.description('Null')
    def test_08(self):
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
        result_change = AuthMethods.reset_password(
            None, email, None
        )
        Checking.check_statuscode(result_change, 422)

    @allure.description('Пароль не соответствует требованиям')
    def test_09(self):
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
        result_change = AuthMethods.reset_password(
            None, email, 'zxcvbnmghqwertyu'
        )
        Checking.check_statuscode(result_change, 422)

    @allure.description('Неверный тип данных (integer)')
    def test_09(self):
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
        result_change = AuthMethods.reset_password(
            None, email, 123456789963852741
        )
        Checking.check_statuscode(result_change, 422)

    @allure.description('Поле отсутствует')
    def test_10(self):
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
        result_change = AuthMethods.reset_password_without_password(None, email)
        Checking.check_statuscode(result_change, 422)


