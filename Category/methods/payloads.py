import json

import allure


class CategoryPayloads:
    payloads = {
        "meta": {},
        "data": [
            {
                "title": "Title or description",
                "transaction_type": "Income",
                "icon": "string",
                "color": "string",
                "id": 1,
                "subcategories": [
                    {
                        "category_id": 1,
                        "title": "Title or description",
                        "id": 1,
                        "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "is_archived": True
                    }
                ]
            }
        ]
    }

    category_list = ['Продукты и хозтовары', 'Недвижимость', 'Покупки', 'Транспорт', 'Автомобиль', 'Дети',
                     'Домашние питомцы', 'Подарки', 'Копилки', 'Красота и здоровье', 'Отдых и развлечения',
                     'Образование', 'Путешествия', 'Платежи и комиссии', 'Пожертвования', 'Налоги', 'Долги',
                     'Внеплановые расходы', 'Кафе и рестораны', 'Другие расходы', 'Зарплата', 'Подработка',
                     'Фриланс', 'Подарок', 'Возврат долгов', 'Инвестиции', 'Продажа личных вещей', 'Рента',
                     'Возврат налогов', 'Другие доходы']

    @staticmethod
    def check_required_fields(result, required_fields):
        with allure.step('Проверка наличия обязательных полей'):
            result_text = result.text
            data = json.loads(result_text)

            for field in required_fields:
                assert field in data, f'обязательное поле {field} отсутствует'

            for field in required_fields['data']:
                for i_field in field:
                    assert i_field in data['data'][0]

    @staticmethod
    def check_excluded_category(result, exc_category):
        with allure.step('Проверка наличия исключенной категории'):
            result_text = result.text
            data = json.loads(result_text)

            for fields in data['data']:
                if exc_category != fields['title']:
                    print(fields['title'])
                else:
                    print(f'Категория: {exc_category} не исключена')
                    raise AssertionError

    @staticmethod
    def check_excluded_category_list(result, exc_category):
        with allure.step('Проверка наличия исключенной категории'):
            result_text = result.text
            data = json.loads(result_text)
            list_category = list(exc_category)
            for fields in data['data']:
                for category in list_category:
                    if category != fields['title']:
                        print('Исключенной категории нет в: ', fields['title'])
                    else:
                        print(f'Категория: {category} не исключена и присутствует в ')
                        raise AssertionError

    @staticmethod
    def check_titles(result, checking_titles):
        # Получаем список всех title из data['data'], вызывая ошибку, если title отсутствует
        data = json.loads(result.text)
        existing_titles = [item['title'] for item in data['data']]
        # Проверяем наличие каждого элемента из titles в существующем списке
        missing_titles = [title for title in checking_titles if title not in existing_titles]
        return missing_titles

