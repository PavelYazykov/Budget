import allure
import pytest
from Regular_outcome.methods.payloads import RegularOutcomePayloads
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking


@pytest.mark.Regular_outcome
@allure.epic('Patch/api/v1/regular_outcome/{regular_outcome}/ - Редактирование регулярного платежа - общие проверки')
class TestPatchRegularOutcomeCommon:

    @allure.description('Oбщие проверки - Изменение c валидными данными')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 156, None, 'day', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос на изменение платежа"""
            result_patch = RegularOutcomeMethods.change_regular_outcome(
                regular_outcome_id, 'title_name', 156, None, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Oбщие проверки - Отправка запроса Без body')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 156, None, 'day', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос на изменение платежа"""
            result_patch = RegularOutcomeMethods.change_regular_outcome_without_body(regular_outcome_id, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

