import allure
import pytest

from Payment_info.methods.payloads import Payloads
from Payment_info.methods.payment_info_methods import PaymentInfoMethods
from common_methods.checking import Checking
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from Wallet.methods.wallet_methods import WalletMethods


@pytest.mark.Payment_info
@allure.epic('Post/api/v1/payment_info/{payment_info_id}/ - Оплата просроченного платежа - '
             'проверка поля payment_info_id')
class TestPostPaymentInfoId:

    @allure.description('Проверка поля payment_info_id - Существующий id')
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
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

            """Удаление wallet"""
            WalletMethods.delete_wallet_sql(wallet_id)

    @allure.description('Проверка поля payment_info_id - Несуществующий id')
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

            """Оплата"""
            pay_payment_info = PaymentInfoMethods.post_pay_payment_info(1111, wallet_id, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(pay_payment_info, 404)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

            """Удаление wallet"""
            WalletMethods.delete_wallet_sql(wallet_id)

    @allure.description('Проверка поля payment_info_id - Недопустимые символы')
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

            """Оплата"""
            pay_payment_info = PaymentInfoMethods.post_pay_payment_info('12swe', wallet_id, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(pay_payment_info, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

            """Удаление wallet"""
            WalletMethods.delete_wallet_sql(wallet_id)

    @allure.description('Проверка поля payment_info_id - Пустое поле')
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
                'Pavel_wallet', 2, 10, access_token
            )
            Checking.check_statuscode(create_wallet, 201)
            data = Checking.get_data(create_wallet)
            wallet_id = data['data']['id']

            """Оплата"""
            pay_payment_info = PaymentInfoMethods.post_pay_payment_info('', wallet_id, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(pay_payment_info, 404)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

            """Удаление wallet"""
            WalletMethods.delete_wallet_sql(wallet_id)

    @allure.description('Проверка поля payment_info_id - Поле отсутствует')
    def test_05(self, auth_fixture):
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

            """Оплата"""
            pay_payment_info = PaymentInfoMethods.post_pay_payment_info_without_payment_info_id(wallet_id, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(pay_payment_info, 405)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

            """Удаление wallet"""
            WalletMethods.delete_wallet_sql(wallet_id)

    @allure.description('Проверка поля payment_info_id - Null')
    def test_06(self, auth_fixture):
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

            """Оплата"""
            pay_payment_info = PaymentInfoMethods.post_pay_payment_info(None, wallet_id, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(pay_payment_info, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

            """Удаление wallet"""
            WalletMethods.delete_wallet_sql(wallet_id)

    @allure.description('Проверка поля payment_info_id - Значение больше 2147483647')
    def test_07(self, auth_fixture):
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

            """Оплата"""
            pay_payment_info = PaymentInfoMethods.post_pay_payment_info(2147483648, wallet_id, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(pay_payment_info, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

            """Удаление wallet"""
            WalletMethods.delete_wallet_sql(wallet_id)