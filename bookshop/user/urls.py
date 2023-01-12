from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import AccountViewSet


router = DefaultRouter()
router.register(r'users', AccountViewSet, basename="users")


urlpatterns = [
    path('api/', include(router.urls)),
]

urlpatterns += router.urls