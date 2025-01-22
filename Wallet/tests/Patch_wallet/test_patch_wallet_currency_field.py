import allure
import pytest

from common_methods.checking import Checking
from Wallet.methods.wallet_methods import WalletMethods

@pytest.mark.Wallet
@allure.epic('Patch/api/v1/wallet/{wallet_id}/ Редактирование кошелька - Проверка поля currency_id')
class TestPatchWalletCurrencyId:

    @allure.description('Проверка поля currency_id - Изменение на несуществующий id')
    def test_01(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на изменение"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            wallet_id, 90, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('Проверка поля currency_id - Поле отсутствует')
    def test_02(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на изменение"""
        result = WalletMethods.change_wallet_by_id_only_name_field(
            wallet_id, 'ww', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Проверка поля currency_id - Пустое поле')
    def test_03(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на изменение"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            wallet_id, '', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля currency_id - Null')
    def test_04(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на изменение"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            wallet_id, '', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля currency_id - Изменение на существующий id')
    def test_05(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на изменение"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            wallet_id, 2, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения поля"""
        data = Checking.get_data(result)
        assert data['data']['currency_id'] == 2

    @allure.description('Проверка поля currency_id - id = 0')
    def test_06(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на изменение"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            wallet_id, 0, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля currency_id - Неверный тип данных')
    def test_07(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на изменение"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            wallet_id, 'string', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля currency_id - Вещественное число')
    def test_08(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на изменение"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            wallet_id, 2.5, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля currency_id - Спецсимволы')
    def test_09(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на изменение"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            wallet_id, '!@#$%^', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля currency_id - Отрицательный id')
    def test_10(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на изменение"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            wallet_id, -1, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 405)
