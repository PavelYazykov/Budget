import time
import allure
from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
from common_methods.variables import AuthVariables
email = AuthVariables.email
password = AuthVariables.password


@allure.epic('Post_reset_password/code/check Проверка поля code')
class TestCheckCodeField:

    @allure.description('Проверка поля code - Действующий код')
    def test_01(self):

        """Запрос кода на смену пароля"""
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

    @allure.description('Проверка поля code - Ввести неверный пароль 2 раза подряд и на 3 раз ввести верный пароль')
    def test_02(self):

        """Запрос кода на смену пароля"""
        result = AuthMethods.forgot_password(None, email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        for _ in range(2):
            check_code = AuthMethods.code_check(None, email, '000000')
            Checking.check_statuscode(check_code, 400)
        result_check = AuthMethods.code_check(None, email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 200)

        """Изменение пароля"""
        result_change = AuthMethods.reset_password(None, email, password)
        Checking.check_statuscode(result_change, 200)

    @allure.description('Проверка поля code - Несуществующий код')
    def test_03(self):

        """Проверка кода"""
        result_check = AuthMethods.code_check(None, email, 111111)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)

    @allure.description('Проверка поля code - Ввести неверный пароль 3 раза подряд и на 4 раз ввести верный пароль')
    def test_04(self):
        """Запрос кода на смену пароля"""
        result = AuthMethods.forgot_password(None, email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)
        print('RESULT CODE:', result_code)

        """Проверка кода"""
        for _ in range(3):
            wrong_code = AuthMethods.code_check(None, email, '000000')
            time.sleep(1)
            print('ПРОВЕРКА НЕВЕРНОГО КОДА:', wrong_code.json())
            Checking.check_statuscode(wrong_code, 400)
        result_check = AuthMethods.code_check(None, email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 404)

    @allure.description('Проверка поля code - Истекший код (более 60 сек)')
    def test_05(self):

        """Запрос кода на смену пароля"""
        result = AuthMethods.forgot_password(None, email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        time.sleep(61)
        result_check = AuthMethods.code_check(None, email, result_code)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 404)

    @allure.description('Проверка поля code - 5 символов')
    def test_06(self):

        """Проверка кода"""
        result_check = AuthMethods.code_check(None, email, 00000)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)

    @allure.description('Проверка поля code - 7 символов')
    def test_07(self):
        """Проверка кода"""
        result_check = AuthMethods.code_check(None, email, 0000000)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)

    @allure.description('Проверка поля code - Пуcтое поле')
    def test_08(self):
        """Проверка кода"""
        result_check = AuthMethods.code_check(None, email, "")

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)

    @allure.description('Проверка поля code- Поле отсутствует')
    def test_09(self):

        """Проверка кода"""
        result_check = AuthMethods.code_check_without_code(None, email)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)

    @allure.description('Null')
    def test_10(self):
        """Проверка кода"""
        result_check = AuthMethods.code_check(None, email, None)

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)

    @allure.description('Проверка поля code - Неверный тип данных integer')
    def test_11(self):

        """Запрос кода на смену пароля"""
        result = AuthMethods.forgot_password(None, email)
        Checking.check_statuscode(result, 200)
        result_code = AuthMethods.get_verify_code(result)

        """Проверка кода"""
        result_check = AuthMethods.code_check(None, email, int(result_code))

        """Проверка статус кода"""
        Checking.check_statuscode(result_check, 422)
