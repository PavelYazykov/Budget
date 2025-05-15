import json

import allure
import pytest

from common_methods.checking import Checking
from Wallet.methods.wallet_methods import WalletMethods
from Wallet.methods.payloads import WalletPayloads


@pytest.mark.Wallet
@allure.epic('Post/api/v1/wallet/  Создание счета')
class TestCreateWalletCommonCheck:

    @allure.description('Создане счета с валидными данными')
    def test_01(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet(
            'Pavel_wallet', 2, 0, access_token
        )
        data = Checking.get_data(result)
        wallet_id = data['data']['id']

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        try:
            """Проверка наличия обязательных полей"""
            WalletPayloads.check_required_fields(result, WalletPayloads.get_payloads)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            WalletMethods.delete_wallet_sql(wallet_id)

    @allure.description('Создане счета без body')
    def test_02(self, auth_fixture):
        """Авторизауия"""
        access_token = auth_fixture

        """Создание счета"""
        result = WalletMethods.create_wallet_without_body(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)


