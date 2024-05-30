"""Views login."""
from django.conf import settings
from django.shortcuts import redirect, render
from rest_framework_simplejwt.views import TokenObtainPairView

# serializers
from apps.users.serializers import LoginGetTokenObtainPairSerializer


class LoginGetTokenObtainPairView(TokenObtainPairView):
    """Custom TokenObtainPairView of rest_framework_simplejwt."""
    serializer_class = LoginGetTokenObtainPairSerializer


def home(request):
    """Home page."""
    return render(request, "home/index.html")


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
