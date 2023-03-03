from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User
# from django.contrib.auth.models import User


class RoomForm(ModelForm):  # FORM REGISTRO DE SALAS
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'members']        


class UserForm(ModelForm):  # FORM PERFIL DE USUARIO
    class Meta:
        model = User 
        fields = ['avatar', 'name', 'username', 'email', 'bio']
        
    
class CustomUserCreationForm(UserCreationForm):  # FORM REGISTRO USUARIOS
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']