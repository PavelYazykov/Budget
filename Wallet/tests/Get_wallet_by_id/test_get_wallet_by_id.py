import json
import allure
from common_methods.checking import Checking
from Wallet.methods.wallet_methods import WalletMethods
from Wallet.methods.payloads import WalletPayloads


@allure.epic('Get/api/v1/wallet/  Получение информации о кошельке по id')
class TestGetWalletById:

    @allure.description('Получение информации о кошельке по id - Существующим ID (авторизованный пользователь)')
    def test_01(self, create_and_delete_wallet):
        """Авторизауия"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на получение кошелька"""
        result = WalletMethods.get_wallet_by_id(wallet_id, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        WalletPayloads.check_required_fields(result, WalletPayloads.get_payloads)

    @allure.description('Получение информации о кошельке по id - Существующим ID (неавторизованный пользователь)')
    def test_02(self):
        """Запрос на получение кошелька"""
        result = WalletMethods.get_wallet_by_id_without_auth('001')

        """Проверка статус кода"""
        Checking.check_statuscode(result, 401)

    @allure.description('Получение информации о кошельке по id - несуществующее значение')
    def test_03(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Запрос на получение кошелька"""
        result = WalletMethods.get_wallet_by_id('001', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 403)

    @allure.description('Получение информации о кошельке по id - вещественное число')
    def test_04(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Запрос на получение кошелька"""
        result = WalletMethods.get_wallet_by_id(1.5, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Получение информации о кошельке по id - Значение = 0')
    def test_05(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Запрос на получение кошелька"""
        result = WalletMethods.get_wallet_by_id(0, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Получение информации о кошельке по id - Отрицательное значение')
    def test_06(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Запрос на получение кошелька"""
        result = WalletMethods.get_wallet_by_id(-1, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Получение информации о кошельке по id - Пуcтое поле -> Отрабатыват как get_all_wallet')
    def test_07(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Запрос на получение кошелька"""
        result = WalletMethods.get_wallet_by_id('', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Получение информации о кошельке по id - Null')
    def test_08(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Запрос на получение кошелька"""
        result = WalletMethods.get_wallet_by_id(None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Получение информации о кошельке по id - Недопустимое значение поля')
    def test_09(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Запрос на получение кошелька"""
        result = WalletMethods.get_wallet_by_id('string', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Получение информации о кошельке по id - Получение чужого счета')
    def test_10(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Запрос на получение кошелька"""
        result = WalletMethods.get_wallet_by_id('992', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 403)





