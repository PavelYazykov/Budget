import json


class Variables:
    transaction_type = "Income"
    category_id = 30
    subcategory_id = None
    amount = 10
    date_reminder = '2026-12-12'


class Payloads:

    get_payloads = {
        "meta": {},
        "data":
            {
                "transaction_type": "Income",
                "category_id": 1,
                "subcategory_id": 1,
                "amount": 100.55,
                "date_reminder": "2025-03-13",
                "id": 1
            }
    }

    post_payloads = {
        "meta": {},
        "data":
            {
                "transaction_type": "Income",
                "category_id": 1,
                "subcategory_id": 1,
                "amount": 100.55,
                "date_reminder": "2025-03-13",
                "id": 1
            }
    }

    @staticmethod
    def check_req_fields(result, required_fields):
        result_text = result.text
        data = json.loads(result_text)

        for field in required_fields:
            assert field in data, f'отсутствует обязательное поле {field}'
        for field in required_fields['data']:
            assert field in data['data'][0], f'отсутствует обязательное поле {field}'
        print('Все поля присутствуют')

    @staticmethod
    def check_req_fields_post(result, required_fields):
        result_text = result.text
        data = json.loads(result_text)

        for field in required_fields:
            assert field in data, f'отсутствует обязательное поле {field}'
        for field in required_fields['data']:
            assert field in data['data'], f'отсутствует обязательное поле {field}'
        print('Все поля присутствуют')
