from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import SignUpByPhoneSerializer, SignInSerializer


class SignUpAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpByPhoneSerializer
    permission_classes = [AllowAny]


class SignInAPIView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = SignInSerializer


class ActivateAPIView(APIView):
    def get(self, request, code):
        try:
            user = User.objects.get(activation_code=code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response('Вы успешно активировали аккаунт')
        except User.DoesNotExist:
            raise NotFound


class LogOutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = request.data.get('refresh_token')
        if token is not None:
            token_obj = RefreshToken(token)
            token_obj.blacklist()
            return Response('Вы успешно разлогинились')
        else:
            return Response('Refresh токен обязателен', status=400)
