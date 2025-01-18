import allure
from Subcategory.methods.subcategory_methods import SubcategoryMethods
from common_methods.checking import Checking
from Subcategory.methods.payloads import SubcategoryPayloads
category_id = 156


@allure.epic('Post/api/v1/subcategory/ - Создание новой подкатеогии - Проверка поля category_id')
class TestCreateSubcategoriesCategoryId:

    @allure.description('Проверка поля category_id - Cуществующая категория')
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

    @allure.description('Проверка поля category_id - Несуществующая категория')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(1000, 'desc', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 404)

    @allure.description('Проверка поля category_id - НЗначение category_id = 0')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(0, 'desc', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля category_id - Значение category_id = отрицательное число')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(0, 'desc', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля category_id - Значение category_id = пустое поле')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory('', 'desc', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля category_id - Значение category_id = Null')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(None, 'desc', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля category_id - Поле category_id = отсутствует')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory_without_category_id('desc', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля category_id - Неверный тип данных string')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory('string', 'desc', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)
