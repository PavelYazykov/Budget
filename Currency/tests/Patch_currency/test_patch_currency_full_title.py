import allure
import pytest

from Currency.methods.currency_methods import CurrencyMethods
from common_methods.checking import Checking


@pytest.mark.Currency
@allure.epic('Patch/api/v1/currency/{currency}/ - Проверка поля full_title')
class TestPatchCurrencyFullTitle:

    @allure.description('Проверка поля full_title - 8 символов')
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
                currency_id, 6, 'Namename', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['full_title'] == 'Namename'
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - 20 символов')
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
                currency_id, 6, 'Namename12Namename12', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['full_title'] == 'Namename12Namename12'
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Цифры')
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
                currency_id, 6, '123456789', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['full_title'] == '123456789'
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Кириллица')
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
                currency_id, 6, 'Кириллица', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['full_title'] == 'Кириллица'
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Латиница')
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
                currency_id, 6, 'Namename', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['full_title'] == 'Namename'
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Пробел')
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
                currency_id, 6, 'Name name', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['full_title'] == 'Name name'
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Нижнее подчеркивание')
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
            result_change = CurrencyMethods.change_currency(
                currency_id, 6, 'Name_name', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['full_title'] == 'Name_name'
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Кириллица + Латиница + цифры')
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
                currency_id, 6, 'Name12345йц', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['full_title'] == 'Name12345йц'
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Точка')
    def test_09(self, auth_fixture):
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
                currency_id, 6, 'NameName.q', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['full_title'] == 'NameName.q'
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Null')
    def test_10(self, auth_fixture):
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
                currency_id, 6, None, 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Уже существующее значение')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(666, 'Name_currency', 'N', access_token)
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        currency_id = data['data']['id']
        print(currency_id)

        """Запрос на создание второй  валюты"""
        result_create_2 = CurrencyMethods.create_currency(555, 'Name_currency_2', 'ETH', access_token)
        Checking.check_statuscode(result_create, 201)
        data_2 = Checking.get_data(result_create_2)
        currency_id_2 = data_2['data']['id']
        print(currency_id_2)
        try:
            """Запрос на редактрование информации о валюте"""
            result_change = CurrencyMethods.change_currency(
                currency_id, 6, 'Name_currency_2', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)
            """Удаление второй валюты"""
            result_delete_2 = CurrencyMethods.delete_currency(currency_id_2, access_token)
            Checking.check_statuscode(result_delete_2, 204)

    @allure.description('Проверка поля full_title - 7 символов')
    def test_12(self, auth_fixture):
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
                currency_id, 6, 'Russian', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - 21 символ')
    def test_13(self, auth_fixture):
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
                currency_id, 6, 'Name_curreName_curreq', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Спецсимволы')
    def test_14(self, auth_fixture):
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
                currency_id, 6, '@#$%^&*@#$%^&', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Пустое поле')
    def test_15(self, auth_fixture):
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
                currency_id, 6, '', 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Неверный тип данных integer')
    def test_16(self, auth_fixture):
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
                currency_id, 6, 1234567890, 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля full_title - Поле отсутствует')
    def test_17(self, auth_fixture):
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
            result_change = CurrencyMethods.change_currency_wt_full_title(
                currency_id, 6, 'NC', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)