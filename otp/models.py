
from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
from django.conf import settings


class Pin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pin = models.IntegerField()
    expire_date = models.DateTimeField(default=timezone.now()+timedelta(seconds=settings.OTP_EXPIRY))
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pin)

    def is_pin_expired(self):
        if (self.expire_date - self.created).total_seconds() > settings.OTP_EXPIRY:
            return True
        else:
            return False