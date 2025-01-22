import allure
import pytest

from Currency.methods.payloads import CurrencyPayloads
from Currency.methods.currency_methods import CurrencyMethods
from common_methods.checking import Checking


@pytest.mark.Currency
@allure.epic('Post/api/v1/currency - Создание валюты - Общие проверки')
class TestPostCurrency:

    @allure.description('Создание валюты с валидными данными')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание валюты"""
        result_create = CurrencyMethods.create_currency(5, 'Name_currency', 'N', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)
        try:
            """Проверка наличия обязательных полей"""
            CurrencyPayloads.check_required_fields(result_create, CurrencyPayloads.post_payloads)

            """Проверка значений"""
            data = Checking.get_data(result_create)
            assert data['data']['code'] == 5
            assert data['data']['full_title'] == 'Name_currency'
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

