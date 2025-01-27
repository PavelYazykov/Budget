import allure
import pytest
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking
from Subcategory.methods.subcategory_methods import SubcategoryMethods


@pytest.mark.Regular_outcome
@allure.epic(
    'Patch/api/v1/regular_outcome/{regular_outcome}/ Редактирование регулярного платежа - проверка поля subcategory_id'
)
class TestPatchRegularOutcomeSubategoryId:

    @allure.description('проверка поля subcategory_id - Существующий id')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание подкатегории"""
        subcategory_result = SubcategoryMethods.create_subcategory(
            156, 'desr', access_token
        )
        Checking.check_statuscode(subcategory_result, 201)
        data = Checking.get_data(subcategory_result)
        subcategory_id = data['data']['id']
        print('Sub', subcategory_id)

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
                regular_outcome_id, 'title', 156, subcategory_id, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля subcategory_id"""
            patch_data = Checking.get_data(result_patch)
            assert patch_data['data']['subcategory_id'] == subcategory_id
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

            delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('проверка поля category_id - Поле отсутствует')
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
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, 'title', 156, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля subcategory_id - Null')
    def test_03(self, auth_fixture):
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
                regular_outcome_id, 'title', 156, None, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля subcategory_id"""
            patch_data = Checking.get_data(result_patch)
            assert patch_data['data']['subcategory_id'] is None
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля subcategory_id - Несуществующий id')
    def test_04(self, auth_fixture):
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
                regular_outcome_id, 'title', 156, 1000, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 404)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля subcategory_id - Значение id = 0')
    def test_05(self, auth_fixture):
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
                regular_outcome_id, 'title', 156, 0, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля subcategory_id - Отрицательное значение')
    def test_06(self, auth_fixture):
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
                regular_outcome_id, 'title', 156, -20, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля subcategory_id - Пустое полe')
    def test_07(self, auth_fixture):
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
                regular_outcome_id, 'title', 156, '', 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля subcategory_id - Неверный тип данных string')
    def test_08(self, auth_fixture):
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
                regular_outcome_id, 'title', 156, 'string', 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля subcategory_id - Вещественное число')
    def test_09(self, auth_fixture):
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
                regular_outcome_id, 'title', 156, 1.1, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
