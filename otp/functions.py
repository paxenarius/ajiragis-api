import random
import string

import africastalking
from django.conf import settings


def generate_pin(length=6):
    ''' generate an OTP '''
    chars = string.digits
    otp = ''
    for i in range(length):
        otp += chars[int(random.random() * 10)]
    return int(otp)


def send_message(phone_number, otp):
    ''' send a message with the otp'''
    print(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)
    africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)
    sms = africastalking.SMS
    phone_number = '+254' + str(phone_number)[1:]
    message = 'Use this PIN to login to Ajira : {}'.format(str(otp))
    response = sms.send(message, [phone_number])
    try:
        status = response['SMSMessageData']['Recipients'][0]['status']
        if status == 'Success':
            return {
                'phone_number': phone_number,
                'otp': otp
            }
        return False
    except Exception as e:
        print(e)
        return False


def phone_number_validator(phone_number):
    """
    Simple Validator to check if number is a valid phone number
    :param phone_number:
    :return Boolean:
    """
    if len(phone_number) != 10:
        return False
    if phone_number[0] == '0':
        return False
    try:
        int(phone_number)
    except ValueError:
        return False
    return True
