import allure

from Notifications.methods.notifications_methods import NotificationsMethods
from common_methods.checking import Checking
from Users.methods.users_methods import UsersMethods
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from Wallet.methods.wallet_methods import WalletMethods
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
from datetime import date
current_date = date.today()


@allure.epic('Get/api/v1/notification/get/regular - Получение списка уведомлений о регулярных платежах - '
             'проверка поля local_date')
class TestGetNotificationsLocalDate:

    @allure.description('проверка поля local_date - Дата в формате гггг-мм-дд')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Инициализация переменных"""
        wallet_id = None
        data_wallet = None

        """Получение информации о пользователе"""
        get_user = UsersMethods.get_user(access_token)
        data = Checking.get_data(get_user)
        user_id = data['id']

        # """Создание регулярного персонального бюджета"""
        # result_create = RegularOutcomeMethods.create_regular_outcome(
        #     'Pavel', 20, None, 'day', 100, False,
        #     '2030-12-12', access_token
        # )
        # data = Checking.get_data(result_create)
        # regular_outcome_id = data['data']['id']
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

        finally:
            """Удаление счета"""
            # if float(data_wallet['data']['amount']) > 0:
            #     print(float(data_wallet['data']['amount']))
            #     PersonalTransactionMethods.create_personal_transaction(
            #         100, 'pavel', 'Consumption', '2025-03-24',
            #         None, wallet_id, 20, None, access_token
            #     )
            # delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            # Checking.check_statuscode(delete_wallet, 204)
            #
            # """Удаление регулярного бюджета"""
            # result_delete = RegularOutcomeMethods.delete_regular_outcome(
            #     regular_outcome_id, access_token
            # )
            # Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля local_date - Дата в формате гггг-мм-дд (integer)')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Инициализация переменных"""
        wallet_id = None
        data_wallet = None

        """Получение информации о пользователе"""
        get_user = UsersMethods.get_user(access_token)
        data = Checking.get_data(get_user)
        user_id = data['id']

        # """Создание регулярного персонального бюджета"""
        # result_create = RegularOutcomeMethods.create_regular_outcome(
        #     'Pavel', 20, None, 'day', 100, False,
        #     '2030-12-12', access_token
        # )
        # data = Checking.get_data(result_create)
        # regular_outcome_id = data['data']['id']
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
            result = NotificationsMethods.get_notifications(user_id, 2030-12-11, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)

        finally:
            """Удаление счета"""
            # if float(data_wallet['data']['amount']) > 0:
            #     print(float(data_wallet['data']['amount']))
            #     PersonalTransactionMethods.create_personal_transaction(
            #         100, 'pavel', 'Consumption', '2025-03-24',
            #         None, wallet_id, 20, None, access_token
            #     )
            # delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            # Checking.check_statuscode(delete_wallet, 204)
            #
            # """Удаление регулярного бюджета"""
            # result_delete = RegularOutcomeMethods.delete_regular_outcome(
            #     regular_outcome_id, access_token
            # )
            # Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля local_date - Недопустимые символы string')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Инициализация переменных"""
        wallet_id = None
        data_wallet = None

        """Получение информации о пользователе"""
        get_user = UsersMethods.get_user(access_token)
        data = Checking.get_data(get_user)
        user_id = data['id']

        # """Создание регулярного персонального бюджета"""
        # result_create = RegularOutcomeMethods.create_regular_outcome(
        #     'Pavel', 20, None, 'day', 100, False,
        #     '2030-12-12', access_token
        # )
        # data = Checking.get_data(result_create)
        # regular_outcome_id = data['data']['id']
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
            result = NotificationsMethods.get_notifications(user_id, 'цук35"№4', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)

        finally:
            """Удаление счета"""
            # if float(data_wallet['data']['amount']) > 0:
            #     print(float(data_wallet['data']['amount']))
            #     PersonalTransactionMethods.create_personal_transaction(
            #         100, 'pavel', 'Consumption', '2025-03-24',
            #         None, wallet_id, 20, None, access_token
            #     )
            # delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            # Checking.check_statuscode(delete_wallet, 204)
            #
            # """Удаление регулярного бюджета"""
            # result_delete = RegularOutcomeMethods.delete_regular_outcome(
            #     regular_outcome_id, access_token
            # )
            # Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля local_date - Дата в формате гг-мм-дд')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Инициализация переменных"""
        wallet_id = None
        data_wallet = None

        """Получение информации о пользователе"""
        get_user = UsersMethods.get_user(access_token)
        data = Checking.get_data(get_user)
        user_id = data['id']

        # """Создание регулярного персонального бюджета"""
        # result_create = RegularOutcomeMethods.create_regular_outcome(
        #     'Pavel', 20, None, 'day', 100, False,
        #     '2030-12-12', access_token
        # )
        # data = Checking.get_data(result_create)
        # regular_outcome_id = data['data']['id']
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
            result = NotificationsMethods.get_notifications(user_id, '25-12-12', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)

        finally:
            """Удаление счета"""
            # if float(data_wallet['data']['amount']) > 0:
            #     print(float(data_wallet['data']['amount']))
            #     PersonalTransactionMethods.create_personal_transaction(
            #         100, 'pavel', 'Consumption', '2025-03-24',
            #         None, wallet_id, 20, None, access_token
            #     )
            # delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            # Checking.check_statuscode(delete_wallet, 204)
            #
            # """Удаление регулярного бюджета"""
            # result_delete = RegularOutcomeMethods.delete_regular_outcome(
            #     regular_outcome_id, access_token
            # )
            # Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля local_date - Дата в формате гггг-м-дд')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Инициализация переменных"""
        wallet_id = None
        data_wallet = None

        """Получение информации о пользователе"""
        get_user = UsersMethods.get_user(access_token)
        data = Checking.get_data(get_user)
        user_id = data['id']

        # """Создание регулярного персонального бюджета"""
        # result_create = RegularOutcomeMethods.create_regular_outcome(
        #     'Pavel', 20, None, 'day', 100, False,
        #     '2030-12-12', access_token
        # )
        # data = Checking.get_data(result_create)
        # regular_outcome_id = data['data']['id']
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
            result = NotificationsMethods.get_notifications(user_id, '25-1-12', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)

        finally:
            """Удаление счета"""
            # if float(data_wallet['data']['amount']) > 0:
            #     print(float(data_wallet['data']['amount']))
            #     PersonalTransactionMethods.create_personal_transaction(
            #         100, 'pavel', 'Consumption', '2025-03-24',
            #         None, wallet_id, 20, None, access_token
            #     )
            # delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            # Checking.check_statuscode(delete_wallet, 204)
            #
            # """Удаление регулярного бюджета"""
            # result_delete = RegularOutcomeMethods.delete_regular_outcome(
            #     regular_outcome_id, access_token
            # )
            # Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля local_date - Дата в формате гггг-мм-д')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Инициализация переменных"""
        wallet_id = None
        data_wallet = None

        """Получение информации о пользователе"""
        get_user = UsersMethods.get_user(access_token)
        data = Checking.get_data(get_user)
        user_id = data['id']

        # """Создание регулярного персонального бюджета"""
        # result_create = RegularOutcomeMethods.create_regular_outcome(
        #     'Pavel', 20, None, 'day', 100, False,
        #     '2030-12-12', access_token
        # )
        # data = Checking.get_data(result_create)
        # regular_outcome_id = data['data']['id']
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
            result = NotificationsMethods.get_notifications(user_id, '25-11-1', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)

        finally:
            """Удаление счета"""
            # if float(data_wallet['data']['amount']) > 0:
            #     print(float(data_wallet['data']['amount']))
            #     PersonalTransactionMethods.create_personal_transaction(
            #         100, 'pavel', 'Consumption', '2025-03-24',
            #         None, wallet_id, 20, None, access_token
            #     )
            # delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            # Checking.check_statuscode(delete_wallet, 204)
            #
            # """Удаление регулярного бюджета"""
            # result_delete = RegularOutcomeMethods.delete_regular_outcome(
            #     regular_outcome_id, access_token
            # )
            # Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля local_date - Неверный порядок формата даты (дд-мм-гг)')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Инициализация переменных"""
        wallet_id = None
        data_wallet = None

        """Получение информации о пользователе"""
        get_user = UsersMethods.get_user(access_token)
        data = Checking.get_data(get_user)
        user_id = data['id']

        # """Создание регулярного персонального бюджета"""
        # result_create = RegularOutcomeMethods.create_regular_outcome(
        #     'Pavel', 20, None, 'day', 100, False,
        #     '2030-12-12', access_token
        # )
        # data = Checking.get_data(result_create)
        # regular_outcome_id = data['data']['id']
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
            result = NotificationsMethods.get_notifications(user_id, '24-12-2026', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)

        finally:
            """Удаление счета"""
            # if float(data_wallet['data']['amount']) > 0:
            #     print(float(data_wallet['data']['amount']))
            #     PersonalTransactionMethods.create_personal_transaction(
            #         100, 'pavel', 'Consumption', '2025-03-24',
            #         None, wallet_id, 20, None, access_token
            #     )
            # delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            # Checking.check_statuscode(delete_wallet, 204)
            #
            # """Удаление регулярного бюджета"""
            # result_delete = RegularOutcomeMethods.delete_regular_outcome(
            #     regular_outcome_id, access_token
            # )
            # Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля local_date - Неверный разделитель в формате даты (гггг.мм.дд)')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Инициализация переменных"""
        wallet_id = None
        data_wallet = None

        """Получение информации о пользователе"""
        get_user = UsersMethods.get_user(access_token)
        data = Checking.get_data(get_user)
        user_id = data['id']

        # """Создание регулярного персонального бюджета"""
        # result_create = RegularOutcomeMethods.create_regular_outcome(
        #     'Pavel', 20, None, 'day', 100, False,
        #     '2030-12-12', access_token
        # )
        # data = Checking.get_data(result_create)
        # regular_outcome_id = data['data']['id']
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
            result = NotificationsMethods.get_notifications(user_id, '2026.12.11', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)

        finally:
            """Удаление счета"""
            # if float(data_wallet['data']['amount']) > 0:
            #     print(float(data_wallet['data']['amount']))
            #     PersonalTransactionMethods.create_personal_transaction(
            #         100, 'pavel', 'Consumption', '2025-03-24',
            #         None, wallet_id, 20, None, access_token
            #     )
            # delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            # Checking.check_statuscode(delete_wallet, 204)
            #
            # """Удаление регулярного бюджета"""
            # result_delete = RegularOutcomeMethods.delete_regular_outcome(
            #     regular_outcome_id, access_token
            # )
            # Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля local_date - Null')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Инициализация переменных"""
        wallet_id = None
        data_wallet = None

        """Получение информации о пользователе"""
        get_user = UsersMethods.get_user(access_token)
        data = Checking.get_data(get_user)
        user_id = data['id']

        # """Создание регулярного персонального бюджета"""
        # result_create = RegularOutcomeMethods.create_regular_outcome(
        #     'Pavel', 20, None, 'day', 100, False,
        #     '2030-12-12', access_token
        # )
        # data = Checking.get_data(result_create)
        # regular_outcome_id = data['data']['id']
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
            result = NotificationsMethods.get_notifications(user_id, None, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)

        finally:
            """Удаление счета"""
            # if float(data_wallet['data']['amount']) > 0:
            #     print(float(data_wallet['data']['amount']))
            #     PersonalTransactionMethods.create_personal_transaction(
            #         100, 'pavel', 'Consumption', '2025-03-24',
            #         None, wallet_id, 20, None, access_token
            #     )
            # delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            # Checking.check_statuscode(delete_wallet, 204)
            #
            # """Удаление регулярного бюджета"""
            # result_delete = RegularOutcomeMethods.delete_regular_outcome(
            #     regular_outcome_id, access_token
            # )
            # Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля local_date - Пустое поле')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Инициализация переменных"""
        wallet_id = None
        data_wallet = None

        """Получение информации о пользователе"""
        get_user = UsersMethods.get_user(access_token)
        data = Checking.get_data(get_user)
        user_id = data['id']

        # """Создание регулярного персонального бюджета"""
        # result_create = RegularOutcomeMethods.create_regular_outcome(
        #     'Pavel', 20, None, 'day', 100, False,
        #     '2030-12-12', access_token
        # )
        # data = Checking.get_data(result_create)
        # regular_outcome_id = data['data']['id']
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
            result = NotificationsMethods.get_notifications(user_id, '', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)

        finally:
            """Удаление счета"""
            # if float(data_wallet['data']['amount']) > 0:
            #     print(float(data_wallet['data']['amount']))
            #     PersonalTransactionMethods.create_personal_transaction(
            #         100, 'pavel', 'Consumption', '2025-03-24',
            #         None, wallet_id, 20, None, access_token
            #     )
            # delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            # Checking.check_statuscode(delete_wallet, 204)
            #
            # """Удаление регулярного бюджета"""
            # result_delete = RegularOutcomeMethods.delete_regular_outcome(
            #     regular_outcome_id, access_token
            # )
            # Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля local_date - Поле отсутствует')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Инициализация переменных"""
        wallet_id = None
        data_wallet = None

        """Получение информации о пользователе"""
        get_user = UsersMethods.get_user(access_token)
        data = Checking.get_data(get_user)
        user_id = data['id']

        # """Создание регулярного персонального бюджета"""
        # result_create = RegularOutcomeMethods.create_regular_outcome(
        #     'Pavel', 20, None, 'day', 100, False,
        #     '2030-12-12', access_token
        # )
        # data = Checking.get_data(result_create)
        # regular_outcome_id = data['data']['id']
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
            result = NotificationsMethods.get_notifications_without_local_date(user_id, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)

        finally:
            """Удаление счета"""
            # if float(data_wallet['data']['amount']) > 0:
            #     print(float(data_wallet['data']['amount']))
            #     PersonalTransactionMethods.create_personal_transaction(
            #         100, 'pavel', 'Consumption', '2025-03-24',
            #         None, wallet_id, 20, None, access_token
            #     )
            # delete_wallet = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            # Checking.check_statuscode(delete_wallet, 204)
            #
            # """Удаление регулярного бюджета"""
            # result_delete = RegularOutcomeMethods.delete_regular_outcome(
            #     regular_outcome_id, access_token
            # )
            # Checking.check_statuscode(result_delete, 204)