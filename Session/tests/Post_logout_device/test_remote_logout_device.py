import time

import allure
import pytest

from Auth.methods.auth_methods import AuthMethods
from common_methods.http_methods import HttpMethods
from Session.methods.sessions_methods import SessionsMethods
from common_methods.auth import Auth
from common_methods.checking import Checking
from common_methods.variables import AuthVariables


@pytest.mark.Session
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

        """Создание второго пользователя"""
        result_create_second_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_second_user, 201)
        data, user_id = AuthMethods.get_id(result_create_second_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Авторизация второго пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token_2 = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Запрос на отзыв refresh token"""
            result = SessionsMethods.remote_logout('11111', access_token_2)
            Checking.check_statuscode(result, 403)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)

