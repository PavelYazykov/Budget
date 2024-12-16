import allure

from Settings.methods.settings_methods import SettingsMethods
from common_methods.checking import Checking
from Settings.methods.payloads import SettingsPayloads
from common_methods.variables import AuthVariables


@allure.epic('Post/api/v1/settings/contact_to_admin/ Связь с администратором проверка поля message_topic')
class TestContactAdminMessageTopic:

    @allure.description('message_topic - 10 символов')
    def test_01(self):

        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email, 'qwertyuiop', SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('message_topic - 49 символов')
    def test_02(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email,
            'qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuio',
            SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('message_topic - 50 символов')
    def test_03(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email,
            'qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop',
            SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('message_topic - цифры')
    def test_04(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email,
            '1234567890123',
            SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('message_topic - Кириллица')
    def test_05(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email,
            'Кириллицааааа',
            SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('message_topic - Латиница')
    def test_06(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email,
            'Latinlatin',
            SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('message_topic - Пробел')
    def test_07(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email,
            'Latin latin',
            SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('message_topic - Нижнее подчеркивание')
    def test_08(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email,
            'Latin_latin',
            SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('message_topic - тире')
    def test_09(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email,
            'Latin-latin',
            SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('message_topic - точка')
    def test_10(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email,
            'Latin.latin',
            SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка ответа"""
        data = Checking.get_data(result)
        assert data['message'] == 'Request sent successfully'

    @allure.description('message_topic - Null')
    def test_11(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email,
            None,
            SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('message_topic - 09 символов')
    def test_12(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email,
            '123456789',
            SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('message_topic - 51 символ')
    def test_13(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email,
            'qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopq',
            SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('message_topic - спецсимволы')
    def test_14(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email,
            '!@#$%^^&*$#@%^&',
            SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('message_topic - Пустое поле')
    def test_15(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email,
            '',
            SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('message_topic - Поле отсутствует')
    def test_16(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth_message_topic(
            AuthVariables.email,
            SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('message_topic - Неверный тип данных integer')
    def test_17(self):
        """Отправка запроса"""
        result = SettingsMethods.post_contact_to_admin_without_auth(
            AuthVariables.email,
            12345678978654123,
            SettingsPayloads.message
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)



