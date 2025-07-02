import allure
import pytest

from Notifications.methods.notifications_methods import NotificationsMethods
from common_methods.checking import Checking
from Users.methods.users_methods import UsersMethods
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from Wallet.methods.wallet_methods import WalletMethods
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
from datetime import date
current_date = date.today()


@pytest.mark.notifications
@allure.epic('Get/api/v1/notification/get/regular - Получение списка уведомлений о регулярных платежах - '
             'проверка поля user_id')
class TestGetNotificationsUserId:

    @allure.description('проверка поля user_id - Существующее значение user_id')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Получение информации о пользователе"""
        get_user = UsersMethods.get_user(access_token)
        data = Checking.get_data(get_user)
        user_id = data['id']

        """Создание регулярного персонального бюджета"""
        result_create = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, None, 'day', 100, False,
            '2030-12-12', access_token
        )
        data = Checking.get_data(result_create)
        regular_outcome_id = data['data']['id']
        try:
            # """Создание счета"""
            # create_wallet = WalletMethods.create_wallet(
            #     'Pavel_wallet', 2, 100, access_token
            # )
            # Checking.check_statuscode(create_wallet, 201)
            # data_wallet = Checking.get_data(create_wallet)
            # wallet_id = data_wallet['data']['id']
            #
            # """Оплата регулярного платежа"""
            # result_pay = RegularOutcomeMethods.pay_regular_outcome(
            #     regular_outcome_id, wallet_id, access_token,
            # )
            # Checking.check_statuscode(result_pay, 200)

            """Запрос списка регулярных платежей"""
            result = NotificationsMethods.get_notifications(user_id, '2030-12-11', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка отображения уведомления"""
            data_notifications = Checking.get_data(result)
            assert data_notifications['meta']['total_count'] == 1
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            # """Удаление счета"""
            # if float(data_wallet['data']['amount']) > 0:
            #     print(float(data_wallet['data']['amount']))
            #     PersonalTransactionMethods.create_personal_transaction(
            #         100, 'pavel', 'Consumption', '2025-03-24',
            #         None, wallet_id, 20, None, access_token
            #     )
            # delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            # Checking.check_statuscode(delete_wallet, 204)

            """Удаление регулярного бюджета"""
            result_delete = RegularOutcomeMethods.delete_regular_outcome(
                regular_outcome_id, access_token
            )
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля user_id - Несуществующее значение user_id')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание регулярного персонального бюджета"""
        result_create = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, None, 'day', 100, False,
            '2030-12-12', access_token
        )
        data = Checking.get_data(result_create)
        regular_outcome_id = data['data']['id']
        try:
            # """Создание счета"""
            # create_wallet = WalletMethods.create_wallet(
            #     'Pavel_wallet', 2, 100, access_token
            # )
            # Checking.check_statuscode(create_wallet, 201)
            # data_wallet = Checking.get_data(create_wallet)
            # wallet_id = data_wallet['data']['id']
            #
            # """Оплата регулярного платежа"""
            # result_pay = RegularOutcomeMethods.pay_regular_outcome(
            #     regular_outcome_id, wallet_id, access_token,
            # )
            # Checking.check_statuscode(result_pay, 200)

            """Запрос списка регулярных платежей"""
            result = NotificationsMethods.get_notifications('cb59999c-b112-47bb-a048-c9b4cb234fa1',
                                                            '2030-12-11', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 404)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            # """Удаление счета"""
            # if float(data_wallet['data']['amount']) > 0:
            #     print(float(data_wallet['data']['amount']))
            #     PersonalTransactionMethods.create_personal_transaction(
            #         100, 'pavel', 'Consumption', '2025-03-24',
            #         None, wallet_id, 20, None, access_token
            #     )
            # delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            # Checking.check_statuscode(delete_wallet, 204)

            """Удаление регулярного бюджета"""
            result_delete = RegularOutcomeMethods.delete_regular_outcome(
                regular_outcome_id, access_token
            )
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля user_id - Неверный тип данных integer')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Инициализация переменных"""
        wallet_id = None
        data_wallet = None

        """Создание регулярного персонального бюджета"""
        result_create = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, None, 'day', 100, False,
            '2030-12-12', access_token
        )
        data = Checking.get_data(result_create)
        regular_outcome_id = data['data']['id']
        try:
            """Создание счета"""
            create_wallet = WalletMethods.create_wallet(
                'Pavel_wallet', 2, 100, access_token
            )
            Checking.check_statuscode(create_wallet, 201)
            data_wallet = Checking.get_data(create_wallet)
            wallet_id = data_wallet['data']['id']

            """Оплата регулярного платежа"""
            result_pay = RegularOutcomeMethods.pay_regular_outcome(
                regular_outcome_id, wallet_id, access_token,
            )
            Checking.check_statuscode(result_pay, 200)

            """Запрос списка регулярных платежей"""
            result = NotificationsMethods.get_notifications(12345678912345685478996321445,
                                                            '2030-12-11', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление счета"""
            if float(data_wallet['data']['amount']) > 0:
                print(float(data_wallet['data']['amount']))
                PersonalTransactionMethods.create_personal_transaction(
                    100, 'pavel', 'Consumption', '2025-03-24',
                    None, wallet_id, 20, None, access_token
                )
            delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            Checking.check_statuscode(delete_wallet, 204)

            """Удаление регулярного бюджета"""
            result_delete = RegularOutcomeMethods.delete_regular_outcome(
                regular_outcome_id, access_token
            )
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля user_id - Пустое поле')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Инициализация переменных"""
        wallet_id = None
        data_wallet = None

        """Создание регулярного персонального бюджета"""
        result_create = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, None, 'day', 100, False,
            '2030-12-12', access_token
        )
        data = Checking.get_data(result_create)
        regular_outcome_id = data['data']['id']
        try:
            """Создание счета"""
            create_wallet = WalletMethods.create_wallet(
                'Pavel_wallet', 2, 100, access_token
            )
            Checking.check_statuscode(create_wallet, 201)
            data_wallet = Checking.get_data(create_wallet)
            wallet_id = data_wallet['data']['id']

            """Оплата регулярного платежа"""
            result_pay = RegularOutcomeMethods.pay_regular_outcome(
                regular_outcome_id, wallet_id, access_token,
            )
            Checking.check_statuscode(result_pay, 200)

            """Запрос списка регулярных платежей"""
            result = NotificationsMethods.get_notifications('',
                                                            '2030-12-11', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление счета"""
            if float(data_wallet['data']['amount']) > 0:
                print(float(data_wallet['data']['amount']))
                PersonalTransactionMethods.create_personal_transaction(
                    100, 'pavel', 'Consumption', '2025-03-24',
                    None, wallet_id, 20, None, access_token
                )
            delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            Checking.check_statuscode(delete_wallet, 204)

            """Удаление регулярного бюджета"""
            result_delete = RegularOutcomeMethods.delete_regular_outcome(
                regular_outcome_id, access_token
            )
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля user_id - Пустое поле')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Инициализация переменных"""
        wallet_id = None
        data_wallet = None

        """Создание регулярного персонального бюджета"""
        result_create = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, None, 'day', 100, False,
            '2030-12-12', access_token
        )
        data = Checking.get_data(result_create)
        regular_outcome_id = data['data']['id']
        try:
            """Создание счета"""
            create_wallet = WalletMethods.create_wallet(
                'Pavel_wallet', 2, 100, access_token
            )
            Checking.check_statuscode(create_wallet, 201)
            data_wallet = Checking.get_data(create_wallet)
            wallet_id = data_wallet['data']['id']

            """Оплата регулярного платежа"""
            result_pay = RegularOutcomeMethods.pay_regular_outcome(
                regular_outcome_id, wallet_id, access_token,
            )
            Checking.check_statuscode(result_pay, 200)

            """Запрос списка регулярных платежей"""
            result = NotificationsMethods.get_notifications('',
                                                            '2030-12-11', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление счета"""
            if float(data_wallet['data']['amount']) > 0:
                print(float(data_wallet['data']['amount']))
                PersonalTransactionMethods.create_personal_transaction(
                    100, 'pavel', 'Consumption', '2025-03-24',
                    None, wallet_id, 20, None, access_token
                )
            delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            Checking.check_statuscode(delete_wallet, 204)

            """Удаление регулярного бюджета"""
            result_delete = RegularOutcomeMethods.delete_regular_outcome(
                regular_outcome_id, access_token
            )
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля user_id - Поле отсутствует')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Инициализация переменных"""
        wallet_id = None
        data_wallet = None

        """Создание регулярного персонального бюджета"""
        result_create = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, None, 'day', 100, False,
            '2030-12-12', access_token
        )
        data = Checking.get_data(result_create)
        regular_outcome_id = data['data']['id']
        try:
            """Создание счета"""
            create_wallet = WalletMethods.create_wallet(
                'Pavel_wallet', 2, 100, access_token
            )
            Checking.check_statuscode(create_wallet, 201)
            data_wallet = Checking.get_data(create_wallet)
            wallet_id = data_wallet['data']['id']

            """Оплата регулярного платежа"""
            result_pay = RegularOutcomeMethods.pay_regular_outcome(
                regular_outcome_id, wallet_id, access_token,
            )
            Checking.check_statuscode(result_pay, 200)

            """Запрос списка регулярных платежей"""
            result = NotificationsMethods.get_notifications_without_user_id('2030-12-11', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление счета"""
            if float(data_wallet['data']['amount']) > 0:
                print(float(data_wallet['data']['amount']))
                PersonalTransactionMethods.create_personal_transaction(
                    100, 'pavel', 'Consumption', '2025-03-24',
                    None, wallet_id, 20, None, access_token
                )
            delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            Checking.check_statuscode(delete_wallet, 204)

            """Удаление регулярного бюджета"""
            result_delete = RegularOutcomeMethods.delete_regular_outcome(
                regular_outcome_id, access_token
            )
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля user_id - Null')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Инициализация переменных"""
        wallet_id = None
        data_wallet = None

        """Создание регулярного персонального бюджета"""
        result_create = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, None, 'day', 100, False,
            '2030-12-12', access_token
        )
        data = Checking.get_data(result_create)
        regular_outcome_id = data['data']['id']
        try:
            """Создание счета"""
            create_wallet = WalletMethods.create_wallet(
                'Pavel_wallet', 2, 100, access_token
            )
            Checking.check_statuscode(create_wallet, 201)
            data_wallet = Checking.get_data(create_wallet)
            wallet_id = data_wallet['data']['id']

            """Оплата регулярного платежа"""
            result_pay = RegularOutcomeMethods.pay_regular_outcome(
                regular_outcome_id, wallet_id, access_token,
            )
            Checking.check_statuscode(result_pay, 200)

            """Запрос списка регулярных платежей"""
            result = NotificationsMethods.get_notifications(None, '2030-12-11', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление счета"""
            if float(data_wallet['data']['amount']) > 0:
                print(float(data_wallet['data']['amount']))
                PersonalTransactionMethods.create_personal_transaction(
                    100, 'pavel', 'Consumption', '2025-03-24',
                    None, wallet_id, 20, None, access_token
                )
            delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            Checking.check_statuscode(delete_wallet, 204)

            """Удаление регулярного бюджета"""
            result_delete = RegularOutcomeMethods.delete_regular_outcome(
                regular_outcome_id, access_token
            )
            Checking.check_statuscode(result_delete, 204)

