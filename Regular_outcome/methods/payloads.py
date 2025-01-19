import json


class RegularOutcomePayloads:
    post_payloads = {
        "meta": {},
        "data":
            {
                "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "title": "Title or description",
                "category_id": 1,
                "subcategory_id": 1,
                "period": "День",
                "amount": 100.55,
                "is_paid_off": False,
                "id": 1,
                "date_of_next_pay": "2025-01-19"
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
