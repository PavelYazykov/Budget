import json

import allure
from datetime import date


class Payloads:
    get_payloads = {
        "meta": {},
        "data": [
            {
                "amount": 100.55,
                "description": "Title or description",
                "transaction_type": "Income",
                "transaction_date": "2024-10-23",
                "id_wallet_for_transfer": 1,
                "wallet_id": 1,
                "category_id": 1,
                "subcategory_id": 1,
                "id": 1
            }
        ]
    }

    post_payloads = {
        "meta": {},
        "data":
            {
                "amount": 100.55,
                "description": "Title or description",
                "transaction_type": "Income",
                "transaction_date": "2024-10-23",
                "id_wallet_for_transfer": 1,
                "wallet_id": 1,
                "category_id": 1,
                "subcategory_id": 1,
                "id": 1
            }
    }

    @staticmethod
    def check_required_fields(result, required_fields):
        with allure.step('Проверка наличия обязательных полей в ответе запроса'):
            result_text = result.text
            data = json.loads(result_text)
            for field in required_fields:
                assert field in data, f'Отсутствует обязательное поле {field}'

            for field in required_fields['data']:
                for i_field in field:
                    assert i_field in data['data'][0]

    @staticmethod
    def check_required_fields_post(result, required_fields):
        with allure.step('Проверка наличия обязательных полей в ответе запроса'):
            result_text = result.text
            data = json.loads(result_text)
            for field in required_fields:
                assert field in data, f'Отсутствует обязательное поле {field}'

            for field in required_fields['data']:
                assert field in data['data']

    @staticmethod
    def check_value(result):
        result_text = result.text
        data = json.loads(result_text)
        print('VALUE:', data['data'][0]['amount'])


