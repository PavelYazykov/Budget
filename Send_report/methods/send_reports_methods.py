from common_methods.http_methods import HttpMethods
from common_methods.variables import CommonVariables


class SendReportsMethods:

    @staticmethod
    def get_send_report_with_params(payload, access_token):
        endpoint = '/api/v1/send_report/'
        payload = payload
        get_url = CommonVariables.base_url + endpoint + payload
        result = HttpMethods.get(get_url, access_token)
        return result
