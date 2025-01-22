import allure
import pytest

from Currency.methods.currency_methods import CurrencyMethods
from common_methods.checking import Checking


@pytest.mark.Currency
@allure.epic('Patch/api/v1/currency/{currency}/ - Измнение информации о валюте по id - Проверка поля code')
class TestPatchCurrencyCode:

    @allure.description('Проверка поля code - Значение не занятая цифра')
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
            """Запрос на редактрование информации о валюте"""
            result_change = CurrencyMethods.change_currency(
                currency_id, 6, 'Name_name', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['code'] == 6
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля code - Уже существующее значение')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(5, 'Name_currency', 'N', access_token)
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        currency_id = data['data']['id']
        print(currency_id)
        try:
            """Запрос на редактрование информации о валюте"""
            result_change = CurrencyMethods.change_currency(
                currency_id, 5, 'Name_name', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['code'] == 5
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля code - Вещественное число')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(5, 'Name_currency', 'N', access_token)
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        currency_id = data['data']['id']
        print(currency_id)
        try:
            """Запрос на редактрование информации о валюте"""
            result_change = CurrencyMethods.change_currency(
                currency_id, 3.3, 'Name_name', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля code - Отрицательное значение')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(5, 'Name_currency', 'N', access_token)
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        currency_id = data['data']['id']
        print(currency_id)
        try:
            """Запрос на редактрование информации о валюте"""
            result_change = CurrencyMethods.change_currency(
                currency_id, -3, 'Name_name', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля code - Неверный тип данных string')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(5, 'Name_currency', 'N', access_token)
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        currency_id = data['data']['id']
        print(currency_id)
        try:
            """Запрос на редактрование информации о валюте"""
            result_change = CurrencyMethods.change_currency(
                currency_id, 'string', 'Name_name', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля code - Пустое поле')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(5, 'Name_currency', 'N', access_token)
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        currency_id = data['data']['id']
        print(currency_id)
        try:
            """Запрос на редактрование информации о валюте"""
            result_change = CurrencyMethods.change_currency(
                currency_id, '', 'Name_name', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля code - Поле отсутствует')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(5, 'Name_currency', 'N', access_token)
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        currency_id = data['data']['id']
        print(currency_id)
        try:
            """Запрос на редактрование информации о валюте"""
            result_change = CurrencyMethods.change_currency_wt_code(
                currency_id, 'Name_name', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля code - Null')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(5, 'Name_currency', 'N', access_token)
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        currency_id = data['data']['id']
        print(currency_id)
        try:
            """Запрос на редактрование информации о валюте"""
            result_change = CurrencyMethods.change_currency(
                currency_id, None, 'Name_name', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)
