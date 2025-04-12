import json
import allure
import pytest

from common_methods.checking import Checking
from Wallet.methods.wallet_methods import WalletMethods


@pytest.mark.Wallet
@allure.epic('Post/api/v1/wallet/ - Создание счета, проверка поля amount')
class TestCreateWalletAmountField:

    @allure.description('Создание счета проверка поля amount - Создание счета со значением "0"')
    def test_01(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wallet', 2, 0, access_token
        )
        data = Checking.get_data(result)
        wallet_id = data['data']['id']

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        try:
            """Проверка значения поля amount"""
            assert data['data']['amount'] == '0.00'
        finally:
            WalletMethods.delete_wallet_sql(wallet_id)

    @allure.description('Создание счета проверка поля amount - Поле отсутствует')
    def test_02(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet_without_amount(
            'wallet', 2, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Удаление счета"""
        data = Checking.get_data(result)
        wallet_id = data['data']['id']
        WalletMethods.delete_wallet_sql(wallet_id)

    @allure.description('Создание счета проверка поля amount - Целое число')
    def test_03(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wallet', 2, 10, access_token
        )
        print(result.json())
        data = Checking.get_data(result)
        wallet_id = data['data']['id']

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        try:
            """Проверка значения поля amount"""
            assert data['data']['amount'] == '10.00'

        finally:
            WalletMethods.delete_wallet_sql(wallet_id)

    @allure.description('Создание счета проверка поля amount - Вещественное число')
    def test_04(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wallet', 2, 10.10, access_token
        )
        data = Checking.get_data(result)
        wallet_id = data['data']['id']

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        try:
            """Проверка значения поля amount"""
            assert data['data']['amount'] == '10.10'
        finally:
            WalletMethods.delete_wallet_sql(wallet_id)

    @allure.description('Создание счета проверка поля amount - Null')
    def test_05(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wallet', 2, None, access_token
        )

        """Проверка статус кода"""
        WalletMethods.delete_wallet_if_bug(result)
        Checking.check_statuscode(result, 422)

    @allure.description('Создание счета проверка поля amount - Пустое поле')
    def test_06(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wallet', 2, '', access_token
        )

        """Проверка статус кода"""
        WalletMethods.delete_wallet_if_bug(result)
        Checking.check_statuscode(result, 422)

    @allure.description('Создание счета проверка поля amount - Неверный тип данных')
    def test_07(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wallet', 2, 'string', access_token
        )

        """Проверка статус кода"""
        WalletMethods.delete_wallet_if_bug(result)
        Checking.check_statuscode(result, 422)

    @allure.description('Создание счета проверка поля amount - Отрицательное значение')
    def test_08(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wallet', 2, -10, access_token
        )

        """Проверка статус кода"""
        WalletMethods.delete_wallet_if_bug(result)
        Checking.check_statuscode(result, 422)


