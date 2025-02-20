import allure
import pytest
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking


@pytest.mark.Regular_outcome
@allure.epic(
    'Patch/api/v1/regular_outcome/{regular_outcome}/ Редактирование регулярного платежа - проверка поля category_id'
)
class TestPatchRegularOutcomeCategoryId:

    @allure.description('проверка поля category_id - Существующий id')
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
                regular_outcome_id, 'title', 20, 'week', 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля category_id"""
            patch_data = Checking.get_data(result_patch)
            assert patch_data['data']['category_id'] == 20
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля category_id - Поле отсутствует')
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
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id_and_category_id(
                regular_outcome_id, 'title', 'week', 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля category_id - Null')
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
                regular_outcome_id, 'title', None, 'week', 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля category_id - Несуществующий id')
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
                regular_outcome_id, 'title', 1030, 'week', 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 404)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля category_id - Значение id = 0')
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
                regular_outcome_id, 'title', 0, 'week', 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля category_id - Отрицательное значение')
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
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, 'title', -20, 'week', 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля category_id - Пустое поле')
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
                regular_outcome_id, 'title', '', 'week', 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля category_id - Неверный тип данных string')
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
                regular_outcome_id, 'title', 'string', 'week', 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля category_id - Вещественное число')
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
                regular_outcome_id, 'title', 1.1, 'week', 100,
                access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)