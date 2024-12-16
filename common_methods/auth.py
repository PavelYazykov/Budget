import allure
import requests
from common_methods.variables import AuthVariables
from common_methods.variables import CommonVariables


class Auth:
    """Авторизация пользователя"""
    @staticmethod
    def auth():
        with allure.step('Авторизация'):
            base_url = CommonVariables.base_url + '/auth/jwt/login'
            device_id = '?device_id=11111'
            auth_url = base_url + device_id
            body = AuthVariables.auth_payloads
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }

            post_response = requests.post(auth_url, headers=headers, data=body)
            return post_response

    @staticmethod
    def auth_with_params(device_id, payloads):
        with allure.step('Авторизация с выбором устройства и пользователя'):
            base_url = CommonVariables.base_url + '/auth/jwt/login'
            device_id = f'?device_id={device_id}'
            auth_url = base_url + device_id
            body = payloads
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }

            post_response = requests.post(auth_url, headers=headers, data=body)
            return post_response

