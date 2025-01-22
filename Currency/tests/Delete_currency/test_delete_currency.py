import allure
import pytest

from Currency.methods.payloads import CurrencyPayloads
from Currency.methods.currency_methods import CurrencyMethods
from common_methods.checking import Checking


@pytest.mark.Currency
@allure.epic('Delete/api/v1/currency - Удаление валюты')
class TestDeleteCurrency:

    @allure.description('Удаление существующей валюты')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(5, 'Name_currency', 'N', access_token)
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        currency_id = data['data']['id']
        print(currency_id)

        """Удаление валюты"""
        result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
        Checking.check_statuscode(result_delete, 204)

    @allure.description('Удаление несуществующей валюты')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(5, 'Name_currency', 'N', access_token)
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        currency_id = data['data']['id']
        print(currency_id)

        """Удаление валюты"""
        result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
        Checking.check_statuscode(result_delete, 204)

        """Повторное удаление валюты"""
        result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
        Checking.check_statuscode(result_delete, 404)

    @allure.description('Удаление валюты - Значение id валюты = 0')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление валюты"""
        result_delete = CurrencyMethods.delete_currency(0, access_token)
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление валюты - Отрицательное значение id валюты')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление валюты"""
        result_delete = CurrencyMethods.delete_currency(-2, access_token)
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление валюты - Значение id - пустое поле')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление валюты"""
        result_delete = CurrencyMethods.delete_currency('', access_token)
        Checking.check_statuscode(result_delete, 405)

    @allure.description('Удаление валюты - Поле id отсутствует')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление валюты"""
        result_delete = CurrencyMethods.delete_currency_wt_currency_id(access_token)
        Checking.check_statuscode(result_delete, 405)

    @allure.description('Удаление валюты - Null')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление валюты"""
        result_delete = CurrencyMethods.delete_currency(None, access_token)
        Checking.check_statuscode(result_delete, 422)
