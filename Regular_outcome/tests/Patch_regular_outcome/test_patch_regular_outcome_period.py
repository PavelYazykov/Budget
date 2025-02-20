import allure
import pytest
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking


@pytest.mark.Regular_outcome
@allure.epic(
    'Patch/api/v1/regular_outcome/{regular_outcome}/ Редактирование регулярного платежа - проверка поля period'
)
class TestPatchRegularOutcomePeriod:

    @allure.description('проверка поля period - day')
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
            """Запрос на изменение платежа"""
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, 'title', 20, 'day', 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля period"""
            patch_data = Checking.get_data(result_patch)
            assert patch_data['data']['period'] == 'day'
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля period - week')
    def test_02(self, auth_fixture):
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
            """Запрос на изменение платежа"""
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, 'title', 20, 'week', 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля period"""
            patch_data = Checking.get_data(result_patch)
            assert patch_data['data']['period'] == 'week'
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля period - month')
    def test_03(self, auth_fixture):
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
            """Запрос на изменение платежа"""
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, 'title', 20, 'month', 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля period"""
            patch_data = Checking.get_data(result_patch)
            assert patch_data['data']['period'] == 'month'
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля period - year')
    def test_04(self, auth_fixture):
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
            """Запрос на изменение платежа"""
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, 'title', 20, 'year', 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля period"""
            patch_data = Checking.get_data(result_patch)
            assert patch_data['data']['period'] == 'year'
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля period - onetime')
    def test_05(self, auth_fixture):
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
            """Запрос на изменение платежа"""
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, 'title', 20, 'onetime', 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля period"""
            patch_data = Checking.get_data(result_patch)
            assert patch_data['data']['period'] == 'onetime'
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля period - поле отсутствует')
    def test_06(self, auth_fixture):
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
            """Запрос на изменение платежа"""
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id_and_period(
                regular_outcome_id, 'title', 20, 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля period - Несуществующее значение')
    def test_07(self, auth_fixture):
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
            """Запрос на изменение платежа"""
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, 'title', 20, 'Two', 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля period - Пуcтое поле')
    def test_08(self, auth_fixture):
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
            """Запрос на изменение платежа"""
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, 'title', 20, '', 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля period - Null')
    def test_09(self, auth_fixture):
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
            """Запрос на изменение платежа"""
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, 'title', 20, None, 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)