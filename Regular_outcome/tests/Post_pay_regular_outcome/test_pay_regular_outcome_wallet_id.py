import allure
import pytest

from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from Regular_outcome.methods.payloads import RegularOutcomePayloads


@pytest.mark.Regular_outcome
@allure.epic(
    'POST/api/v1/regular_outcome/pay_regular_outcome/{regular_outcome_id}/ - '
    'оплата регулярных списаний по id - проверка поля wallet_id'
)
class TestPayRegularOutcomeWalletIdField:

    @allure.description('проверка поля wallet_id - Существующий id')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )

        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        """Создание копилки"""
        result_create_moneybox = MoneyboxMethods.create_moneybox(
            '2030-12-12', 1000, 'name', 2, 100, access_token
        )
        Checking.check_statuscode(result_create_moneybox, 201)
        data = Checking.get_data(result_create_moneybox)
        wallet_id = data['data']['wallet']['id']
        moneybox_id = data['data']['id']
        try:
            """списание регулярного плтаежа"""
            result_pay = RegularOutcomeMethods.post_pay_regular_outcome(
                regular_outcome_id, wallet_id, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_pay, 200)

            """Проверка поля id"""
            RegularOutcomePayloads.check_required_fields(result_pay, RegularOutcomePayloads.pay_regular_outcome)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id, wallet_id)

    @allure.description('проверка поля wallet_id - Несуществующий id')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )

        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        try:
            """списание регулярного плтаежа"""
            result_pay = RegularOutcomeMethods.post_pay_regular_outcome(
                regular_outcome_id, 999, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_pay, 404)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля wallet_id - Отрицательное значение id')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )

        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        try:
            """списание регулярного плтаежа"""
            result_pay = RegularOutcomeMethods.post_pay_regular_outcome(
                regular_outcome_id, -9, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_pay, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля wallet_id - Значение id = 0')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )

        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        try:
            """списание регулярного плтаежа"""
            result_pay = RegularOutcomeMethods.post_pay_regular_outcome(
                regular_outcome_id, 0, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_pay, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля wallet_id - Пустое поле')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )

        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        try:
            """списание регулярного плтаежа"""
            result_pay = RegularOutcomeMethods.post_pay_regular_outcome(
                regular_outcome_id, '', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_pay, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля wallet_id - Поле отсутствует')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )

        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        try:
            """списание регулярного плтаежа"""
            result_pay = RegularOutcomeMethods.post_pay_regular_outcome_without_wallet_id(
                regular_outcome_id, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_pay, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля wallet_id - Null')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )

        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        try:
            """списание регулярного плтаежа"""
            result_pay = RegularOutcomeMethods.post_pay_regular_outcome(
                regular_outcome_id, None, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_pay, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля wallet_id - Неверный тип данных string')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )

        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        try:
            """списание регулярного плтаежа"""
            result_pay = RegularOutcomeMethods.post_pay_regular_outcome(
                regular_outcome_id, 'string', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_pay, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
