from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    # Replaced by permission IsAdminUser
    # def has_permission(self, request, view):
    #     user = request.user
    #     if not user.is_staff:
    #         return False
    #     return super().has_permission(request, view)

    # def has_permission(self, request, view):

    #     user = request.user
    #     print(user.get_all_permissions())

    #     if user.is_staff:
    #         if user.has_perm("productos.add_producto"): # <app>.<action>_<model>
    #             return True
    #         if user.has_perm("productos.change_producto"): # <app>.<action>_<model>
    #             return True
    #         if user.has_perm("productos.delete_producto"): # <app>.<action>_<model>
    #             return True
    #         if user.has_perm("productos.view_producto"): # <app>.<action>_<model>
    #             return True
            
    #         return False
        
    #     return False

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)