import allure
from common_methods.checking import Checking
from Wallet.methods.wallet_methods import WalletMethods


@allure.epic('Patch/api/v1/wallet/{wallet_id}/ Редактирование кошелька - Проверка поля wallet_id')
class TestPatchWalletCommon:

    @allure.description('Проверка поля wallet_id - Существующее значение')
    def test_01(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            wallet_id, 2, access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Проверка поля wallet_id - Несуществующее значение')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            994, 2, access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('Проверка поля wallet_id - Значение = 0')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            0, 2, access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля wallet_id - Отрицательное значение')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            -1, 2, access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля wallet_id - Пуcтое поле')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            '', 2, access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 405)

    @allure.description('Проверка поля wallet_id - Поле отсутствует')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_without_id(
            'name', 2, False, access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 405)

    @allure.description('Проверка поля wallet_id - Null')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            None, 2, access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля wallet_id - Недопустимое значение поля')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            'string', 2, access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 422)
