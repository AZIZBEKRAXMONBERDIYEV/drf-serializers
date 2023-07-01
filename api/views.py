from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request

from .serializers import User, UserSerializer

class UserView(APIView):
    """Test API View"""

    def get(self, request: Request):
        # create a user object
        user = User("John", "Doe", 42)

        # create a serializer object
        serializer = UserSerializer(user)

        # return the serialized data
        return Response(serializer.data)

