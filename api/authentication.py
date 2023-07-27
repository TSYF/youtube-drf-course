from rest_framework.authentication import (
    TokenAuthentication as BaseTokenAuth
)
from django.utils.translation import gettext_lazy as _
from rest_framework import HTTP_HEADER_ENCODING, exceptions

class TokenAuthentication(BaseTokenAuth):
    keyword = "Bearer"
    
    """ def get_model(self):
        # if self.model is not None:
        #     return self.model
        from .models import Token
        return Token
    
    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (token.user, token) """