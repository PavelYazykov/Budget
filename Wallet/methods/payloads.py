import json

import allure


class WalletPayloads:
    get_payloads = {
        "meta": {},
        "data":
            {
              "name": "Title or description",
              "currency_id": 1,
              "is_archived": True,
              "amount": 100.55,
              "id": 1,
              "goal_is_achieved": True,
            }
    }

    patch_payloads = {
        "name": "wallet_name",
        "currency_id": 2,
        "is_archived": False
    }

    @staticmethod
    def check_required_fields_patch(result, required_fields):
        with allure.step('Проверка наличия обязательных полей'):
            resul_text = result.text
            data = json.loads(resul_text)

            for field in required_fields:
                assert field in data, f'поле {field} отсутствует'
            print('Все поля присутствуют')

    @staticmethod
    def check_required_fields(result, required_fields):
        with allure.step('Проверка наличия обязательных полей'):
            resul_text = result.text
            data = json.loads(resul_text)

            for field in required_fields:
                assert field in data, f'поле {field} отсутствует'

            for field in required_fields['data']:
                assert field in data['data'], f'поле {field} отсутствует'
            print('Все поля присутствуют')
