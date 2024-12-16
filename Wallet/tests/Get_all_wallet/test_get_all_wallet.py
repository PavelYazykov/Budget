import json

import allure
from common_methods.checking import Checking
from Wallet.methods.wallet_methods import WalletMethods
from Wallet.methods.payloads import WalletPayloads
from Auth.methods.auth_methods import Auth


@allure.epic('GET/api/v1/wallet/  Получение списка всех счетов')
class TestGetAllWallet:

    @allure.description('Получение списка все счетов (авторизованный пользователь)')
    def test_01(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Запрос счетов"""
        result = WalletMethods.get_all_wallet(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Получение списка все счетов (неавторизованный пользователь)')
    def test_02(self):

        """Запрос счетов"""
        result = WalletMethods.get_all_wallet_without_auth()

        """Проверка статус кода"""
        Checking.check_statuscode(result, 401)



