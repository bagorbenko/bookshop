from rest_framework.permissions import AllowAny, IsAdminUser


class CustomPermissionMixin:
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAdminUser],
                                    'retrieve': [AllowAny],
                                    'update': [IsAdminUser],
                                    'partial_update': [IsAdminUser],
                                    'destroy': [IsAdminUser]}

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]