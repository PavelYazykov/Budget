from common_methods.http_methods import HttpMethods
from common_methods.checking import Checking
from Auth.methods.auth_methods import AuthMethods
import allure


@allure.epic('Post_reset_password/login Проверка поля device_id')
class TestCheckDeviceId:

    @allure.description('5 символов ')
    def test_01(self):
        result = AuthMethods.login(
            '11111', 'username=y.pawel_test1%40mail.ru&password=Ohranatruda%401'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('64 символа')
    def test_02(self):
        result = AuthMethods.login(
            '1111111111111111111111111111111111111111111111111111111111111111',
            'username=y.pawel_test1%40mail.ru&password=Ohranatruda%401'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('4 символа')
    def test_03(self):
        result = AuthMethods.login(
            '1111', 'username=y.pawel_test1%40mail.ru&password=Ohranatruda%401'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('65 символов')
    def test_05(self):
        result = AuthMethods.login(
            '11111111111111111111111111111111111111111111111111111111111111111',
            'username=y.pawel_test1%40mail.ru&password=Ohranatruda%401'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Пуcтое поле')
    def test_06(self):

        result = AuthMethods.login(
            '', 'username=y.pawel_test1%40mail.ru&password=Ohranatruda%401'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Поле отсутствует')
    def test_07(self):
        result = AuthMethods.login_without_device_id(
            'username=y.pawel_test1%40mail.ru&password=Ohranatruda%401'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Null')
    def test_08(self):
        result = AuthMethods.login(
            None, 'username=y.pawel_test1%40mail.ru&password=Ohranatruda%401'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)
