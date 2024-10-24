import allure

from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking

old_password = 'Ohranatruda@2'


@allure.epic('Post_change_password Общие проверки')
class TestCommonCheck:

    @allure.description('Изменение пароля с валидными данными')
    def test_01(self, auth_fixture_2):
        """Авторизация"""
        access_token = auth_fixture_2

        """Запрос на изменение пароля"""
        result_change = AuthMethods.change_password(
            old_password, 'Ohranatruda@1', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 200)

        """Возврат старого пароля"""
        with allure.step('Возврат старого пароля'):
            result_change = AuthMethods.change_password(
                'Ohranatruda@1', 'Ohranatruda@2', access_token
            )
            Checking.check_statuscode(result_change, 200)

    @allure.description('Измененеие на текущий пароль')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на изменение пароля"""
        result_change = AuthMethods.change_password(
            old_password, 'Ohranatruda@2', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_change, 400)

    @allure.description('апрос со старым access_token')
    def test_03(self):
        """Запрос со старым access_token"""
        pass  # Доделать!
