import allure
import pytest

from Payment_info.methods.payment_info_methods import PaymentInfoMethods
from Payment_info.methods.payloads import Payloads
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking


@pytest.mark.Payment_info
@allure.epic('Get/api/v1/payment_info/ - Запрос объектов payment_info - проверка поля paid_off_date')
class TestGetPaymentInfoPaidOffDate:

    @allure.description('проверка поля paid_off_date  - Значение True')
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

        PaymentInfoMethods.create_regular_outcome('2025-01-12', regular_outcome_id)
        try:

            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-01-12', None, False, 111
            )

            """Запрос информации о платеже"""
            get_result = PaymentInfoMethods.get_payment_info_with_params(
                '?paid_off_date=true', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(get_result, 200)

            """Проверка что данных не отображаются"""
            data = Checking.get_data(get_result)
            print('L', data['data'])
            assert len(data['data']) == 0
            assert data['data'] == []
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

    @allure.description('проверка поля paid_off_date  - Значение False')
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

        PaymentInfoMethods.create_regular_outcome('2025-01-12', regular_outcome_id)
        try:

            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-01-12', None, False, 111
            )

            """Запрос информации о платеже"""
            get_result = PaymentInfoMethods.get_payment_info_with_params(
                '?paid_off_date=false', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(get_result, 200)

            """Проверка наличия всех полей"""
            Payloads.check_required_fields_for_get_request(get_result, Payloads.get_payloads)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

    @allure.description('проверка поля paid_off_date  - Поле отсутствует')
    def test_03(self, auth_fixture):
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

        PaymentInfoMethods.create_regular_outcome('2025-01-12', regular_outcome_id)
        try:

            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-01-12', None, False, 111
            )

            """Запрос информации о платеже"""
            get_result = PaymentInfoMethods.get_payment_info_with_params(
                '?month=1', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(get_result, 200)

            """Проверка наличия всех полей"""
            Payloads.check_required_fields_for_get_request(get_result, Payloads.get_payloads)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

    @allure.description('проверка поля paid_off_date  - Пустое поле')
    def test_04(self, auth_fixture):
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

        PaymentInfoMethods.create_regular_outcome('2025-01-12', regular_outcome_id)
        try:

            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-01-12', None, False, 111
            )

            """Запрос информации о платеже"""
            get_result = PaymentInfoMethods.get_payment_info_with_params(
                '?paid_off_date=""', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(get_result, 422)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)

    @allure.description('проверка поля paid_off_date  - Недопустимое значение')
    def test_05(self, auth_fixture):
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

        PaymentInfoMethods.create_regular_outcome('2025-01-12', regular_outcome_id)
        try:

            """Создание просроченного платежа"""
            PaymentInfoMethods.create_payment_info_in_bd(
                regular_outcome_id, 10, '2025-01-12', None, False, 111
            )

            """Запрос информации о платеже"""
            get_result = PaymentInfoMethods.get_payment_info_with_params(
                '?paid_off_date=date', access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(get_result, 422)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление регулярного платежа"""
            delete_regular_outcome = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_regular_outcome, 204)