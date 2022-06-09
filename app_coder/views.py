from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso , Alumno , Profesor
from django.template import loader
from app_coder.forms import Alumnos_formulario, Curso_formulario, Profesores_formulario
# Create your views here.


def inicio(request):

    return render( request , "index.html" )

def alumnos(request):

    return render( request , "alumnos.html" )


def profesores(request):

    return render( request , "profesores.html" )

def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos" : cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )
 

# alta cursos

def alta_curso(request, nombre):
    curso = Curso(nombre=nombre , camada=287318)
    curso.save()
    texto = f"Se guardo en la BD el Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(texto)


def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            curso = Curso( nombre=datos['nombre'] , camada=datos['camada'])
            curso.save()

            return render( request , "alta_curso.html")

    return render( request, "alta_curso.html")

#BUSQUEDA DE CURSO

def buscar_curso(request):

    return render( request , "buscar_curso.html")


def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")

#alta profesores

def alta_profesores(request):

    if request.method == "POST":

        formulario_profe = Profesores_formulario( request.POST )

        if formulario_profe.is_valid():
            datos = formulario_profe.cleaned_data          
            
            profesor = Profesor( nombre=datos['nombre'] , legajo=datos['legajo'])
            profesor.save()
            # return HttpResponse("se creo el profesor")
            return render( request , "alta_profesores.html")

    return render( request, "alta_profesores.html")

# alta alumnos
def alta_alumnos(request):

    if request.method == "POST":

        formulario_alumno = Alumnos_formulario( request.POST )

        if formulario_alumno.is_valid():
            datos = formulario_alumno.cleaned_data          
            alumno = Alumno( nombre=datos['nombre'] , camada=datos['camada'], nacimiento=datos['nacimiento'])
            alumno.save()

            return render( request , "alta_alumnos.html")

    return render( request, "alta_alumnos.html")



   
def registro(request):
    
     return render( request , "registro.html")

def inicio_sesion(request):
    
     return render( request , "inicio_sesion.html")