import allure
import pytest

from Subcategory.methods.subcategory_methods import SubcategoryMethods
from common_methods.checking import Checking
from Subcategory.methods.payloads import SubcategoryPayloads
category_id = 30


@pytest.mark.Subcategory
@allure.epic('Post/api/v1/subcategory/ - Создание новой подкатеогии - общие проверки')
class TestCreateSubcategoriesCommon:

    @allure.description('Создание подкатегории с валидными данными')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'desc', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_required_fields_post(result_create, SubcategoryPayloads.post_payloads)
        except AssertionError:
            raise AssertionError
        finally:
            SubcategoryMethods.delete_subcategory(subcategory_id, access_token)

    @allure.description('Создание запроса без body')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory_without_body(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

