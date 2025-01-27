import allure
import pytest
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking


@pytest.mark.Regular_outcome
@allure.epic('Patch/api/v1/regular_outcome/{regular_outcome}/ Редактирование регулярного платежа - проверка поля title')
class TestPatchRegularOutcomeTitle:

    @allure.description('проверка поля title - 1 символ')
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
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, 't', 156, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля title"""
            patch_data = Checking.get_data(result_patch)
            assert patch_data['data']['title'] == 't'
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - 20 символов')
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
                regular_outcome_id, 'ttttttttttqqqqqqqqqq', 156, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля title"""
            patch_data = Checking.get_data(result_patch)
            assert patch_data['data']['title'] == 'ttttttttttqqqqqqqqqq'
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Цифры')
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
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, '123456', 156, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля title"""
            patch_data = Checking.get_data(result_patch)
            assert patch_data['data']['title'] == '123456'
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Кирилица')
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
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, 'йцуке', 156, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля title"""
            patch_data = Checking.get_data(result_patch)
            assert patch_data['data']['title'] == 'йцуке'
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Латиница')
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
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, 'qwerty', 156, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля title"""
            patch_data = Checking.get_data(result_patch)
            assert patch_data['data']['title'] == 'qwerty'
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Пробел')
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
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, 'qwert y', 156, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля title"""
            patch_data = Checking.get_data(result_patch)
            assert patch_data['data']['title'] == 'qwert y'
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Нижнее подчеркивание')
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
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, 'qwert_y', 156, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля title"""
            patch_data = Checking.get_data(result_patch)
            assert patch_data['data']['title'] == 'qwert_y'
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Тире')
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
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, 'qwert-y', 156, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля title"""
            patch_data = Checking.get_data(result_patch)
            assert patch_data['data']['title'] == 'qwert-y'
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Точка')
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
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
                regular_outcome_id, 'qwert.y', 156, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

            """Проверка значения поля title"""
            patch_data = Checking.get_data(result_patch)
            assert patch_data['data']['title'] == 'qwert.y'
        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Поле отсутствует')
    def test_10(self, auth_fixture):
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
            result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id_and_title(
                regular_outcome_id, 156, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 200)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Null')
    def test_11(self, auth_fixture):
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
                regular_outcome_id, 't', 156, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - 21 символ')
    def test_12(self, auth_fixture):
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
                regular_outcome_id, 'ttttttttttqqqqqqqqqqw', 156, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Пустое поле')
    def test_13(self, auth_fixture):
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
                regular_outcome_id, '', 156, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Неверный тип данный integer')
    def test_14(self, auth_fixture):
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
                regular_outcome_id, 12345, 156, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Спецсимволы')
    def test_15(self, auth_fixture):
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
                regular_outcome_id, '!@#$%', 156, 'week', 100,
                False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_patch, 422)

        except AssertionError:
            raise AssertionError

        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)