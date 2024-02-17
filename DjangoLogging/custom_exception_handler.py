import logging
import sys

from django.http import HttpResponseServerError, JsonResponse
from django.utils.deprecation import MiddlewareMixin
from django.views.debug import technical_500_response

from . import settings

logger = logging.getLogger(__name__)


def custom_exception_handler(request, exception, status=500):
    response_data = {
        'message': "some thing went wrong.",
        'isSuccess': False,
        'statusCode': 500,
    }
    return JsonResponse(response_data, status=status)


class ExceptionLoggingMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        error_info = {
            "error": str(exception),
            "request_path": request.path,
            "request_method": request.method,
            "request_body": self.get_request_body(request),
            "user": self.get_user(request),
            "query_params": request.GET.dict(),
            "headers": self.get_headers(request),
        }
        logger.error(f"Standard Django error: {error_info}", exc_info=True)


        if settings.DEBUG:
            return technical_500_response(request, *sys.exc_info())
        else:
            return HttpResponseServerError("""<!doctype html>
                                                <html lang="en">
                                                <head>
                                                <title>Server Error (500)</title>
                                                </head>
                                                <body>
                                                <h1>Server Error (500)(here you can write any thing or render an html file)</h1><p></p>
                                                </body>
                                                </html>""", content_type="text/html")

    @staticmethod
    def get_headers(request):
        # Filtering out sensitive headers
        sensitive_headers = ['Authorization', 'Cookie']
        return {k: v for k, v in request.headers.items() if k not in sensitive_headers}

    @staticmethod
    def get_request_body(request):
        try:
            return request.body.decode('utf-8')
        except Exception as e:
            return f"Error decoding request body: {e}"

    @staticmethod
    def get_user(request):
        if hasattr(request, 'user') and request.user.is_authenticated:
            return f"User ID: {request.user.id}, Username: {request.user.username}"
        return "Anonymous User"
