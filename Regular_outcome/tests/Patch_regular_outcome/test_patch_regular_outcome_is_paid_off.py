# import allure
# import pytest
# from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
# from common_methods.checking import Checking
#
#
# @pytest.mark.Regular_outcome
# @allure.epic(
#     'Patch/api/v1/regular_outcome/{regular_outcome}/ Редактирование регулярного платежа - проверка поля is_paid_off'
# )
# class TestPatchRegularOutcomeAmount:
#
#     @allure.description('проверка поля is_paid_off - Значение True')
#     def test_01(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Запрос на создание regular_outcome"""
#         result = RegularOutcomeMethods.create_regular_outcome(
#             'title', 20, None, 'day', 100, False,
#             '2030-12-12', access_token,
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 201)
#         data = Checking.get_data(result)
#         regular_outcome_id = data['data']['id']
#         try:
#             """Запрос на изменение платежа"""
#             result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
#                 regular_outcome_id, 'title', 20, 'day', 100,
#                 True, access_token
#             )
#
#             """Проверка статус кода"""
#             Checking.check_statuscode(result_patch, 200)
#
#             """Проверка значения поля is_paid_off"""
#             patch_data = Checking.get_data(result_patch)
#             assert patch_data['data']['is_paid_off'] is True
#         except AssertionError:
#             raise AssertionError
#
#         finally:
#             result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
#             Checking.check_statuscode(result_delete, 204)
#
#     @allure.description('проверка поля is_paid_off - Значение False')
#     def test_02(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Запрос на создание regular_outcome"""
#         result = RegularOutcomeMethods.create_regular_outcome(
#             'title', 20, None, 'day', 100, False,
#             '2030-12-12', access_token,
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 201)
#         data = Checking.get_data(result)
#         regular_outcome_id = data['data']['id']
#         try:
#             """Запрос на изменение платежа"""
#             result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
#                 regular_outcome_id, 'title', 20, 'day', 100,
#                 False, access_token
#             )
#
#             """Проверка статус кода"""
#             Checking.check_statuscode(result_patch, 200)
#
#             """Проверка значения поля is_paid_off"""
#             patch_data = Checking.get_data(result_patch)
#             assert patch_data['data']['is_paid_off'] is False
#         except AssertionError:
#             raise AssertionError
#
#         finally:
#             result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
#             Checking.check_statuscode(result_delete, 204)
#
#     @allure.description('проверка поля is_paid_off - Поле отсутствует')
#     def test_03(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Запрос на создание regular_outcome"""
#         result = RegularOutcomeMethods.create_regular_outcome(
#             'title', 20, None, 'day', 100, False,
#             '2030-12-12', access_token,
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 201)
#         data = Checking.get_data(result)
#         regular_outcome_id = data['data']['id']
#         try:
#             """Запрос на изменение платежа"""
#             result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id_and_is_paid_off(
#                 regular_outcome_id, 'title', 20, 'day', 100,
#                 access_token
#             )
#
#             """Проверка статус кода"""
#             Checking.check_statuscode(result_patch, 200)
#
#             """Проверка значения поля"""
#             patch_data = Checking.get_data(result_patch)
#             assert patch_data['data']['title'] == 'title'
#         except AssertionError:
#             raise AssertionError
#
#         finally:
#             result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
#             Checking.check_statuscode(result_delete, 204)
#
#     @allure.description('проверка поля is_paid_off - Значение Null')
#     def test_04(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Запрос на создание regular_outcome"""
#         result = RegularOutcomeMethods.create_regular_outcome(
#             'title', 20, None, 'day', 100, False,
#             '2030-12-12', access_token,
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 201)
#         data = Checking.get_data(result)
#         regular_outcome_id = data['data']['id']
#         try:
#             """Запрос на изменение платежа"""
#             result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
#                 regular_outcome_id, 'title', 20, 'day', 100,
#                 None, access_token
#             )
#
#             """Проверка статус кода"""
#             Checking.check_statuscode(result_patch, 422)
#
#         except AssertionError:
#             raise AssertionError
#
#         finally:
#             result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
#             Checking.check_statuscode(result_delete, 204)
#
#     @allure.description('проверка поля is_paid_off - Пустое поле')
#     def test_05(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Запрос на создание regular_outcome"""
#         result = RegularOutcomeMethods.create_regular_outcome(
#             'title', 20, None, 'day', 100, False,
#             '2030-12-12', access_token,
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 201)
#         data = Checking.get_data(result)
#         regular_outcome_id = data['data']['id']
#         try:
#             """Запрос на изменение платежа"""
#             result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
#                 regular_outcome_id, 'title', 20, 'day', 100,
#                 '', access_token
#             )
#
#             """Проверка статус кода"""
#             Checking.check_statuscode(result_patch, 422)
#
#         except AssertionError:
#             raise AssertionError
#
#         finally:
#             result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
#             Checking.check_statuscode(result_delete, 204)
#
#     @allure.description('проверка поля is_paid_off - Неверный тип данных integer')
#     def test_06(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Запрос на создание regular_outcome"""
#         result = RegularOutcomeMethods.create_regular_outcome(
#             'title', 20, None, 'day', 100, False,
#             '2030-12-12', access_token,
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 201)
#         data = Checking.get_data(result)
#         regular_outcome_id = data['data']['id']
#         try:
#             """Запрос на изменение платежа"""
#             result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
#                 regular_outcome_id, 'title', 20, 'day', 100,
#                 1234, access_token
#             )
#
#             """Проверка статус кода"""
#             Checking.check_statuscode(result_patch, 422)
#
#         except AssertionError:
#             raise AssertionError
#
#         finally:
#             result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
#             Checking.check_statuscode(result_delete, 204)
#
#     @allure.description('проверка поля is_paid_off - Неверный тип данных string')
#     def test_07(self, auth_fixture):
#         """Авторизация"""
#         access_token = auth_fixture
#
#         """Запрос на создание regular_outcome"""
#         result = RegularOutcomeMethods.create_regular_outcome(
#             'title', 20, None, 'day', 100, False,
#             '2030-12-12', access_token,
#         )
#
#         """Проверка статус кода"""
#         Checking.check_statuscode(result, 201)
#         data = Checking.get_data(result)
#         regular_outcome_id = data['data']['id']
#         try:
#             """Запрос на изменение платежа"""
#             result_patch = RegularOutcomeMethods.change_regular_outcome_wt_subcategory_id(
#                 regular_outcome_id, 'title', 20, 'day', 100,
#                 'string', access_token
#             )
#
#             """Проверка статус кода"""
#             Checking.check_statuscode(result_patch, 422)
#
#         except AssertionError:
#             raise AssertionError
#
#         finally:
#             result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
#             Checking.check_statuscode(result_delete, 204)