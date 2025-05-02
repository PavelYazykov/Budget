import json

import allure


class Payloads:

    post_response = {
        "meta": {},
        "data":
            {
                "amount": 100.55,
                "description": "Title or description",
                "transaction_type": "Income",
                "transaction_date": "2025-04-12",
                "id_wallet_for_transfer": 1,
                "wallet_id": 1,
                "category_id": 1,
                "subcategory_id": 1,
                "regular_outcome_id": 1,
                "id": 1
            }
    }

    get_payloads_by_id = {
      "meta": {},
      "data":
        {
          "id": 1,
          "regular_outcome_id": 1,
          "amount": 100.55,
          "debt_date": "2025-04-16",
          "paid_off_date": "2025-04-16",
          "is_paid_on_time": True
        }
    }

    get_payloads = {
      "meta": {},
      "data": [
        {
          "id": 1,
          "regular_outcome_id": 1,
          "amount": 100.55,
          "debt_date": "2025-04-16",
          "paid_off_date": "2025-04-16",
          "is_paid_on_time": True
        }
      ]
    }

    @staticmethod
    def check_required_fields(result, required_fields):
        with allure.step('Проверка наличия полей в ответе запроса'):
            data = json.loads(result.text)
            for field in required_fields:
                assert field in data, f'Отсутствует обязательное поле {field}'
            for field in required_fields['data']:
                assert field in data['data'], f'Отсутствует обязательное поле {field}'
            print('Все обязательные поля присутствуют')

    @staticmethod
    def check_required_fields_for_get_request(result, required_fields):
        with allure.step('Проверка наличия полей в ответе запроса'):
            data = json.loads(result.text)
            for field in required_fields:
                assert field in data, f'Отсутствует обязательное поле {field}'
            for field in required_fields['data'][0]:
                assert field in data['data'][0], f'Отсутствует обязательное поле {field}'
            print('Все обязательные поля присутствуют')

