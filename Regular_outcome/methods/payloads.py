import json


class RegularOutcomePayloads:
    post_payloads = {
        "meta": {},
        "data":
            {
                "title": "Title or description",
                "category_id": 1,
                "subcategory_id": 1,
                "period": "day",
                "amount": 100.55,
                "is_paid_off": False,
                "date_of_next_pay": "2025-01-19",
                "id": 1

            }
    }

    pay_regular_outcome = {
        "meta": {},
        "data":
            {
                "amount": 100.55,
                "description": "Title or description",
                "transaction_type": "Income",
                "transaction_date": "2025-02-02",
                "id_wallet_for_transfer": 1,
                "wallet_id": 1,
                "category_id": 1,
                "subcategory_id": 1,
                "regular_outcome_id": 1,
                "id": 1
            }
    }

    @staticmethod
    def check_required_fields(result, required_fields):
        result_text = result.text
        data = json.loads(result_text)
        for field in required_fields:
            assert field in data, f'отсутствует обязательное поле {field}'
        for field in required_fields['data']:
            assert field in data['data'], f'отсутствует обязательное поле {field}'

        print('Все поля присутствуют')
