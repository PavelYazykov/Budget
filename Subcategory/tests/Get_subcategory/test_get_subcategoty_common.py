import allure
import pytest

from Subcategory.methods.subcategory_methods import SubcategoryMethods
from common_methods.checking import Checking


@pytest.mark.Subcategory
@allure.epic('Get/api/v1/subcategory/ - Получение списка всех подкатегорий без параметров')
class TestGetAllSubcategoriesCommon:

    @allure.description('Получение списка всех подкатегорий без параметров - авторизованный пользователь')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(30, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Get запрос"""
            result_get = SubcategoryMethods.get_subcategory(access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
            data = Checking.get_data(result_get)
            category_id = data['data'][0]['category_id']
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Получение списка всех подкатегорий без параметров - неавторизованный пользователь')
    def test_02(self):

        """Get запрос"""
        result = SubcategoryMethods.get_subcategory_without_auth()

        """Проверка статус кода"""
        Checking.check_statuscode(result, 401)


