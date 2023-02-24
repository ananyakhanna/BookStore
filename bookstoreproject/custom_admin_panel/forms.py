from django.contrib.auth.forms import UserCreationForm
from django import forms
from captcha.fields import CaptchaField
from bookstoreapp.models import *

class UCF(UserCreationForm):
    captcha = CaptchaField()

    class Meta(UserCreationForm.Meta):
        model = User

