from django import forms

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