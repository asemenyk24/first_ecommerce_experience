from django.contrib.auth.forms import UserCreationForm
from .models import User


class CreateCustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
