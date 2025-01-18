import allure
from Currency.methods.payloads import CurrencyPayloads
from Currency.methods.currency_methods import CurrencyMethods
from common_methods.checking import Checking


@allure.epic('Patch/api/v1/currency/{currency}/ - Измнение информации о валюте по id - Общие проверки')
class TestPatchCurrency:

    @allure.description('Общие проверки - Измнение информации о валюте с валидными данными')
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
            assert data_new['data']['full_title'] == 'Name_name'
            assert data_new['data']['short_title'] == 'NC'
        except AssertionError:
            raise AssertionError
        finally:
            """Удаление валюты"""
            result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
            Checking.check_statuscode(result_delete, 204)
