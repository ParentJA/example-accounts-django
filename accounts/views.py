# Third-party imports...
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
)

# Django imports...
from django.contrib.auth import authenticate, get_user_model, login, logout

# Local imports...
from .serializers import UserSerializer

User = get_user_model()


class LogInView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user.
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return Response(status=HTTP_200_OK, data=UserSerializer(user).data)
        else:
            return Response(status=HTTP_401_UNAUTHORIZED)


class LogOutView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(status=HTTP_204_NO_CONTENT)


class SignUpView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        # Create a new user.
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response(status=HTTP_201_CREATED, data=UserSerializer(user).data)

        # Handle creation error (e.g. username already exists, password mismatch).
        return Response(status=HTTP_400_BAD_REQUEST)
