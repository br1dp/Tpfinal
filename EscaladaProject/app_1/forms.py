from django import forms

from django.contrib.auth.forms import UserChangeForm


from django.contrib.auth.models import User

from app_1.models import Avatar


class CursoFormulario(forms.Form):

    nivel = forms.CharField()

    dia = forms.CharField()

    horario = forms.IntegerField()

    profesor = forms.CharField()
    

class AlumnosFormulario(forms.Form):

    nombre = forms.CharField()

    apellido = forms.CharField()

    edad = forms.IntegerField()

    email = forms.EmailField()


class ProfesoresFormulario(forms.Form):

    nombre = forms.CharField()

    apellido = forms.CharField()

    email = forms.EmailField()


class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text = "",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ['first_name','last_name', 'email']
        
        
    def clean_password2(self):
        
        password2 = self.cleaned_data["password2"]
        if (password2 != self.cleaned_data["password1"]):
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ('imagen',)
