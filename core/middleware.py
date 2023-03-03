import datetime

# CUSTOM MIDDLEWARE

class Session:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)

        user_agent = request.META.get('HTTP_USER_AGENT')
        host = request.META.get('HTTP_HOST')
        request.current_time = datetime.datetime.now()
        active_user = request.user

        print('Custom middleware called...')
        print('-----------------------------------')
        print(f'Usuario activo: {active_user}')
        print(f'Host: {host}')
        print(f'User agent: {user_agent}')
        print(f'Request realizada a las: {request.current_time}')

        return response