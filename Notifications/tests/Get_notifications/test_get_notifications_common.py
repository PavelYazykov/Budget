import allure

from Notifications.methods.notifications_methods import NotificationsMethods
from common_methods.checking import Checking
from Users.methods.users_methods import UsersMethods
from datetime import datetime
current_date = datetime.now()


@allure.epic('Get/api/v1/notification/get/regular - Получение списка уведомлений о регулярных платежах - общие проверки')
class TestGetNotifications:

    @allure.description('Oбщие проверки - Запрос списка уведомлений регулярных платежей авторизованный пользователь')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Получение информации о пользователе"""
        get_user = UsersMethods.get_user(access_token)
        data = Checking.get_data(get_user)
        user_id = data['id']
        print(user_id)

        """Запрос списка регудярных платежей"""
        result = NotificationsMethods.get_notifications(user_id, '2025-01-25', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)


