import json


class Payloads:
    get_completed_detail = {
        "meta": {},
        "data": [
            {
                "subcategory": 0,
                "date": "2025-05-04",
                "amount": 100.55
            }
        ]
    }

    get_missed_detail = {
        "meta": {},
        "data": [
            {
                "subcategory": 0,
                "date": "2025-05-04",
                "amount": 100.55
            }
        ]
    }

    get_payments_analytics = {
      "meta": {
          "completed": 0,
          "total": 0
      },
      "data": {
        "fulfilled": [
          {
            "category": 0,
            "amount": 100.55
          }
        ],
        "missed": [
          {
            "category": 0,
            "amount": 100.55
          }
        ]
      }
    }

    @staticmethod
    def check_required_fields(result, required_fields):
        data = json.loads(result.text)
        for field in required_fields['data'][0]:
            assert field in data['data'][0], f'отсутствует поле {field}'
        print('Все поля присутствуют')

    @staticmethod
    def check_data_mete(result):
        data = json.loads(result.text)
        assert 'data' in data, 'отсутствует поле data'
        assert 'meta' in data, 'отсутствует поле meta'
        print('Все поля присутствуют')

    @staticmethod
    def check_get_payments_analytics(result, req_fields):
        data = json.loads(result.text)
        for field in req_fields:
            assert field in data, f'отсутствует поле {field}'
        for field in req_fields['meta']:
            assert field in data['meta'], f'отсутствует поле {field}'
        for field in req_fields['data']:
            assert field in data['data'], f'отсутствует поле {field}'
        print('Все поля присутствуют')



