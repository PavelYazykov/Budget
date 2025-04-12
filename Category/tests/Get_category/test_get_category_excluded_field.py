import allure
import pytest

from common_methods.checking import Checking
from Category.methods.category_methods import CategoryMethods
from Category.methods.payloads import CategoryPayloads


@pytest.mark.Category
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

    @allure.description('проверка поля excluded - Список существующих названий категорий') # 'Покупки,Недвижимость' без квадратных скоюок и кавычек
    def test_02(self, auth_fixture):
        """Авторизацтя"""
        access_token = auth_fixture

        """Запрос на получение категорий"""
        result = CategoryMethods.get_category_with_excluded('Покупки,Недвижимость', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

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

        """Проверка что все категории остались"""
        try:
            missing_titles = CategoryPayloads.check_titles(result, CategoryPayloads.category_list)
        except KeyError as e:
            print(f"Поле 'title' отсутствует в одном из элементов: {e}")
        else:
            if missing_titles:
                print(f'Отсутствуют следующие title: {", ".join(missing_titles)}')
            else:
                print("Все title присутствуют")

    @allure.description('проверка поля excluded - Код категории')
    def test_04(self, auth_fixture):
        """Авторизацтя"""
        access_token = auth_fixture

        """Запрос на получение категорий"""
        result = CategoryMethods.get_category_with_excluded(20, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка что все категории остались"""
        try:
            missing_titles = CategoryPayloads.check_titles(result, CategoryPayloads.category_list)
        except KeyError as e:
            print(f"Поле 'title' отсутствует в одном из элементов: {e}")
        else:
            if missing_titles:
                print(f'Отсутствуют следующие title: {", ".join(missing_titles)}')
            else:
                print("Все title присутствуют")

    @allure.description('проверка поля excluded - Пустое поле')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на получение категорий"""
        result = CategoryMethods.get_category_with_excluded('', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка что все категории остались"""
        try:
            missing_titles = CategoryPayloads.check_titles(result, CategoryPayloads.category_list)
        except KeyError as e:
            print(f"Поле 'title' отсутствует в одном из элементов: {e}")
        else:
            if missing_titles:
                print(f'Отсутствуют следующие title: {", ".join(missing_titles)}')
            else:
                print("Все title присутствуют")

    @allure.description('проверка поля excluded - Null')
    def test_06(self, auth_fixture):
        """Авторизацтя"""
        access_token = auth_fixture

        """Запрос на получение категорий"""
        result = CategoryMethods.get_category_with_excluded(None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка что все категории остались"""
        try:
            missing_titles = CategoryPayloads.check_titles(result, CategoryPayloads.category_list)
        except KeyError as e:
            print(f"Поле 'title' отсутствует в одном из элементов: {e}")
        else:
            if missing_titles:
                print(f'Отсутствуют следующие title: {", ".join(missing_titles)}')
            else:
                print("Все title присутствуют")

    @allure.description('проверка поля excluded - Неверный тип данных')
    def test_07(self, auth_fixture):
        """Авторизацтя"""
        access_token = auth_fixture

        """Запрос на получение категорий"""
        result = CategoryMethods.get_category_with_excluded(1235, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка что все категории остались"""
        try:
            missing_titles = CategoryPayloads.check_titles(result, CategoryPayloads.category_list)
        except KeyError as e:
            print(f"Поле 'title' отсутствует в одном из элементов: {e}")
        else:
            if missing_titles:
                print(f'Отсутствуют следующие title: {", ".join(missing_titles)}')
            else:
                print("Все title присутствуют")
