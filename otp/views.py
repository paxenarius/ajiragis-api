from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import OtpPhoneNumberForm
User = get_user_model()


def otp_view(request):
    form = OtpPhoneNumberForm(request.POST)
    context = {}
    if request.method == 'POST':
        errors = []
        phone = request.POST.get('phone', None)
        pin = request.POST.get('pin', None)
        if phone and pin:
            user = User.objects.get(username=phone)
            otp = user.get_pin()
            if int(pin) == otp.pin:
                if otp.is_pin_expired():
                    errors.append('Pin has expired.')
                    context = {'phone': phone, 'errors': errors}
                    return render(request, 'otp/otp.html', context=context)
                else:
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request, user)
                    return redirect(reverse_lazy('dashboard'))
            else:
                errors.append('Wrong PIN provided. Please generate code again')
                context = {'phone': phone, 'errors': errors}
                return render(request, 'otp/otp.html', context=context)

        if phone:
            user, created = User.objects.get_or_create(username=phone)
            if created:
                user.is_staff = True
                user.save()
            user.send_otp()
        context = {'phone': phone, 'show_pin_input': True}
    return render(request, 'otp/otp.html', context=context)
