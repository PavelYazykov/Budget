import allure

from Settings.methods.settings_methods import SettingsMethods
from common_methods.checking import Checking
from Settings.methods.payloads import SettingsPayloads


@allure.epic('Patch/api/v1/settings/my/ Настройки пользователя - Проверка поля excluded_categories')
class TestPatchSettingsExcludedCategories:

    @allure.description('поле excluded_categories - Существующее значение')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            True, True, 2, ['Продукты и хозтовары'],
            access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения поля analytics"""
        data = Checking.get_data(result)
        assert data['data']['excluded_categories'][0] == 'Продукты и хозтовары'

    @allure.description('поле excluded_categories - Список существующих категорий категорий')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            True, True, 2,
            ['Продукты и хозтовары', 'Недвижимость'], access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения поля analytics"""
        data = Checking.get_data(result)
        print(data['data']['excluded_categories'])
        assert data['data']['excluded_categories'] == ['Продукты и хозтовары', 'Недвижимость']

    @allure.description('поле excluded_categories - Список категорий, одну существующее знпчение, второе нет')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            True, True, 2,
            ['Продукты и хозтовары', 'Самолеты'], access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('поле excluded_categories - несуществующее значение')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            True, True, 2, ['Прод и хозтовары'],
            access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('поле excluded_categories - Null')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            True, True, 2, None,
            access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения поля analytics"""
        data = Checking.get_data(result)
        assert data['data']['excluded_categories'] is None

    @allure.description('поле excluded_categories - Пустое поле')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            True, True, 2, '',
            access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('поле excluded_categories - Поле отсутствует')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings_without_excluded_categories(
            False, True, True, True, True,
            True, True, 2, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('поле excluded_categories - Неверный тип данных integer')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Отправка запроса"""
        result = SettingsMethods.patch_settings(
            False, True, True, True, True,
            True, True, 2, 123456,
            access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)


