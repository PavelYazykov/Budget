import allure
from common_methods.checking import Checking
from Category.methods.category_methods import CategoryMethods
from Category.methods.payloads import CategoryPayloads


@allure.epic('Get/api/v1/category/ Получение списка категорий - проверка поля excluded')
class TestGetCategoryExcluded:

    @allure.description('проверка поля excluded - Существующее название категории')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на получение категорий"""
        result = CategoryMethods.get_category_with_excluded('Недвижимость', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия исключенных категорий"""
        CategoryPayloads.check_excluded_category(result, 'Недвижимость')

    @allure.description('проверка поля excluded - Список существующих названий категорий')
    def test_02(self, auth_fixture):
        """Авторизацтя"""
        access_token = auth_fixture

        """Запрос на получение категорий"""
        result = CategoryMethods.get_category_with_excluded(['Покупки', 'Недвижимость'], access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)
        # data = Checking.get_data(result)
        # for i in data['data']:
        #     print(i['title'])
        #
        """Проверка наличия исключенных категорий"""
        CategoryPayloads.check_excluded_category_list(result, ['Покупки', 'Недвижимость'])

    @allure.description('проверка поля excluded - Несуществующее название категории')
    def test_03(self, auth_fixture):
        """Авторизацтя"""
        access_token = auth_fixture

        """Запрос на получение категорий"""
        result = CategoryMethods.get_category_with_excluded('Покуп', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия исключенных категорий"""
        print(result.json())

    @allure.description('проверка поля excluded - Код категории')
    def test_04(self, auth_fixture):
        """Авторизацтя"""
        access_token = auth_fixture

        """Запрос на получение категорий"""
        result = CategoryMethods.get_category_with_excluded(136, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия исключенных категорий"""
        print(result.json())

    @allure.description('проверка поля excluded - Пустое поле')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на получение категорий"""
        result = CategoryMethods.get_category_with_excluded('', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия исключенных категорий"""
        print(result.json())

    @allure.description('проверка поля excluded - Null')
    def test_06(self, auth_fixture):
        """Авторизацтя"""
        access_token = auth_fixture

        """Запрос на получение категорий"""
        result = CategoryMethods.get_category_with_excluded(None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия исключенных категорий"""
        print(result.json())

    @allure.description('проверка поля excluded - Неверный тип данных')
    def test_07(self, auth_fixture):
        """Авторизацтя"""
        access_token = auth_fixture

        """Запрос на получение категорий"""
        result = CategoryMethods.get_category_with_excluded(1235, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия исключенных категорий"""
        print(result.json())