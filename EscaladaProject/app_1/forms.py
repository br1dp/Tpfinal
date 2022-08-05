from django import forms

class CursoFormulario(forms.Form):

    nivel = forms.CharField()

    horario = forms.IntegerField()

    profesor = forms.CharField()