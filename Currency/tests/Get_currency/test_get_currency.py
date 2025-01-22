import allure
import pytest

from Currency.methods.currency_methods import CurrencyMethods
from common_methods.checking import Checking


@pytest.mark.Currency
@allure.epic('Get/api/v1/currency - Получение списка валют')
class TestGetCurrency:

    @allure.description('Получение списка валют - Запрос списка валют (авторизованный пользователь)')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на получение списка валют"""
        result = CurrencyMethods.get_currency(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Получение списка валют - Запрос списка валют (неавторизованный пользователь)')
    def test_02(self):

        """Запрос на получение списка валют"""
        result = CurrencyMethods.get_currency_without_auth()

        """Проверка статус кода"""
        Checking.check_statuscode(result, 401)
