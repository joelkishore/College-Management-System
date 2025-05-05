from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  
        fields = ('username', 'role', 'password1', 'password2')  