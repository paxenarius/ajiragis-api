from django.contrib.auth.models import AbstractUser
from django.db import models
from otp.models import Pin
from otp.functions import generate_pin, send_message


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_pin(self):
        otps = self.pin_set.all()
        if otps:
            return otps.latest('created')
        else:
            return False

    def send_otp(self):
        otp = generate_pin()
        send_message(self.username, otp)
        self.pin_set.create(pin=otp)
        return True