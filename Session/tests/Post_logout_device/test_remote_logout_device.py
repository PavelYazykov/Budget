import allure
from common_methods.http_methods import HttpMethods
from Session.methods.sessions_methods import SessionsMethods
from common_methods.auth import Auth
from common_methods.checking import Checking


@allure.epic('Post/ remote_logout/device_id Отзыв refresh_token по device_id')
class TestRemoteLogoutDeviceId:

    @allure.description('Отзыв refresh_token с валидными данными')
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
        result = SessionsMethods.remote_logout('22222', access_token)
        Checking.check_statuscode(result, 204)

    @allure.description('Несуществующий device_id')
    def test_02(self, auth_fixture):

        """Автоирзация"""
        access_token = auth_fixture

        """Запрос на отзыв refresh token"""
        result = SessionsMethods.remote_logout('22222', access_token)
        Checking.check_statuscode(result, 403)

    @allure.description('Поле отсутствует')
    def test_03(self, auth_fixture):
        """Автоирзация"""
        access_token = auth_fixture

        """Запрос на отзыв refresh token"""
        result = SessionsMethods.remote_logout_without_device(access_token)
        Checking.check_statuscode(result, 404)

    @allure.description('Пустое поле')
    def test_04(self, auth_fixture):
        """Автоирзация"""
        access_token = auth_fixture

        """Запрос на отзыв refresh token"""
        result = SessionsMethods.remote_logout('', access_token)
        Checking.check_statuscode(result, 404)

    @allure.description('Null')
    def test_05(self, auth_fixture):
        """Автоирзация"""
        access_token = auth_fixture

        """Запрос на отзыв refresh token"""
        result = SessionsMethods.remote_logout(None, access_token)
        Checking.check_statuscode(result, 422)

    @allure.description('device_id чужого пользователя')
    def test_06(self, auth_fixture):
        """Автоирзация"""
        access_token = auth_fixture
        another_user_auth = Auth.auth_with_params(
            '222222',
            'username=pawel_test_1@rambler.ru&password=Ohranatruda@2'
        )
        """Проверка статус кода"""
        Checking.check_statuscode(another_user_auth, 200)

        """Запрос на отзыв refresh token"""
        result = SessionsMethods.remote_logout('222222', access_token)
        Checking.check_statuscode(result, 403)

