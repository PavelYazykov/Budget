import json


class Payloads:

    @staticmethod
    def required_fields():
        required_fields = {
            "data": {
                "to_date": "2024-12-30",
                "goal": "1000.00",
                "wallet": {
                    "name": "My Goal_2",
                    "currency_id": 2,
                    "amount": "0"
                }
            }
        }

    @staticmethod
    def check_required_fields_value(result, date, goal, name, currency_id, amount):
        result_text = result.text
        data = json.loads(result_text)
        required_fields_value = {
            "data": {
                "to_date": date,
                "goal": goal,
                "wallet": {
                    "name": name,
                    "currency_id": currency_id,
                    "amount": amount
                }
            }
        }
        for field, value in required_fields_value.items():
            assert field, value in data
