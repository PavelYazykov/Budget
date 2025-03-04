import allure
import pytest

from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking
from Regular_outcome.methods.payloads import RegularOutcomePayloads


@pytest.mark.Regular_outcome
@allure.epic('Post/api/v1/regular_outcome/ - Создание нового объекта регулярных списаний - общие проверки')
class TestRegularOutcomeCommon:

    @allure.description('Создание объекта с валидными данными (авторизованный пользователь)')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            RegularOutcomePayloads.check_required_fields(result, RegularOutcomePayloads.post_payloads)
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Создание объекта с валидными данными (неавторизованный пользователь)')
    def test_02(self):

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome_without_access_token(
            'title', 20, None, 'day', 100, False,
            '2030-12-12'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 401)

    @allure.description('Создание объекта с валидными данными (авторизованный пользователь)')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome_without_body(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля is_paid_off - Поле отсутствует')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome_without_is_paid_off(
            'title', 20, None, 'day', 100,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
        Checking.check_statuscode(result_delete, 204)


