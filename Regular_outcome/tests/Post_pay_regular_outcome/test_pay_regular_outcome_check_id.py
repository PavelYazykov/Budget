import allure
import pytest

from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from Regular_outcome.methods.payloads import RegularOutcomePayloads
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods


@pytest.mark.Regular_outcome
@allure.epic(
    'POST/api/v1/regular_outcome/pay_regular_outcome/{regular_outcome_id}/ - '
    'оплата регулярных списаний по id - проверка поля regular_outcome_id'
)
class TestPayRegularOutcomeIdField:

    @allure.description('проверка поля regular_outcome_id - Существующий id')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'Pavel', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )

        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        """Создание копилки"""
        result_create_moneybox = MoneyboxMethods.create_moneybox(
            '2030-12-12', 1000, 'Pavel', 2, 100, access_token
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

            """проверка поля regular_outcome_id"""
            RegularOutcomePayloads.check_required_fields(result_pay, RegularOutcomePayloads.pay_regular_outcome)
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
            if float(data['data']['wallet']['amount']) > 0:
                PersonalTransactionMethods.create_personal_transaction(
                    100, 'descr', 'Consumption', '2025-03-09',
                    None, wallet_id, 20, None, access_token
                )
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('проверка поля regular_outcome_id - Несуществующий id')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_create_moneybox = MoneyboxMethods.create_moneybox(
            '2030-12-12', 1000, 'name', 2, 0, access_token
        )
        Checking.check_statuscode(result_create_moneybox, 201)
        data = Checking.get_data(result_create_moneybox)
        wallet_id = data['data']['wallet']['id']
        moneybox_id = data['data']['id']
        try:
            """списание регулярного плтаежа"""
            result_pay = RegularOutcomeMethods.post_pay_regular_outcome(
                999, wallet_id, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_pay, 404)
        finally:
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('проверка поля regular_outcome_id - Отрицательное значение id')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_create_moneybox = MoneyboxMethods.create_moneybox(
            '2030-12-12', 1000, 'name', 2, 0, access_token
        )
        Checking.check_statuscode(result_create_moneybox, 201)
        data = Checking.get_data(result_create_moneybox)
        wallet_id = data['data']['wallet']['id']
        moneybox_id = data['data']['id']
        try:
            """списание регулярного плтаежа"""
            result_pay = RegularOutcomeMethods.post_pay_regular_outcome(
                -9, wallet_id, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_pay, 422)
        finally:
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('проверка поля regular_outcome_id - Значение id = 0')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_create_moneybox = MoneyboxMethods.create_moneybox(
            '2030-12-12', 1000, 'name', 2, 0, access_token
        )
        Checking.check_statuscode(result_create_moneybox, 201)
        data = Checking.get_data(result_create_moneybox)
        wallet_id = data['data']['wallet']['id']
        moneybox_id = data['data']['id']
        try:
            """списание регулярного плтаежа"""
            result_pay = RegularOutcomeMethods.post_pay_regular_outcome(
                0, wallet_id, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_pay, 422)
        finally:
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('проверка поля regular_outcome_id - Значение id - Пустое поле')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_create_moneybox = MoneyboxMethods.create_moneybox(
            '2030-12-12', 1000, 'name', 2, 0, access_token
        )
        Checking.check_statuscode(result_create_moneybox, 201)
        data = Checking.get_data(result_create_moneybox)
        wallet_id = data['data']['wallet']['id']
        moneybox_id = data['data']['id']
        try:
            """списание регулярного плтаежа"""
            result_pay = RegularOutcomeMethods.post_pay_regular_outcome(
                '', wallet_id, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_pay, 404)
        finally:
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('проверка поля regular_outcome_id - Значение id - Поле отсутствует')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_create_moneybox = MoneyboxMethods.create_moneybox(
            '2030-12-12', 1000, 'name', 2, 0, access_token
        )
        Checking.check_statuscode(result_create_moneybox, 201)
        data = Checking.get_data(result_create_moneybox)
        wallet_id = data['data']['wallet']['id']
        moneybox_id = data['data']['id']
        try:
            """списание регулярного плтаежа"""
            result_pay = RegularOutcomeMethods.post_pay_regular_outcome_without_regular_outcome_id(
                wallet_id, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_pay, 405)
        finally:
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('проверка поля regular_outcome_id - Значение id - Null')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_create_moneybox = MoneyboxMethods.create_moneybox(
            '2030-12-12', 1000, 'name', 2, 0, access_token
        )
        Checking.check_statuscode(result_create_moneybox, 201)
        data = Checking.get_data(result_create_moneybox)
        wallet_id = data['data']['wallet']['id']
        moneybox_id = data['data']['id']
        try:
            """списание регулярного плтаежа"""
            result_pay = RegularOutcomeMethods.post_pay_regular_outcome(
                None, wallet_id, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_pay, 422)
        finally:
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('проверка поля regular_outcome_id - Значение id - Неверный тип данных string')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_create_moneybox = MoneyboxMethods.create_moneybox(
            '2030-12-12', 1000, 'name', 2, 0, access_token
        )
        Checking.check_statuscode(result_create_moneybox, 201)
        data = Checking.get_data(result_create_moneybox)
        wallet_id = data['data']['wallet']['id']
        moneybox_id = data['data']['id']
        try:
            """списание регулярного плтаежа"""
            result_pay = RegularOutcomeMethods.post_pay_regular_outcome(
                'string', wallet_id, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_pay, 422)
        finally:
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)
