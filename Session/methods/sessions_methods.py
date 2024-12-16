import allure
from common_methods.variables import CommonVariables
from common_methods.http_methods import HttpMethods
base_url = CommonVariables.base_url


class SessionsMethods:

    @staticmethod
    def get_active_sessions(access_token):
        with allure.step('Получение списка активных сессий'):
            endpoint = '/auth/active_sessions'
            get_url = base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_active_sessions_without_auth():
        with allure.step('Получение списка активных сессий'):
            endpoint = '/auth/active_sessions'
            get_url = base_url + endpoint
            result = HttpMethods.get_without_auth(get_url)
            return result

    @staticmethod
    def remote_logout(device_id, access_token):
        with allure.step('Отзыв refresh token переданного устройства пользователя.'):
            endpoint = f'/auth/remote_logout/{device_id}'
            post_url = base_url + endpoint
            result = HttpMethods.post_without_body(post_url, access_token)
            return result

    @staticmethod
    def remote_logout_without_device(access_token):
        with allure.step('Отзыв refresh token переданного устройства пользователя.'):
            endpoint = f'/auth/remote_logout/'
            post_url = base_url + endpoint
            result = HttpMethods.post_without_body(post_url, access_token)
            return result

    @staticmethod
    def logout_all(except_device, access_token):
        with allure.step('Отзыв всех refresh token текущего пользователя, кроме переданного устройства.'):
            endpoint = '/auth/logout_all'
            except_device = f'?except_device={except_device}'
            post_url = base_url + endpoint + except_device
            result = HttpMethods.post_without_body(post_url, access_token)
            return result

    @staticmethod
    def logout_all_without_device(access_token):
        with allure.step('Отзыв всех refresh token текущего пользователя, без поля except device'):
            endpoint = '/auth/logout_all'
            post_url = base_url + endpoint
            result = HttpMethods.post_without_body(post_url, access_token)
            return result
