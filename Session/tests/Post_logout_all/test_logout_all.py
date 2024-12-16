import allure
from common_methods.auth import Auth
from common_methods.checking import Checking
from Session.methods.sessions_methods import SessionsMethods


@allure.description('Отзыв всех refresh_token, кроме переданного устройства')
class TestLogoutAll:

    @allure.description('Отзыв всех refresh_token, кроме переданного устройства(валидные данные)')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture
        result_auth_1 = Auth.auth_with_params(
            '22222',
            'username=y.pawel_test1%40mail.ru&password=Ohranatruda%401'
        )
        Checking.check_statuscode(result_auth_1, 200)
        result_auth_2 = Auth.auth_with_params(
            '33333',
            'username=y.pawel_test1%40mail.ru&password=Ohranatruda%401'
        )
        Checking.check_statuscode(result_auth_2, 200)

        """Запрос на отзыв refresh token"""
        result = SessionsMethods.logout_all('11111', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 204)

    @allure.description('Проверка поля except_device - Несуществующий device_id')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на отзыв refresh token"""
        result = SessionsMethods.logout_all('000001', access_token)
        Checking.check_statuscode(result, 403)

    @allure.description('Пуcтое поле')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на отзыв refresh token"""
        result = SessionsMethods.logout_all('', access_token)
        Checking.check_statuscode(result, 422)

    @allure.description('Поле отсутствует')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на отзыв refresh token"""
        result = SessionsMethods.logout_all_without_device(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Null')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на отзыв refresh token"""
        result = SessionsMethods.logout_all(None, access_token)
        Checking.check_statuscode(result, 422)

