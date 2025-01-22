import allure
import pytest

from Currency.methods.payloads import CurrencyPayloads
from Currency.methods.currency_methods import CurrencyMethods
from common_methods.checking import Checking


@pytest.mark.Currency
@allure.epic('Post/api/v1/currency - Создание валюты - Проверка поля full_title')
class TestPostCurrencyFullTitle:

    @allure.description('Проверка поля full_title - 8 символов')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(50, 'Name_cur', 'N', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['full_title'] == 'Name_cur'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - 19 символов')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            50, 'Name_curName_curqwe', 'N', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['full_title'] == 'Name_curName_curqwe'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - 20 символов')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            50, 'Name_curName_curqwer', 'N', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['full_title'] == 'Name_curName_curqwer'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Цифры')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            50, '1234567890', 'N', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['full_title'] == '1234567890'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Кириллица')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            50, 'цукенцукен', 'N', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['full_title'] == 'цукенцукен'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Латиница')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            50, 'qwertyqwerty', 'N', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['full_title'] == 'qwertyqwerty'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Пробел')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            50, 'qqwert y', 'N', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['full_title'] == 'qqwert y'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Нижнее подчеркивание')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            50, 'qqwert_y', 'N', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['full_title'] == 'qqwert_y'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Кириллица + Латиница + цифры')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            50, 'фывqer123', 'N', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['full_title'] == 'фывqer123'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Точка')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            50, 'qqwert.y', 'N', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['full_title'] == 'qqwert.y'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Null')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            50, None, 'N', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля full_title - Уже существующее значение')
    def test_12(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            50, 'Russian ruble', 'N', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля full_title - 7 символов')
    def test_13(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            50, 'Russian', 'N', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля full_title - 21 символ')
    def test_14(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            50, 'qqqqqqqqqqwwwwwwwwwwe', 'N', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля full_title - Спецсимволы')
    def test_15(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            50, '!@#$%^&', 'N', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля full_title - Пустое поле')
    def test_16(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            50, '', 'N', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля full_title - Неверный тип данных integer')
    def test_17(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            50, 1234567, 'N', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля full_title - Поле отсутствует')
    def test_18(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency_without_full_title(
            50, 'N', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)


