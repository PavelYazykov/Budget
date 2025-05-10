import allure
import pytest

from Analytics.methods.analytics_methods import AnalyticsMethods
from common_methods.checking import Checking
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods


@pytest.mark.Analytics
@allure.epic(
    'Get/api/v1/analytics/summary_by_outcomes - суммированные по категориям расходы по платежам за заданный период - '
    'Провнерка поля first day'
)
class TestSummaryByOutcomesFirstDay:

    @allure.description('Провнерка поля first_day - Дата в формате гггг-мм-дд (string)')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'week', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', '&first_day=2030-12-12&last_day=2030-12-31', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            print('Result', result_get.text)

            """Проверка типа транзакции"""
            data = Checking.get_data(result_get)
            assert data['meta']['outcome_type'] == 'all'
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Провнерка поля first_day - Null')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'week', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', '&first_day=null&last_day=2030-12-31', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Провнерка поля first_day - Поле отсутствует')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'week', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', '&last_day=2030-12-31', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Провнерка поля first_day - Недопустимые символы')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'week', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', '&first_day=@#$%&last_day=2030-12-31', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Провнерка поля first_day - Дата в формате гг-мм-дд')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'week', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', '&first_day=30-1-12&last_day=2030-12-31', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Провнерка поля first_day - Дата в формате гггг-м-дд')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'week', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', '&first_day=2030-1-30&last_day=2030-12-31', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Провнерка поля first_day - Дата в формате гггг-мм-д')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'week', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', '&first_day=2030-12-3&last_day=2030-12-31', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Провнерка поля first_day - Неверный порядок формата даты (дд-мм-гг)')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'week', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', '&first_day=30-12-2030&last_day=2030-12-31', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Провнерка поля first_day - Неверный разделитель в формате даты (гггг.мм.дд)')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'week', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', '&first_day=2030.12-12&last_day=2030-12-31', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Провнерка поля first_day - Пустое поле')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'week', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', '&first_day=""&last_day=2030-12-31', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Провнерка поля first_day - Дата вещественное число -> 11.0')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'week', 100, False,
            '2030-03-12', access_token,
        )
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос аналитики"""
            result_get = AnalyticsMethods.get_summary_by_outcomes_with_params(
                'all', '&first_day=2030-12.0-12&last_day=2030-12-31', access_token
            )

            """проверка статус кода"""
            Checking.check_statuscode(result_get, 422)

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

