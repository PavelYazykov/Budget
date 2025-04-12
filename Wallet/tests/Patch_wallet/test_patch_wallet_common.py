import time

import allure
import pytest

from common_methods.auth import Auth
from common_methods.checking import Checking
from Wallet.methods.wallet_methods import WalletMethods
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from Auth.methods.auth_methods import AuthMethods
from common_methods.variables import AuthVariables


@pytest.mark.Wallet
@allure.epic('Patch/api/v1/wallet/{wallet_id}/ Редактирование wallet')
class TestPatchWalletCommon:

    @allure.description('Редактирование wallet - Изменение счета с валидными данными')
    def test_01(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование wallet"""
        result = WalletMethods.change_wallet_by_id(
            wallet_id, 'wallet_name', 2, False, access_token
        )
        print(result.text)

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Редактирование wallet - Изменение счета без body')
    def test_02(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование wallet"""
        result = WalletMethods.change_wallet_by_id_without_body(wallet_id, access_token)

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Измение счета от копилки')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_moneybox = MoneyboxMethods.create_moneybox(
            '2030-12-30', 1000, 'name', 2, 0, access_token,
        )
        Checking.check_statuscode(result_moneybox, 201)
        data = Checking.get_data(result_moneybox)
        wallet_id = data['data']['wallet']['id']
        moneybox_id = MoneyboxMethods.get_moneybox_id(result_moneybox)
        try:
            """Запрос на редактирование"""
            result_change = WalletMethods.change_wallet_by_id(
                wallet_id, 'new_name', 2, False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 400)
        finally:
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('Измение счета от копилки чужого пользователя')
    def test_04(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Создание второго пользователя"""
        result_create_second_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_second_user, 201)
        data, user_id = AuthMethods.get_id(result_create_second_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Авторизация второго пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token_2 = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Запрос на редактирование чужого wallet"""
            result_change = WalletMethods.change_wallet_by_id(
                wallet_id, 'wallet_2', 2, False, access_token_2
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 403)
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)


