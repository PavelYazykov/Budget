import allure
import pytest

from Subcategory.methods.subcategory_methods import SubcategoryMethods
from common_methods.checking import Checking
from Subcategory.methods.payloads import SubcategoryPayloads
category_id = 30


@pytest.mark.Subcategory
@allure.epic('Patch/api/v1/subcategory/ - Редактирование подкатегории по id - Проверка поля is_archived')
class TestPatchSubcategoryIsArchived:

    @allure.description('Проверка поля is_archived - Значение true')
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
            result = SubcategoryMethods.change_subcategory(subcategory_id, 'name', True, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get_by_id(result, SubcategoryPayloads.get_payloads_by_id)

            """Проверка значений"""
            data = Checking.get_data(result)
            assert data['data']['is_archived'] is True
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля is_archived - Значение false')
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
            result = SubcategoryMethods.change_subcategory(subcategory_id, 'name', False, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get_by_id(result, SubcategoryPayloads.get_payloads_by_id)

            """Проверка значений"""
            data = Checking.get_data(result)
            assert data['data']['is_archived'] is False
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля is_archived - Возврат подкатегории из архива')
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
            """Запрос на перевод подкатегории в архив"""
            result = SubcategoryMethods.change_subcategory(subcategory_id, 'name', True, access_token)
            Checking.check_statuscode(result, 200)

            """Проверка значений"""
            data = Checking.get_data(result)
            assert data['data']['is_archived'] is True

            """Запрос на возврат подкатегории из архива"""
            result = SubcategoryMethods.change_subcategory(subcategory_id, 'name', False, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get_by_id(result, SubcategoryPayloads.get_payloads_by_id)

            """Проверка значений"""
            data = Checking.get_data(result)
            assert data['data']['is_archived'] is False
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля is_archived - Поле отсутствует')
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
            result = SubcategoryMethods.change_subcategory_without_is_archived(subcategory_id, 'name', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get_by_id(result, SubcategoryPayloads.get_payloads_by_id)
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля is_archived - Значение Null')
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
            result = SubcategoryMethods.change_subcategory(subcategory_id, 'name', None, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля is_archived - Пустое поле')
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
            result = SubcategoryMethods.change_subcategory(subcategory_id, 'name', '', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля is_archived - Неверный тип данный integer')
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
            result = SubcategoryMethods.change_subcategory(subcategory_id, 'name', 123456, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля is_archived - Неверный тип данный string')
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
            result = SubcategoryMethods.change_subcategory(subcategory_id, 'name', 'string', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)
