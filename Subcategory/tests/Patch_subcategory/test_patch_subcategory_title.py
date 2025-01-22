import allure
import pytest

from Subcategory.methods.subcategory_methods import SubcategoryMethods
from common_methods.checking import Checking
from Subcategory.methods.payloads import SubcategoryPayloads
category_id = 156


@pytest.mark.Subcategory
@allure.epic('Patch/api/v1/subcategory/ - Редактирование подкатегории по id - Проверка поля title')
class TestPatchSubcategoryTitle:

    @allure.description('Проверка поля title - 1 символ')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Запрос на изменение информации о подкатегории"""
            result = SubcategoryMethods.change_subcategory(subcategory_id, 't', False, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get_by_id(result, SubcategoryPayloads.get_payloads_by_id)

            """Проверка значений"""
            data = Checking.get_data(result)
            assert data['data']['title'] == 't'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля title - 19 символов')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Запрос на изменение информации о подкатегории"""
            result = SubcategoryMethods.change_subcategory(
                subcategory_id, 'ttttttttttwwwwwwwww', False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get_by_id(result, SubcategoryPayloads.get_payloads_by_id)

            """Проверка значений"""
            data = Checking.get_data(result)
            assert data['data']['title'] == 'ttttttttttwwwwwwwww'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля title - 20 символов')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Запрос на изменение информации о подкатегории"""
            result = SubcategoryMethods.change_subcategory(
                subcategory_id, 'ttttttttttwwwwwwwwwq', False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get_by_id(result, SubcategoryPayloads.get_payloads_by_id)

            """Проверка значений"""
            data = Checking.get_data(result)
            assert data['data']['title'] == 'ttttttttttwwwwwwwwwq'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля title - Цифры')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Запрос на изменение информации о подкатегории"""
            result = SubcategoryMethods.change_subcategory(
                subcategory_id, '123456', False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get_by_id(result, SubcategoryPayloads.get_payloads_by_id)

            """Проверка значений"""
            data = Checking.get_data(result)
            assert data['data']['title'] == '123456'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля title - Кириллица')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Запрос на изменение информации о подкатегории"""
            result = SubcategoryMethods.change_subcategory(
                subcategory_id, 'фыва', False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get_by_id(result, SubcategoryPayloads.get_payloads_by_id)

            """Проверка значений"""
            data = Checking.get_data(result)
            assert data['data']['title'] == 'фыва'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля title - Латиница')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Запрос на изменение информации о подкатегории"""
            result = SubcategoryMethods.change_subcategory(
                subcategory_id, 'qwerty', False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get_by_id(result, SubcategoryPayloads.get_payloads_by_id)

            """Проверка значений"""
            data = Checking.get_data(result)
            assert data['data']['title'] == 'qwerty'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля title - Пробел')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Запрос на изменение информации о подкатегории"""
            result = SubcategoryMethods.change_subcategory(
                subcategory_id, 'qwert y', False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get_by_id(result, SubcategoryPayloads.get_payloads_by_id)

            """Проверка значений"""
            data = Checking.get_data(result)
            assert data['data']['title'] == 'qwert y'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля title - Нижнее подчеркивание')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Запрос на изменение информации о подкатегории"""
            result = SubcategoryMethods.change_subcategory(
                subcategory_id, 'qwert_y', False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get_by_id(result, SubcategoryPayloads.get_payloads_by_id)

            """Проверка значений"""
            data = Checking.get_data(result)
            assert data['data']['title'] == 'qwert_y'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля title - Тире')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Запрос на изменение информации о подкатегории"""
            result = SubcategoryMethods.change_subcategory(
                subcategory_id, 'qwert-y', False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get_by_id(result, SubcategoryPayloads.get_payloads_by_id)

            """Проверка значений"""
            data = Checking.get_data(result)
            assert data['data']['title'] == 'qwert-y'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля title - Точка')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Запрос на изменение информации о подкатегории"""
            result = SubcategoryMethods.change_subcategory(
                subcategory_id, 'qwert.y', False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get_by_id(result, SubcategoryPayloads.get_payloads_by_id)

            """Проверка значений"""
            data = Checking.get_data(result)
            assert data['data']['title'] == 'qwert.y'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля title - Поле отсутствует')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Запрос на изменение информации о подкатегории"""
            result = SubcategoryMethods.change_subcategory_without_title(
                subcategory_id, False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get_by_id(result, SubcategoryPayloads.get_payloads_by_id)

        except AssertionError:
            raise AssertionError
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля title - Null')
    def test_12(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Запрос на изменение информации о подкатегории"""
            result = SubcategoryMethods.change_subcategory(
                subcategory_id, None, False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)

        except AssertionError:
            raise AssertionError
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля title - 21 символ')
    def test_13(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Запрос на изменение информации о подкатегории"""
            result = SubcategoryMethods.change_subcategory(
                subcategory_id, 'qqqqqqqqqqwqqqqqqqqqw', False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)

        except AssertionError:
            raise AssertionError
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля title - Пустое поле')
    def test_14(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Запрос на изменение информации о подкатегории"""
            result = SubcategoryMethods.change_subcategory(
                subcategory_id, '', False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)

        except AssertionError:
            raise AssertionError
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля title - Неверный тип данный integer')
    def test_15(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Запрос на изменение информации о подкатегории"""
            result = SubcategoryMethods.change_subcategory(
                subcategory_id, 123456, False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)

        except AssertionError:
            raise AssertionError
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля title - Спецсимволы')
    def test_16(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Запрос на изменение информации о подкатегории"""
            result = SubcategoryMethods.change_subcategory(
                subcategory_id, '!@#$%^&*', False, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)

        except AssertionError:
            raise AssertionError
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)
