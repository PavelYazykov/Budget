import allure
from common_methods.checking import Checking
from Wallet.methods.wallet_methods import WalletMethods
from Wallet.methods.payloads import WalletPayloads
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from Auth.methods.auth_methods import AuthMethods
from common_methods.variables import AuthVariables


@allure.epic('Patch/api/v1/wallet/{wallet_id}/ Редактирование кошелька')
class TestPatchWalletCommon:

    @allure.description('Редактирование кошелька - Изменение счета с валидными данными')
    def test_01(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id(
            wallet_id, 'wallet_name', 2, False, access_token
        )
        print(result.text)

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Редактирование кошелька - Изменение счета без body')
    def test_02(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
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
        print(wallet_id)

        """Запрос на редактирование"""
        result_change = WalletMethods.change_wallet_by_id(
            wallet_id, 'new_name', 2, False, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 400)

    @allure.description('Измение счета от копилки')
    def test_04(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Авторизация второго пользователя"""
        result_auth = AuthMethods.login('010101', AuthVariables.auth_payloads_3)
        Checking.check_statuscode(result_auth, 200)
        access_token_2 = result_auth.json().get('access_token')

        """Запрос на редактирование чужого кошелька"""
        result_change = WalletMethods.change_wallet_by_id(
            wallet_id, 'wallet_2', 2, False, access_token_2
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 403)


