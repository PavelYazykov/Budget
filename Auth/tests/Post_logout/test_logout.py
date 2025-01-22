import json

import allure
import pytest

from common_methods.variables import AuthVariables
from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
from common_methods.auth import Auth
payloads = AuthVariables.auth_payloads


@pytest.mark.Auth
@allure.epic('Post_reset_password/logout Отзвы refresh_token')
class TestLogout:

    @allure.description('Отзыв refresh_token')
    def test_01(self):

        """Авторизация"""
        auth_result = Auth.auth()

        """Получение refresh_token"""
        refresh_token = AuthMethods.get_refresh_token(auth_result)

        """Запрос на отзыв refresh_token"""
        result = AuthMethods.logout(
            refresh_token, payloads
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 204)

    @allure.description('Неверный refresh_token')
    def test_02(self):

        """Запрос на отзыв refresh_token"""
        result = AuthMethods.logout(
            'jghkgkjrbgkbrkgbksbgkgbkjsbgjk',
            payloads
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 401)

