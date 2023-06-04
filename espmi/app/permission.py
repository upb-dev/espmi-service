from espmi.app.helper.phone_formater import change_phone_format
from espmi.app.models import User, UserBackOffice, UserPortal
from espmi.app.services.oauth_services import OauthService
from django.conf import settings
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from rest_framework.permissions import BasePermission


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = authentication.get_authorization_header(request).decode().replace('Bearer ', '')
        oauth_response = OauthService().check_token(token)
        if oauth_response is None or 'authorities' not in oauth_response:
            raise NotAuthenticated()

        try:
            is_worker = 'back_office' in request.query_params

            try:
                user = User.objects.get(oauth_id=oauth_response['user_id'],
                                        userportal__isnull=is_worker, userbackoffice__isnull=not is_worker)
            except User.DoesNotExist:
                if is_worker:
                    user = User.objects.get(userbackoffice__email=oauth_response['email'])
                else:
                    user = User.objects.get(userportal__email=oauth_response['email'])

                user.save_oauth_id(oauth_response['user_id'])

            if not user.is_active:
                raise User.DoesNotExist()

            user.update_last_login()
        except (User.DoesNotExist):
            raise AuthenticationFailed('User Not Found')

        user.role = list([e for e in oauth_response['authorities']])

        return (user, token)


class WorkerAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = authentication.get_authorization_header(request).decode().replace('Bearer ', '')
        oauth_response = OauthService().check_token(token)
        if oauth_response is None or 'authorities' not in oauth_response:
            raise NotAuthenticated()

        oauth_response['user_mobile_no'] = change_phone_format(oauth_response['user_mobile_no'])

        try:
            try:
                user = User.objects.get(oauth_id=oauth_response['user_id'], worker__isnull=False)
            except User.DoesNotExist:
                if oauth_response['user_mobile_no'] is not None:
                    user = User.objects.get(worker__phone=oauth_response['user_mobile_no'])
                else:
                    user = User.objects.get(worker__email=oauth_response['user_email'])

                user.save_oauth_id(oauth_response['user_id'])

            if not user.is_active:
                raise User.DoesNotExist()

            user.update_last_login()
        except (User.DoesNotExist):
            raise AuthenticationFailed('Worker Not Found')

        user.role = list([e for e in oauth_response['authorities'] if e.startswith('C1')])

        return (user, token)


class CustomerAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = authentication.get_authorization_header(request).decode().replace('Bearer ', '')
        oauth_response = OauthService().check_token(token)
        if oauth_response is None or 'authorities' not in oauth_response:
            raise NotAuthenticated()

        oauth_response['user_mobile_no'] = change_phone_format(oauth_response['user_mobile_no'])

        try:
            try:
                user = User.objects.get(oauth_id=oauth_response['user_id'], customer__isnull=False)
            except User.DoesNotExist:
                user = User.objects.get(customer__phone=oauth_response['user_mobile_no'])

                user.save_oauth_id(oauth_response['user_id'])

            if not user.is_active:
                raise AuthenticationFailed('Account is inactive')

            user.update_last_login()
        except User.DoesNotExist:
            raise AuthenticationFailed('Customer Not Found')

        user.role = list([e for e in oauth_response['authorities'] if e.startswith('C1')])

        return (user, token)


class ClientAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = authentication.get_authorization_header(request).decode().replace('Bearer ', '')
        oauth_response = OauthService().check_token(token)
        if oauth_response is None or 'authorities' not in oauth_response:
            raise AuthenticationFailed()

        user = type('Client', (), {})()

        for key, value in oauth_response.items():
            setattr(user, key, value)

        return (user, token)


class Oauth2AuthenticatedAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = authentication.get_authorization_header(request).decode().replace('Bearer ', '')
        oauth_response = OauthService().check_token(token)
        if oauth_response is None or 'authorities' not in oauth_response:
            raise AuthenticationFailed()

        user = type('Oauth2User', (), {})()

        for key, value in oauth_response.items():
            setattr(user, key, value)

        return (user, token)


class IsSuperAdminPermission(BasePermission):
    def has_permission(self, request, view):
        try:
            request.user.customer
            return False
        except UserPortal.DoesNotExist:
            return request.user.worker.is_super_admin


class IsMySelfPermission(BasePermission):
    def has_permission(self, request, view):
        return request._auth == settings.OAUTH2_TOKEN


class IsGreaterThanEqualAdminPermission(BasePermission):
    def has_permission(self, request, view):
        try:
            request.user.customer
            return False
        except UserPortal.DoesNotExist:
            return request.user.worker.is_super_admin or request.user.worker.is_admin


class C1NotifyPermission(BasePermission):
    def has_permission(self, request, view):
        return 'C1_NOTIFY' in request.user.authorities


class S1FltNotifPermission(BasePermission):
    def has_permission(self, request, view):
        if 'S1_FLT_NOTIF' not in request.user.authorities:
            raise AuthenticationFailed({'detail': 'Sorry you\'re not authenticated'})
        return True


class CreateC1DataPermission(BasePermission):
    def has_permission(self, request, view):
        return 'S1_REGISTER_USER' in request.user.authorities
