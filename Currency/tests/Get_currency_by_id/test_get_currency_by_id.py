import allure
from Currency.methods.payloads import CurrencyPayloads
from Currency.methods.currency_methods import CurrencyMethods
from common_methods.checking import Checking


@allure.epic('Get/api/v1/currency/{currency}/ - Получение информации о валюте по id')
class TestGetCurrencyById:

    @allure.description('Получение информации о валюте по id - Существующее значение')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(5, 'Name_currency', 'N', access_token)
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        currency_id = data['data']['id']
        print(currency_id)
        try:
            """Запрос информации о валюте"""
            result_get = CurrencyMethods.get_currency_by_id(currency_id, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка значений"""
            data = Checking.get_data(result_create)
            id_currency = data['data']['id']
            assert id_currency == currency_id
            assert data['data']['code'] == 5
            assert data['data']['full_title'] == 'Name_currency'
            assert data['data']['short_title'] == 'N'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Получение информации о валюте по id - несуществующее значение')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос информации о валюте"""
        result_get = CurrencyMethods.get_currency_by_id(1000, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 404)

    @allure.description('Получение информации о валюте по id - Значение = 0')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос информации о валюте"""
        result_get = CurrencyMethods.get_currency_by_id(0, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Получение информации о валюте по id - Отрицательное значение')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос информации о валюте"""
        result_get = CurrencyMethods.get_currency_by_id(-2, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Получение информации о валюте по id - Null')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос информации о валюте"""
        result_get = CurrencyMethods.get_currency_by_id(None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)



