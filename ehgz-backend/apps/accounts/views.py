from django.contrib.auth import get_user_model
from dj_rest_auth.views import LoginView
import jwt
from requests import Response
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken, TokenError


class CustomUserDetailsView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return get_user_model().objects.none()


class CustomLoginView(LoginView):
    def get_response(self):
        response = super().get_response()
        user = self.user

        # Generate refresh token
        refresh = RefreshToken.for_user(user)

        # Add refresh token to the response
        response.data['refresh'] = str(refresh)
        return response


class VerifyTokenView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        token = request.COOKIES.get("ehgz-access-token")
        if not token:
            return Response({"detail": "Token not provided."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            AccessToken(token)
            user_id = AccessToken(token).get('user_id')
            return Response({"detail": "Token is valid.","pk":user_id}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({"detail": "Token is invalid or expired."}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get_user_id(request):
        refresh_token = request.data.get('refresh_token')
        # Decode the refresh token to get the user
        decoded_token = jwt.decode(refresh_token, settings.SIGNING_KEY, algorithms=["HS256"])
        user_id = decoded_token['user_id']
        return user_id
    def post(self, request):
        try:
            # Get the refresh token from the request
            refresh_token = request.data.get('refresh_token')
            
            user_id = self.get_user_id(request)
            # Check if the user ID matches the authenticated user
            if str(user_id) != str(request.user.id):
                return Response({"detail": "Invalid token."}, status=status.HTTP_401_UNAUTHORIZED)

            # Blacklist the refresh token
            RefreshToken(refresh_token).blacklist()

            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
