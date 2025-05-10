import allure
import pytest

from Payment_info.methods.payment_info_methods import PaymentInfoMethods
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking


@pytest.mark.payment_info
@allure.epic('Delete/api/v1/payment_info/{debt_id}/ - Удаление объекта payment_info по id')
class TestDeletePaymentInfo:

    @allure.description('Удаление объекта payment_info по id - Cуществующий payment_info_id')
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

            """Удаление платежа"""
            result_delete = PaymentInfoMethods.delete_payment_info(111, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result_delete, 204)

            """Повторное удаление"""
            result_delete_2 = PaymentInfoMethods.delete_payment_info(111, access_token)
            Checking.check_statuscode(result_delete_2, 404)
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

    @allure.description('Удаление объекта payment_info по id - Несуществующая  payment_info_id')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление платежа"""
        result_delete = PaymentInfoMethods.delete_payment_info(1111, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 404)

    @allure.description('Удаление объекта payment_info по id - Значение  payment_info_id = 0')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление платежа"""
        result_delete = PaymentInfoMethods.delete_payment_info(0, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление объекта payment_info по id - Значение  payment_info_id = отрицательное число')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление платежа"""
        result_delete = PaymentInfoMethods.delete_payment_info(-111, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление объекта payment_info по id - Значение  payment_info_id = пустое поле')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление платежа"""
        result_delete = PaymentInfoMethods.delete_payment_info('', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 404)

    @allure.description('Удаление объекта payment_info по id - Значение  payment_info_id = Null')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление платежа"""
        result_delete = PaymentInfoMethods.delete_payment_info(None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление объекта payment_info по id - Значение  payment_info_id = Null')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление платежа"""
        result_delete = PaymentInfoMethods.delete_payment_info(None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление объекта payment_info по id - Неверный тип данных')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление платежа"""
        result_delete = PaymentInfoMethods.delete_payment_info('12sd', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)
