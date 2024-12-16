import json
import allure
from common_methods.checking import Checking
from Wallet.methods.wallet_methods import WalletMethods


@allure.epic('Post/api/v1/wallet/  Создание счета проверка поля currency_id')
class TestCreateWalletCurrencyField:

    @allure.description('Создане счета проверка поля currency_id - Существующий id')
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
            """Проверка наличия обязательных полей"""
            assert data['data']['currency_id'] == 2
        except AssertionError:
            raise AssertionError

        finally:
            WalletMethods.delete_wallet_by_id(wallet_id, access_token)

    @allure.description('Создане счета проверка поля currency_id - несуществующий id')
    def test_02(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wallet', 44, 0, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('Создане счета проверка поля currency_id - Поле отсутствует')
    def test_03(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet_without_currency(
            'wallet', 0, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Создане счета проверка поля currency_id - Пустое поле')
    def test_04(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wallet', '', 0, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Создане счета проверка поля currency_id - Null')
    def test_05(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wallet', None, 0, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Создане счета проверка поля currency_id - id = 0')
    def test_06(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wallet', 0, 0, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Создане счета проверка поля currency_id - Неверный тип данных')
    def test_07(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wallet', 'string', 0, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Создане счета проверка поля currency_id - Вещественное число')
    def test_08(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wallet', 2.5, 0, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Создане счета проверка поля currency_id - Спецсимволы')
    def test_09(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wallet', '!@#$%^&', 0, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Создане счета проверка поля currency_id - Отрицательный id')
    def test_10(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'wallet', -1, 0, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)
