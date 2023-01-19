from rest_framework import views, status, mixins, viewsets
from .models import User
from .serializers import AccountSerializer, RegistrationSerializer
from rest_framework.response import Response


class UserAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer


class RegistrationAPIView(views.APIView):
    """Handle user registration"""
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
