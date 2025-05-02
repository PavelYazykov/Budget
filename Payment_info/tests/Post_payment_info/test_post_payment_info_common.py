import allure

from Payment_info.methods.payment_info_methods import PaymentInfoMethods
from common_methods.checking import Checking
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from Wallet.methods.wallet_methods import WalletMethods
from Payment_info.methods.payloads import Payloads


@allure.epic('Post/api/v1/payment_info/{payment_info_id}/ - Оплата просроченного платежа - общие проверки')
class TestPostPaymentInfoCommon:

    @allure.description('Общие проверки - Оплата долга с валидными данными (авторизованный пользователь)')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        wallet_id = None

        """Создание regular_outcome"""
        create_regular_outcome = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, None, 'month', 10, False,
            '2026-04-12', access_token
        )
        Checking.check_statuscode(create_regular_outcome, 201)
        data = Checking.get_data(create_regular_outcome)
        regular_outcome_id = data['data']['id']

        PaymentInfoMethods.create_regular_outcome('2025-04-12', regular_outcome_id)
        try:
            """Создание wallet"""
            create_wallet = WalletMethods.create_wallet(
                'Pavel_wallet', 2, 10, access_token
            )
            Checking.check_statuscode(create_wallet, 201)
            data = Checking.get_data(create_wallet)
            wallet_id = data['data']['id']

            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-04-12', None, False, 111
            )

            """Оплата"""
            pay_payment_info = PaymentInfoMethods.post_pay_payment_info(111, wallet_id, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(pay_payment_info, 201)

            """Проверка наличия обязательных полей"""
            Payloads.check_required_fields(pay_payment_info, Payloads.post_response)

            """Проверка значений поля amount"""
            data_2 = Checking.get_data(pay_payment_info)
            assert data_2['data']['amount'] == '10.00'
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

            """Удаление wallet"""
            WalletMethods.delete_wallet_sql(wallet_id)

    @allure.description('Общие проверки - Оплата долга с валидными данными (неавторизованный пользователь)')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        wallet_id = None

        """Создание regular_outcome"""
        create_regular_outcome = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, None, 'month', 10, False,
            '2026-04-12', access_token
        )
        Checking.check_statuscode(create_regular_outcome, 201)
        data = Checking.get_data(create_regular_outcome)
        regular_outcome_id = data['data']['id']

        PaymentInfoMethods.create_regular_outcome('2025-04-12', regular_outcome_id)
        try:
            """Создание wallet"""
            create_wallet = WalletMethods.create_wallet(
                'Pavel_wallet', 2, 10, access_token
            )
            Checking.check_statuscode(create_wallet, 201)
            data = Checking.get_data(create_wallet)
            wallet_id = data['data']['id']

            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-04-12', None, False, 111
            )

            """Оплата"""
            pay_payment_info = PaymentInfoMethods.post_pay_payment_info_without_auth(111, wallet_id)

            """Проверка статус кода"""
            Checking.check_statuscode(pay_payment_info, 401)

        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

            """Удаление wallet"""
            WalletMethods.delete_wallet_sql(wallet_id)

    @allure.description('Общие проверки - Отправка запроса без body')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        wallet_id = None

        """Создание regular_outcome"""
        create_regular_outcome = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, None, 'month', 10, False,
            '2026-04-12', access_token
        )
        Checking.check_statuscode(create_regular_outcome, 201)
        data = Checking.get_data(create_regular_outcome)
        regular_outcome_id = data['data']['id']

        PaymentInfoMethods.create_regular_outcome('2025-04-12', regular_outcome_id)
        try:
            """Создание wallet"""
            create_wallet = WalletMethods.create_wallet(
                'Pavel_wallet', 2, 10, access_token
            )
            Checking.check_statuscode(create_wallet, 201)
            data = Checking.get_data(create_wallet)
            wallet_id = data['data']['id']

            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-04-12', None, False, 111
            )

            """Оплата"""
            pay_payment_info = PaymentInfoMethods.post_pay_payment_info_without_body(111, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(pay_payment_info, 422)

        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

            """Удаление wallet"""
            WalletMethods.delete_wallet_sql(wallet_id)

    @allure.description('Общие проверки - Недостаточная сумма на кошельке')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        wallet_id = None

        """Создание regular_outcome"""
        create_regular_outcome = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, None, 'month', 10, False,
            '2026-04-12', access_token
        )
        Checking.check_statuscode(create_regular_outcome, 201)
        data = Checking.get_data(create_regular_outcome)
        regular_outcome_id = data['data']['id']

        PaymentInfoMethods.create_regular_outcome('2025-04-12', regular_outcome_id)
        try:
            """Создание wallet"""
            create_wallet = WalletMethods.create_wallet(
                'Pavel_wallet', 2, 1, access_token
            )
            Checking.check_statuscode(create_wallet, 201)
            data = Checking.get_data(create_wallet)
            wallet_id = data['data']['id']

            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-04-12', None, False, 111
            )

            """Оплата"""
            pay_payment_info = PaymentInfoMethods.post_pay_payment_info(111, wallet_id, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(pay_payment_info, 400)

        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

            """Удаление wallet"""
            WalletMethods.delete_wallet_sql(wallet_id)
