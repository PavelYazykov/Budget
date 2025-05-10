import allure
import random
from common_methods.http_methods import HttpMethods
from common_methods.variables import CommonVariables


class SettingsMethods:

    @staticmethod
    def get_settings(access_token):
        with allure.step('Получение настроек пользователя'):
            endpoint = '/api/v1/settings/my/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_settings_without_auth():
        with allure.step('Получение настроек пользователя'):
            endpoint = '/api/v1/settings/my/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get_without_auth(get_url)
            return result

    @staticmethod
    def patch_settings(
            personal_accounting, business_accounting, analytics, use_subcategories, use_quantity, push_notifications,
            email_notifications, default_currency_id, excluded_categories, access_token
    ):
        with allure.step('Изменение настроек пользователя'):
            endpoint = '/api/v1/settings/my/'
            body = {
                "personal_accounting": personal_accounting,
                "business_accounting": business_accounting,
                "analytics": analytics,
                "use_subcategories": use_subcategories,
                "use_quantity": use_quantity,
                "push_notifications": push_notifications,
                "email_notifications": email_notifications,
                "default_currency_id": default_currency_id,
                "excluded_categories": excluded_categories
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def patch_settings_onboarding(has_onboarding, access_token):
        with allure.step('Изменение настроек пользователя has_onboarding'):
            endpoint = '/api/v1/settings/my/'
            body = {
                "has_onboarding": has_onboarding,
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def patch_settings_2(
            personal_accounting, business_accounting, analytics, use_subcategories, use_quantity, push_notifications,
            email_notifications, default_currency_id, excluded_categories, remind_in_days, telegram_notifications,
            registration_consent, telegram_consent, access_token
    ):
        with allure.step(
                'Изменение настроек пользователя с полем telegram_notifications, registration_consent,telegram_consent,'
                'remind_in_days'
        ):
            endpoint = '/api/v1/settings/my/'
            body = {
                "personal_accounting": personal_accounting,
                "business_accounting": business_accounting,
                "analytics": analytics,
                "use_subcategories": use_subcategories,
                "use_quantity": use_quantity,
                "push_notifications": push_notifications,
                "email_notifications": email_notifications,
                "default_currency_id": default_currency_id,
                "excluded_categories": excluded_categories,
                "remind_in_days": remind_in_days,
                "telegram_notifications": telegram_notifications,
                "registration_consent": registration_consent,
                "telegram_consent": telegram_consent
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def patch_settings_without_excluded_categories(
            personal_accounting, business_accounting, analytics, use_subcategories, use_quantity, push_notifications,
            email_notifications, default_currency_id, access_token
    ):
        with allure.step('Изменение настроек пользователя без поля excluded_categories'):
            endpoint = '/api/v1/settings/my/'
            body = {
                "personal_accounting": personal_accounting,
                "business_accounting": business_accounting,
                "analytics": analytics,
                "use_subcategories": use_subcategories,
                "use_quantity": use_quantity,
                "push_notifications": push_notifications,
                "email_notifications": email_notifications,
                "default_currency_id": default_currency_id
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def patch_settings_without_default_currency_id(
            personal_accounting, business_accounting, analytics, use_subcategories, use_quantity, push_notifications,
            email_notifications, excluded_categories, access_token
    ):
        with allure.step('Изменение настроек пользователя без поля default_currency_id'):
            endpoint = '/api/v1/settings/my/'
            body = {
                "personal_accounting": personal_accounting,
                "business_accounting": business_accounting,
                "analytics": analytics,
                "use_subcategories": use_subcategories,
                "use_quantity": use_quantity,
                "push_notifications": push_notifications,
                "email_notifications": email_notifications,
                "excluded_categories": excluded_categories
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def patch_settings_without_email_notifications(
            personal_accounting, business_accounting, analytics, use_subcategories, use_quantity, push_notifications,
            default_currency_id, excluded_categories, access_token
    ):
        with allure.step('Изменение настроек пользователя без поля email_notifications'):
            endpoint = '/api/v1/settings/my/'
            body = {
                "personal_accounting": personal_accounting,
                "business_accounting": business_accounting,
                "analytics": analytics,
                "use_subcategories": use_subcategories,
                "use_quantity": use_quantity,
                "push_notifications": push_notifications,
                "default_currency_id": default_currency_id,
                "excluded_categories": excluded_categories
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def patch_settings_without_push_notifications(
            personal_accounting, business_accounting, analytics, use_subcategories, use_quantity,
            email_notifications, default_currency_id, excluded_categories, access_token
    ):
        with allure.step('Изменение настроек пользователя без поля push_notifications'):
            endpoint = '/api/v1/settings/my/'
            body = {
                "personal_accounting": personal_accounting,
                "business_accounting": business_accounting,
                "analytics": analytics,
                "use_subcategories": use_subcategories,
                "use_quantity": use_quantity,
                "email_notifications": email_notifications,
                "default_currency_id": default_currency_id,
                "excluded_categories": excluded_categories
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def patch_settings_without_use_quantity(
            personal_accounting, business_accounting, analytics, use_subcategories, push_notifications,
            email_notifications, default_currency_id, excluded_categories, access_token
    ):
        with allure.step('Изменение настроек пользователя без поля use_quantity'):
            endpoint = '/api/v1/settings/my/'
            body = {
                "personal_accounting": personal_accounting,
                "business_accounting": business_accounting,
                "analytics": analytics,
                "use_subcategories": use_subcategories,
                "push_notifications": push_notifications,
                "email_notifications": email_notifications,
                "default_currency_id": default_currency_id,
                "excluded_categories": excluded_categories
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def patch_settings_without_use_subcategories(
            personal_accounting, business_accounting, analytics, use_quantity, push_notifications,
            email_notifications, default_currency_id, excluded_categories, access_token
    ):
        with allure.step('Изменение настроек пользователя без поля use_subcategories'):
            endpoint = '/api/v1/settings/my/'
            body = {
                "personal_accounting": personal_accounting,
                "business_accounting": business_accounting,
                "analytics": analytics,
                "use_quantity": use_quantity,
                "push_notifications": push_notifications,
                "email_notifications": email_notifications,
                "default_currency_id": default_currency_id,
                "excluded_categories": excluded_categories
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def patch_settings_without_analytics(
            personal_accounting, business_accounting, use_subcategories, use_quantity, push_notifications,
            email_notifications, default_currency_id, excluded_categories, access_token
    ):
        with allure.step('Изменение настроек пользователя без поля analytics'):
            endpoint = '/api/v1/settings/my/'
            body = {
                "personal_accounting": personal_accounting,
                "business_accounting": business_accounting,
                "use_subcategories": use_subcategories,
                "use_quantity": use_quantity,
                "push_notifications": push_notifications,
                "email_notifications": email_notifications,
                "default_currency_id": default_currency_id,
                "excluded_categories": excluded_categories
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def patch_settings_without_personal_accounting(
            business_accounting, analytics, use_subcategories, use_quantity, push_notifications,
            email_notifications, default_currency_id, excluded_categories, access_token
    ):
        with allure.step('Изменение настроек пользователя без поля personal_accounting'):
            endpoint = '/api/v1/settings/my/'
            body = {
                "business_accounting": business_accounting,
                "analytics": analytics,
                "use_subcategories": use_subcategories,
                "use_quantity": use_quantity,
                "push_notifications": push_notifications,
                "email_notifications": email_notifications,
                "default_currency_id": default_currency_id,
                "excluded_categories": excluded_categories
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def patch_settings_without_business_accounting(
            personal_accounting, analytics, use_subcategories, use_quantity, push_notifications,
            email_notifications, default_currency_id, excluded_categories, access_token
    ):
        with allure.step('Изменение настроек пользователя без поля business_accounting'):
            endpoint = '/api/v1/settings/my/'
            body = {
                "personal_accounting": personal_accounting,
                "analytics": analytics,
                "use_subcategories": use_subcategories,
                "use_quantity": use_quantity,
                "push_notifications": push_notifications,
                "email_notifications": email_notifications,
                "default_currency_id": default_currency_id,
                "excluded_categories": excluded_categories
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def patch_settings_without_body(access_token):
        with allure.step('Изменение настроек пользователя без body'):
            endpoint = '/api/v1/settings/my/'
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch_without_body(patch_url, access_token)
            return result

    @staticmethod
    def post_contact_to_admin(email, message_topic, message, access_token):
        with allure.step('Обращение к админу'):
            endpoint = '/api/v1/settings/contact_to_admin/'
            body = {
                "email": email,
                "message_topic": message_topic,
                "message": message
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def post_contact_to_admin_without_auth(email, message_topic, message):
        with allure.step('Обращение к админу'):
            endpoint = '/api/v1/settings/contact_to_admin/'
            body = {
                "email": email,
                "message_topic": message_topic,
                "message": message
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post_without_auth(post_url, body)
            return result

    @staticmethod
    def post_contact_to_admin_without_auth_message(email, message_topic):
        with allure.step('Обращение к админу без поля message'):
            endpoint = '/api/v1/settings/contact_to_admin/'
            body = {
                "email": email,
                "message_topic": message_topic
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post_without_auth(post_url, body)
            return result

    @staticmethod
    def post_contact_to_admin_without_auth_message_topic(email, message):
        with allure.step('Обращение к админу без поля message_topic'):
            endpoint = '/api/v1/settings/contact_to_admin/'
            body = {
                "email": email,
                "message": message
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post_without_auth(post_url, body)
            return result

    @staticmethod
    def post_contact_to_admin_without_body(access_token):
        with allure.step('Обращение к админу'):
            endpoint = '/api/v1/settings/contact_to_admin/'
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post_without_body(post_url, access_token)
            return result

    @staticmethod
    def post_contact_to_admin_without_email(message_topic, message, access_token):
        with allure.step('Обращение к админу'):
            endpoint = '/api/v1/settings/contact_to_admin/'
            body = {
                "message_topic": message_topic,
                "message": message
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def randstr(chars, n):
        return ''.join(random.choice(chars) for _ in range(n))


