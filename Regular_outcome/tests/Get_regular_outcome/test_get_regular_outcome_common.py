import allure
import pytest

from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking


@pytest.mark.Regular_outcome
@allure.epic('Get/api/v1/regular_outcome/ - Получение всех регулярных списаний - Общие проверки')
class TestGetRegularOutcomeCommon:

    @allure.description('Проверка поля is_paid_off - Значение True')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result_create = RegularOutcomeMethods.create_regular_outcome(
            'title', 156, None, 'day', 100, False,
            '2030-12-12', access_token,
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        regular_outcome_id = data['data']['id']

        try:
            """Запрос на получение списка"""
            result_get = RegularOutcomeMethods.get_regular_outcome(access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Общие проверки - Получение списка регулярных списаний с валидными данными и спараметрами')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result_create = RegularOutcomeMethods.create_regular_outcome(
            'title', 156, None, 'day', 100, False,
            '2030-12-12', access_token,
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        regular_outcome_id = data['data']['id']

        try:
            """Запрос на получение списка"""
            result_get = RegularOutcomeMethods.get_regular_outcome_with_params(
                False, 1, 1, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

