from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso , Alumno , Profesor
from django.template import loader
from app_coder.forms import Alumnos_formulario, Curso_formulario, Profesores_formulario

def inicio(request):

    return render( request , "index.html" )