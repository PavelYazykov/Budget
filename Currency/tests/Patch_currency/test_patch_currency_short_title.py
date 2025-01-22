import allure
import pytest

from Currency.methods.currency_methods import CurrencyMethods
from common_methods.checking import Checking


@pytest.mark.Currency
@allure.epic('Patch/api/v1/currency/{currency}/ - Проверка поля short_title')
class TestPatchCurrencyShortTitle:

    @allure.description('Проверка поля short_title - 1 символ')
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
                currency_id, 6, 'Name_currency', 'R', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['short_title'] == 'R'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - 5 символов')
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
                currency_id, 6, 'Name_currency', 'Rrrrr', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['short_title'] == 'Rrrrr'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Цифры')
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
                currency_id, 6, 'Name_currency', '123', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['short_title'] == '123'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Кириллица')
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
                currency_id, 6, 'Name_currency', 'К', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['short_title'] == 'К'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Латиница')
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
                currency_id, 6, 'Name_currency', 'R', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['short_title'] == 'R'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Пробел')
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
                currency_id, 6, 'Name_currency', 'R r', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)

        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Нижнее подчеркивание')
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
                currency_id, 6, 'Name_currency', 'R_r', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['short_title'] == 'R_r'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Кириллица + Латиница + цифры')
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
                currency_id, 6, 'Name_currency', 'Rк1', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['short_title'] == 'Rк1'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Точка')
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
                currency_id, 6, 'Name_currency', 'R.r', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['short_title'] == 'R.r'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Поле отсутствует')
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
            result_change = CurrencyMethods.change_currency_wt_short_title(
                currency_id, 6, 'Name_cur', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 200)

            """Проверка значений"""
            data_new = Checking.get_data(result_change)
            assert data_new['data']['full_title'] == 'Name_cur'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Null')
    def test_11(self, auth_fixture):
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
                currency_id, 6, 'Name_currency', None, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)

        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Уже существующее значение')
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
                currency_id, 6, 'Name_currency', 'RUB', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)

        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - 6 символов')
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
                currency_id, 6, 'Name_currency', 'RUBRUB', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)

        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Спецсимволы')
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
                currency_id, 6, 'Name_currency', '@#$%', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)

        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Пустое поле')
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
                currency_id, 6, 'Name_currency', '', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)

        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля short_title - Неверный тип данных integer')
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
                currency_id, 6, 'Name_currency', 123, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 422)

        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)



