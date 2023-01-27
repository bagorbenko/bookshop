from django.shortcuts import redirect
from rest_framework import views, status, mixins, viewsets

from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import UserSerializerBS, RegistrationSerializer
from rest_framework.response import Response


class UserAPIView(mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerBS
    permission_classes = (IsUserOrReadOnly,)


class RegistrationAPIView(views.APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)


class LoginSuccessView(views.APIView):
    def post(self, request, *args, **kwargs):
        return redirect('/api')
