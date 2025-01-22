import allure
import pytest

from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking


@pytest.mark.Regular_outcome
@allure.epic('Post/api/v1/regular_outcome/ - Создание нового объекта регулярных списаний - проверка поля is_paid_off')
class TestRegularOutcomeIsPaidOff:

    @allure.description('проверка поля is_paid_off - Значение True')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 156, None, 'day', 100, True,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Проверка значения поля is_paid_off"""
            assert data['data']['is_paid_off'] is True
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)