import allure
import pytest

from Payment_info.methods.payment_info_methods import PaymentInfoMethods
from Payment_info.methods.payloads import Payloads
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking


@pytest.mark.payment_info
@allure.epic('Get/api/v1/payment_info/ - Запрос объектов payment_info - проверка поля regular_outcome_id')
class TestGetPaymentInfoRegularOutcomeId:

    @allure.description('проверка поля regular_outcome_id  - Существующий id')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

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

            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-04-12', None, False, 111
            )

            """Запрос информации о платеже"""
            get_result = PaymentInfoMethods.get_payment_info_with_params(
                f'?regular_outcome_id={regular_outcome_id}', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(get_result, 200)

            """Проверка наличия всех полей"""
            Payloads.check_required_fields_for_get_request(get_result, Payloads.get_payloads)

        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

    @allure.description('проверка поля regular_outcome_id  - Поле отсутствует')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

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

            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-04-12', None, False, 111
            )

            """Запрос информации о платеже"""
            get_result = PaymentInfoMethods.get_payment_info_with_params(
                f'?month=04', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(get_result, 200)

            """Проверка наличия всех полей"""
            Payloads.check_required_fields_for_get_request(get_result, Payloads.get_payloads)

        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

    @allure.description('проверка поля regular_outcome_id  - Несуществующий id')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос информации о платеже"""
        get_result = PaymentInfoMethods.get_payment_info_with_params(
            '?regular_outcome_id=5', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(get_result, 404)

    @allure.description('проверка поля regular_outcome_id  - Отрицательное значение id')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос информации о платеже"""
        get_result = PaymentInfoMethods.get_payment_info_with_params(
            '?regular_outcome_id=-5', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(get_result, 422)

    @allure.description('проверка поля regular_outcome_id  - Значение = 0')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос информации о платеже"""
        get_result = PaymentInfoMethods.get_payment_info_with_params(
            '?regular_outcome_id=0', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(get_result, 422)

    @allure.description('проверка поля regular_outcome_id  - Неверный тип данных string')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос информации о платеже"""
        get_result = PaymentInfoMethods.get_payment_info_with_params(
            '?regular_outcome_id=string', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(get_result, 422)
