import requests


class HttpMethods:

    @staticmethod
    def get(url, access_token):
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {access_token}"}
        result = requests.get(url, headers=headers)
        return result

    @staticmethod
    def get_without_auth(url):
        headers = {"Content-Type": "application/json"}
        result = requests.get(url, headers=headers)
        return result

    @staticmethod
    def post(url, body, access_token):
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {access_token}"}
        result = requests.post(url, json=body, headers=headers)
        return result

    @staticmethod
    def post_without_auth(url, body):
        headers = {"Content-type": "application/json"}
        result = requests.post(url, json=body, headers=headers)
        return result

    @staticmethod
    def post_without_body(url, access_token):
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {access_token}"}
        result = requests.post(url, headers=headers)
        return result

    @staticmethod
    def patch(url, body, access_token):
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {access_token}"}
        result = requests.patch(url, json=body, headers=headers)
        return result

    @staticmethod
    def patch_without_auth(url, body):
        headers = {"Content-Type": "application/json"}
        result = requests.patch(url, json=body, headers=headers)
        return result

    @staticmethod
    def patch_without_body(url, access_token):
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {access_token}"}
        result = requests.patch(url, headers=headers)
        return result

    @staticmethod
    def delete(url, access_token):
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {access_token}"}
        result = requests.delete(url, headers=headers)
        return result
