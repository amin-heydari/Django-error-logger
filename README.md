# DjangoErrorLogger

DjangoErrorLogger is a middleware for Django projects aimed at improving error logging and handling. It captures detailed information about exceptions occurring within both Django views and Django REST Framework (DRF) API views, logs this information to a file, and provides customizable error responses to the client.
<br>It saves the error on a log file with the user details if the user is logged in, url, time, what was on the header and the body of the request that the user sent that caused the error and etc.

## Features

- Detailed error logging, including request path, method, body, user details, and request headers.
- Customizable error responses for better client-side error handling.
- Seamless integration with Django REST Framework for API error handling.
- Differentiated error handling in debug and production modes.

## Getting Started

### Installation

1. Clone this repository into your Django project directory.
2. Ensure you have Django and Django REST Framework installed in your environment:

```bash
pip install django djangorestframework
```
3. Add the error app to your INSTALLED_APPS in settings.py:
```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'error',
    ...
]
```
4. Integrate ExceptionLoggingMiddleware in your MIDDLEWARE setting in settings.py:
```
MIDDLEWARE = [
    ...
    'DjangoLogging.custom_exception_handler.ExceptionLoggingMiddleware',
    ...
]
```
5.Configure the LOGGING setting in settings.py to specify the log file location and format.
- right now it is saving the errors on django_error.log with the given format you can change it the way you want.

## Usage
Run your Django project as usual. The middleware will automatically log exceptions to logs/django_error.log and handle error responses.


## Testing
- For Standard Django Views: Trigger an error by accessing /error/.
- For DRF API Views: Trigger an error by sending a POST request to /error/api/.
## Error Log Details
Errors are logged in logs/django_error.log with detailed information for debugging.