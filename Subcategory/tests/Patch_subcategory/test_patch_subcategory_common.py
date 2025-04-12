import allure
import pytest

from Subcategory.methods.subcategory_methods import SubcategoryMethods
from common_methods.checking import Checking
from Subcategory.methods.payloads import SubcategoryPayloads
category_id = 30


@pytest.mark.Subcategory
@allure.epic('Patch/api/v1/subcategory/ - Редактирование подкатегории по id')
class TestPatchSubcategoryCommon:

    @allure.description('Редактирование подкатегории с валидными данными')
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
            result = SubcategoryMethods.change_subcategory(subcategory_id, 'title', False, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get_by_id(result, SubcategoryPayloads.get_payloads_by_id)

            """Проверка значений"""
            data = Checking.get_data(result)
            assert data['data']['title'] == 'title'
            assert data['data']['is_archived'] is False
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Редактирование подкатегории - oтправка запроса без body')
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
            result = SubcategoryMethods.change_subcategory_without_body(subcategory_id, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result, 422)
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

