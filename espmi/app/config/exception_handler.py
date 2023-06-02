from rest_framework.views import exception_handler


def get_response_errors(r):
    errors = []
    for field, value in r.items():
        valstr = ""
        for val in value:
            if type(val) is dict:
                for f, v in val.items():
                    valstr = valstr + " ".join(v)
            else:
                valstr = valstr + val + " "
        errors.append("{} : {}".format(field, valstr.strip()))
    return errors


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    request = context['request']
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR'].split(",")[0].strip()
        request.META['REMOTE_ADDR'] = ip
    # error_log = ErrorLog(
    #     oauth_id= request.oauth_id if hasattr(request, 'oauth_id') else None,
    #     user_agent= request.META.get('HTTP_USER_AGENT', '')[:50],
    #     uri= request.build_absolute_uri(),
    #     ip= request.META.get('REMOTE_ADDR', ''),
    #     method= request.method,
    #     payload= request.data,
    #     req_date= timezone.now(),
    #     error_message= json.dumps(response.data, sort_keys=True) if hasattr(response, 'data') else {},
    #     headers= request.headers,
    #     # error_code= response.error_code
    # )
    # error_log.save()

    # Now add the HTTP status code to the response.
    if response is not None:
        errors = []
        if not isinstance(response.data, list):
            message = response.data.get('detail', None)
            if not message:
                error_codes = response.data.pop('error_code', None)
                if error_codes and isinstance(error_codes, list):
                    error_code = error_codes[0]
                else:
                    error_code = "01"
                errors = get_response_errors(response.data)
                response.data = {'success': False, 'error_code': error_code,
                                 'message': 'Validation Error', 'data': None, 'errors': response.data}
            else:
                response.data = {'success': False, 'error_code': "01",
                                 'message': message, 'data': None, 'error': ['detail : %s' % message]}
        else:
            for r in response.data:
                message = r.get('detail', None)
                if not message:
                    errors.extend(get_response_errors(r))
                else:
                    errors.append("{} : {}".format('detail', message.strip()))
            response.data = {'success': False, 'error_code': "01",
                             'message': 'Validation Error', 'data': None, 'errors': errors}

    return response
