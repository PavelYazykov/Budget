import allure

from common_methods.checking import Checking
from common_methods.http_methods import HttpMethods
from common_methods.variables import CommonVariables


class NotificationsMethods:

    @staticmethod
    def get_notifications(user_id, local_date, access_token):
        with allure.step('Получение списка уведомлений о регулярных платежах'):
            endpoint = '/api/v1/notification/get/regular'
            user_id = f'?user_id={user_id}'
            local_date = f'&local_date={local_date}'
            get_url = CommonVariables.base_url + endpoint + user_id + local_date
            result = HttpMethods.get(get_url, access_token)
            return result

