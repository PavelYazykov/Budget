import allure
import pytest

from Settings.methods.settings_methods import SettingsMethods
from common_methods.checking import Checking
from Settings.methods.payloads import SettingsPayloads
from common_methods.variables import AuthVariables


@pytest.mark.Settings
@allure.epic('Post/api/v1/settings/contact_to_admin/ Связь с администратором проверка поля message')
class TestContactAdminMessage:

    @allure.description('проверка поля message - 20 символов')
    def test_01(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email, 'message_topic', 'qwertyuiopqwertyuiop'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('проверка поля message - 20000 символов')
    def test_02(self):
        """Отправка запроса"""
        message = SettingsMethods.randstr('qwertyu', 20000)
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email, 'message_topic', message,)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('проверка поля message - Пробел')
    def test_03(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email, 'message_topic', 'qwertqwert yuiopqyuiopq'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('проверка поля message - Спецсимволы')
    def test_04(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email, 'message_topic', 'messagemessage@#$%^&^&@#$%%^%$#@##$$'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('проверка поля message - Латиница')
    def test_05(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email, 'message_topic', 'messagemessagemessagemessage'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('проверка поля message - Кириллица')
    def test_06(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email, 'message_topic', 'КириллицаКириллицаКириллицаКириллицаКириллица'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('проверка поля message - Латиница + Латиница')
    def test_07(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email, 'message_topic', 'ЛатиницаЛатиницаLatinLatin'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('проверка поля message - 19 символов')
    def test_08(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email, 'message_topic', 'qwertyuiopqwertyuio'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля message -  более 20000 символов')
    def test_09(self):
        """Отправка запроса"""
        message = SettingsMethods.randstr('qwertyu', 20001)
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email, 'message_topic', message, )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля message - Пустое поле')
    def test_10(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email, 'message_topic', ''
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля message - Поле отсутствует')
    def test_11(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth_message(
            AuthVariables.email, 'message_topic'
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля message - Null')
    def test_12(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email, 'message_topic', None
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля message - Неверный тип данных integer')
    def test_13(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email, 'message_topic', 123456789123456789123456789
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

