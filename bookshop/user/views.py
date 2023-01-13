from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import AccountSerializer, CreateAccountSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateAccountSerializer
        self.permission_classes = (AllowAny,)
        return super(UserViewSet, self).create(request, *args, **kwargs)
