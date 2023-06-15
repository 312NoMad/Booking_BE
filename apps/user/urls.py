from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import path

from .views import SignInAPIView, SignUpAPIView, ActivateAPIView, LogOutAPIView

urlpatterns = [
    path("sign-up/", SignUpAPIView.as_view()),
    path("sign-in/", SignInAPIView.as_view()),
    path("sign-in/refresh/", TokenRefreshView.as_view()),
    path("logout/", LogOutAPIView.as_view()),
    path("activate/", ActivateAPIView.as_view()),
]
