import json


class Variables:

    transaction_type = "Income"
    category_id = 30
    subcategory_id = None
    amount = 10
    month = 12
    year = 2026
    date_reminder = "2026-01-12"
    title = "pavel"
    have_to_remind = True
    remind_in_days = 1


class Payloads:

    post_payloads = {
      "meta": {},
      "data": {
          "transaction_type": "Income",
          "category_id": 1,
          "subcategory_id": 1,
          "amount": 100.55,
          "month": 1,
          "year": 2020,
          "id": 1,
          "personal_budgets_auto_use_id": 1
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
        print('Все обязательные поля присутствуют')
