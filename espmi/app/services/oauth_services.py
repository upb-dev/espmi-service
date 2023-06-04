import requests as requests
from django.conf import settings
from requests.auth import HTTPBasicAuth


class MyProjectError(Exception):
    """Exception class from which every exception in this library will derive.
         It enables other projects using this library to catch all errors coming
         from the library with a single "except" statement
    """
    pass


class OauthService:
    def login_oauth(self, username, password):
        url = settings.OAUTH2_BASE_URL + '/oauth/token/'

        body = {
            'grant_type': 'password',
            'username': username.replace('+', ''),
            'password': password
        }

        response = requests.post(url, data=body, auth=HTTPBasicAuth(settings.OAUTH2_USERNAME, settings.OAUTH2_PASSWORD))

        if response:
            return response.json()
        else:
            return None

    def create_user_oauth(self, body):
        url_create_user = settings.OAUTH2_BASE_URL + '/api/users/'

        headers = {
            'Authorization': 'Bearer ' + settings.OAUTH2_TOKEN,
            'Content-Type': 'Application/Json'
        }

        response = requests.post(url_create_user, json=body, headers=headers)

        return response

    def update_user_oauth(self, body, id):
        url_update_user = settings.OAUTH2_BASE_URL + '/api/users/' + id + '/'

        headers = {
            'Authorization': 'Bearer ' + settings.OAUTH2_TOKEN,
            'Content-Type': 'Application/Json'
        }

        response = requests.put(url_update_user, json=body, headers=headers)

        return response

    def get_user_by_email_and_mobile_no(self, email=' ', phone=None):
        url = settings.OAUTH2_BASE_URL + '/api/users/byemailormobile' + '/' + email
        url = url if phone is None else url + '/' + phone

        headers = {
            'Authorization': 'Bearer ' + settings.OAUTH2_TOKEN
        }

        response = requests.get(url, headers=headers)
        return response.json()['data'] if response.json()['data'] != None else {'detail': ''}

    def get_token_oauth(self):
        url = settings.OAUTH2_BASE_URL + '/oauth/token/'

        body = {
            'grant_type': 'client_credentials'
        }

        response = requests.post(url, data=body, auth=HTTPBasicAuth(settings.OAUTH2_USERNAME, settings.OAUTH2_PASSWORD))

        if response:
            return response.json()
        else:
            return None

    def refresh_token(self, token):
        url = settings.OAUTH2_BASE_URL + '/oauth/token/'

        body = {
            'grant_type': 'refresh_token',
            'refresh_token': token
        }

        response = requests.post(url, data=body, auth=HTTPBasicAuth(settings.OAUTH2_USERNAME, settings.OAUTH2_PASSWORD))
        if response:
            return response.json()
        else:
            return None

    def check_token(self, token):
        url = settings.OAUTH2_BASE_URL + '/oauth/check_token/'

        body = {
            'token': token
        }

        response = requests.post(url, data=body, headers={
                                 'Authorization': f"Bearer {settings.OAUTH2_TOKEN}"})
        if response:
            return response.json()
        else:
            return None

    def change_password(self, data, token_user):
        url_change_password = settings.OAUTH2_BASE_URL + '/api/owner/changepassword/'

        header = {
            'Authorization': f'Bearer {token_user}'
        }

        body = data

        response = requests.put(url_change_password, data=body, headers=header)
        return response

    def request_send_otp_to_user(self, oauth_id, media_type):
        url = settings.OAUTH2_BASE_URL + '/api/users/resetpassword/send_otp/'

        headers = {
            'Authorization': 'Bearer ' + settings.OAUTH2_TOKEN
        }

        body = {
            "id": oauth_id,
            "media_type": media_type.upper()
        }

        response = requests.post(url, headers=headers, data=body)
        return response

    def verify_otp_code(self, oauth_id, otp_code):
        url = settings.OAUTH2_BASE_URL + '/api/users/resetpassword/verify_otp/'

        headers = {
            'Authorization': 'Bearer ' + settings.OAUTH2_TOKEN
        }

        body = {
            "id": oauth_id,
            "otp": otp_code
        }

        response = requests.post(url, headers=headers, data=body)
        return response

    def reset_password_user(self, oauth_id, new_password, otp_code):
        url = settings.OAUTH2_BASE_URL + '/api/users/resetpassword/set_password/'

        headers = {
            'Authorization': 'Bearer ' + settings.OAUTH2_TOKEN
        }

        body = {
            "id": oauth_id,
            "otp": otp_code,
            "password": new_password
        }

        response = requests.post(url, headers=headers, data=body)
        return response

    def get_user_by_id(self, oauth_id):
        url = settings.OAUTH2_BASE_URL + '/api/users/' + oauth_id

        headers = {
            'Authorization': 'Bearer ' + settings.OAUTH2_TOKEN
        }

        response = requests.get(url, headers=headers)
        return response.json()['data'] if response.json()['data'] != None else {'detail': ''}

    def revoke_access_token(self, token):
        url = settings.OAUTH2_BASE_URL + '/oauth/revoke_token/'

        body = {
            "token": token,
            "client_id": settings.OAUTH2_USERNAME,
            "client_secret": settings.OAUTH2_PASSWORD
        }

        requests.post(url, data=body)
        return True

    def revoke_refresh_token(self, refresh_token):
        url = settings.OAUTH2_BASE_URL + '/oauth/revoke_token/'

        body = {
            'token': refresh_token,
            'client_id': settings.OAUTH2_USERNAME,
            'client_secret': settings.OAUTH2_PASSWORD,
            'token_type_hint': 'refresh_token'
        }

        requests.post(url, data=body)
        return True

    def client_auth_login(self, username, password):
        url = settings.OAUTH2_BASE_URL + '/oauth/token/'

        response = requests.post(url, data={'grant_type': 'client_credentials'},
                                 auth=HTTPBasicAuth(username, password))

        if 200 <= response.status_code <= 299:
            return response.json()
        else:
            raise MyProjectError(response.json()['error'])
