import allure
from Currency.methods.payloads import CurrencyPayloads
from Currency.methods.currency_methods import CurrencyMethods
from common_methods.checking import Checking


@allure.epic('Post/api/v1/currency - Создание валюты - Проверка поля code')
class TestPostCurrencyCode:

    @allure.description('Проверка поля code - Значение не занятая цифра')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(1000, 'Name_currency', 'N', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значения"""
            data = Checking.get_data(result_create)
            assert data['data']['code'] == 1000
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            data = Checking.get_data(result_create)
            currency_id = data['data']['id']
            print(currency_id)
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    # @allure.description('Проверка поля code - Значение не занятая цифра')
    # def test_02(self, auth_fixture):
    #     """Авторизация"""
    #     access_token = auth_fixture
    #
    #     """Запрос на создание валюты"""
    #     result_create = CurrencyMethods.create_currency(2, 'Name_currency', 'N', access_token)
    #
    #     """Проверка статус кода"""
    #     Checking.check_statuscode(result_create, 422)
    #     print(result_create.text)

    @allure.description('Проверка поля code - Вещественное число')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(1.1, 'Name_currency', 'N', access_token)

        """Проверка статус кода"""
        if result_create.status_code == 201:
            CurrencyMethods.delete_currency_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля code - Отрицательное значение')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(-1, 'Name_currency', 'N', access_token)

        """Проверка статус кода"""
        if result_create.status_code == 201:
            CurrencyMethods.delete_currency_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля code - Неверный тип данных string')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            'string', 'Name_currency', 'N', access_token
        )

        """Проверка статус кода"""
        if result_create.status_code == 201:
            CurrencyMethods.delete_currency_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля code - Пустое поле')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            '', 'Name_currency', 'N', access_token
        )

        """Проверка статус кода"""
        if result_create.status_code == 201:
            CurrencyMethods.delete_currency_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля code - Поле отсутствует')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency_without_code(
            'Name_currency', 'N', access_token
        )

        """Проверка статус кода"""
        if result_create.status_code == 201:
            CurrencyMethods.delete_currency_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля code - Null')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(
            None, 'Name_currency', 'N', access_token
        )

        """Проверка статус кода"""
        if result_create.status_code == 201:
            CurrencyMethods.delete_currency_if_bug(result_create, access_token)
        Checking.check_statuscode(result_create, 422)





