import allure
import pytest

from Currency.methods.payloads import CurrencyPayloads
from Currency.methods.currency_methods import CurrencyMethods
from common_methods.checking import Checking


@pytest.mark.Currency
@allure.epic('Post/api/v1/currency - Создание валюты - Проверка поля short_title')
class TestPostCurrencyShortTitle:

    @allure.description('Проверка поля short_title - 1 символ')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(50, 'Name_currency', 'N', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['short_title'] == 'N'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - 4 символа')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(50, 'Name_currency', 'Nnnn', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['short_title'] == 'Nnnn'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - 5 символов')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(50, 'Name_currency', 'Nnnnn', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['short_title'] == 'Nnnnn'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Цифры')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(50, 'Name_currency', '123', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['short_title'] == '123'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Кириллица')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(50, 'Name_currency', 'Ф', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['short_title'] == 'Ф'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Латиница')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(50, 'Name_currency', 'S', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['short_title'] == 'S'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Пробел')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(50, 'Name_currency', 's s', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля short_title - Нижнее подчеркивание')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(50, 'Name_currency', 's_s', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['short_title'] == 's_s'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Кириллица + Латиница + цифры')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(50, 'Name_currency', 'sф1', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['short_title'] == 'sф1'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Точка')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(50, 'Name_currency', 's.s', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['short_title'] == 's.s'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Null')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(50, 'Name_currency', None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля short_title - Уже существующее значение')
    def test_12(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(50, 'Name_currency', 'RUB', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля short_title - 6 символов')
    def test_13(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(50, 'Name_currency', 'RUBRUB', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля short_title - Спецсимволы')
    def test_14(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(50, 'Name_currency', 'RUBRUB', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля short_title - Пустое поле')
    def test_15(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(50, 'Name_currency', '', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля short_title - Поле отсутствует')
    def test_16(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency_without_short_title(
            50, 'Name_currency', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля short_title - Неверный тип данных integer')
    def test_17(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(50, 'Name_currency', 123, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)
