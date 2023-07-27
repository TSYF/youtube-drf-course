from django.db import models
from rest_framework.authtoken.models import Token as BaseToken
from django.db.models import DateTimeField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Token(BaseToken):
    expires = DateTimeField(_("Expiry"))
    
    def save(self, *args, **kwargs):
        if not self.key:
            self.expires = timezone.now() + timezone.timedelta(1)
        return super().save(*args, **kwargs)