"""Views login."""
import time
from datetime import datetime

from django.conf import settings
from django.shortcuts import redirect, render
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.drf_api_logger.models import APILogsModel
from apps.drf_api_logger.utils import get_headers, get_client_ip, mask_sensitive_data

# serializers
from apps.users.serializers import LoginGetTokenObtainPairSerializer


class LoginGetTokenObtainPairView(TokenObtainPairView):
    """Custom TokenObtainPairView of rest_framework_simplejwt."""
    serializer_class = LoginGetTokenObtainPairSerializer


def home(request):
    """Home page."""
    start_time = time.time()
    logs = _get_log_into_database(request)
    _logs_insert(logs, start_time)
    return render(request, "home/index.html")


def _get_log_into_database(request) -> dict:
    """Gets request data and client."""
    api = request.build_absolute_uri()
    return {
        "method": request.method,
        "api": mask_sensitive_data(api, mask_api_parameters=True),
        "client_ip_address": get_client_ip(request),
        "headers": str(get_headers(request)),
        "response": "OK",
        "status_code": 200,
        "body": "",
        "added_on": datetime.now()
    }


def _logs_insert(log_insert, start_time):
    """Save log."""
    log_insert["execution_time"] = time.time() - start_time
    APILogsModel.objects.create(**log_insert)


def error_404_view(request, exception):
    # we add the path to the 404.html file
    # here. The name of our HTML file is 404.html
    url = settings.URL_REDIRECT
    return redirect(url)


def error_500_view(request):
    # we add the path to the 500.html file
    # here. The name of our HTML file is 500.html
    url = settings.URL_REDIRECT
    return redirect(url)
