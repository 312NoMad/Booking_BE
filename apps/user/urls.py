from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import path

from .views import SignInAPIView, SignUpAPIView

urlpatterns = [
    path("sign-up/", SignUpAPIView.as_view()),
    path("sign-in/", SignInAPIView.as_view()),
    path("sign-in/refresh/", TokenRefreshView.as_view()),
]
