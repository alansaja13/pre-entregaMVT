from django import forms


class Curso_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class Alumnos_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()
    nacimiento = forms.DateField()

class Profesores_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    legajo = forms.IntegerField()