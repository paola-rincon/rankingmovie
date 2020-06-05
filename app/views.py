from django.shortcuts import render
# from django.contrib.postgres.fields import ArrayField<
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import Calificacion,Categoria,Pelicula,Comentario
from django.contrib.auth.models import User
from django.db.models import Avg, Count	
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

def index(request):
    return HttpResponse("Hola, mundo")

# View anonimo

def inicio1(request):

    cartelera=Pelicula.objects.filter(enCartelera=1)
    lista_categorias = Categoria.objects.all()
    contexto ={
        'lista_categorias' : lista_categorias,
        'cartelera' : cartelera
    }
    return render(request, 'app/inicio1.html', contexto)

def categorias1(request):
    lista_categorias = Categoria.objects.all()
    contexto = {
        'lista_categorias' : lista_categorias
    }
    return render(request,'app/categorias1.html', contexto)

def categoria1(request,id):
    obj_categoria = Categoria.objects.get(pk=id)
    contexto = {
        'categoria1' : obj_categoria,
    }
    return render(request,'app/categoria1.html', contexto)

def verpelis1(request):
   lista_peli = Pelicula.objects.all()
   contexto = {
        'lista_peli' : lista_peli
    }
   return render(request, 'app/verpelis1.html', contexto)

def verpeli1(request,id):

    peli =Pelicula.objects.get(pk=id)
    promedio= Calificacion.objects.values('pelicula').annotate(average_rating=Avg('valor'))
    # comentario= Comentario.objects.values('pelicula')
    contexto = {
      'peli':peli,
      'promedio' : promedio}
    #   'comentario': comentario}
    return render(request, "app/verpeli1.html", contexto)




def ultipeli1(request):
    ulti =Pelicula.objects.order_by('-fecha_creacion')[:6]
    contexto = {

        'ulti' : ulti

    }
    return render(request, 'app/ultipeli1.html',contexto)

def cartelera1(request):

    encartelera=Pelicula.objects.filter(enCartelera=1)
    contexto = {
        'encartelera' : encartelera
    }
    return render(request, 'app/cartelera1.html',contexto)



def buscarpeli1(request):
# parametro = request.POST['parametro']
# busca=Pelicula.objects.filter(titulo_contain=parametro)
# lista_categorias=Categoria.objects.all()

# contexto={
#     'busca':busca,
#     'lista_categorias': lista_categorias
# }
    return render(request, 'app/buscarpeli1.html')




def ranking1(request):
    lista_peliculas = Pelicula.objects.all()
    promedio=Calificacion.objects.values('pelicula__titulo').annotate(average_rating=Avg('valor')).order_by('-average_rating')

    contexto ={
        'lista_peliculas' : lista_peliculas,
        'promedio' : promedio
    }
    return render(request, 'app/ranking1.html',contexto)


# View ususario

def inicio2(request):
    cartelera=Pelicula.objects.filter(enCartelera=1)
    lista_categorias = Categoria.objects.all()
    contexto ={
        'lista_categorias' : lista_categorias,
        'cartelera' : cartelera
    }
    return render(request, 'app/inicio2.html', contexto)


def categorias2(request):
    lista_categorias = Categoria.objects.all()
    contexto = {
        'lista_categorias' : lista_categorias
    }
    return render(request,'app/categorias2.html', contexto)

def categoria2(request,id):
    obj_categoria = Categoria.objects.get(pk=id)
    contexto = {
        'categoria2' : obj_categoria
    }
    return render(request,'app/categoria2.html', contexto)


def ultipeli2(request):

    ulti =Pelicula.objects.order_by('-fecha_creacion')[:6]
    contexto = {
        'ulti' : ulti

    }
    return render(request, 'app/ultipeli2.html',contexto)

def cartelera2(request):
    encartelera=Pelicula.objects.filter(enCartelera=1)
    contexto = {
        'encartelera' : encartelera
    }
    return render(request, 'app/cartelera2.html',contexto)

def buscarpeli2(request):
# parametro = request.POST['parametro']
# busca=Pelicula.objects.filter(titulo_contain=parametro)
# lista_categorias=Categoria.objects.all()

# contexto={
#     'busca':busca,
#     'lista_categorias': lista_categorias
# }
    return render(request, 'app/buscarpeli2.html')


def verpelis2(request):
   lista_peli = Pelicula.objects.all()
   contexto = {
        'lista_peli' : lista_peli
    }
   return render(request,'app/verpelis2.html', contexto)

def verpeli2(request,id):
    peli =Pelicula.objects.get(pk=id)
    promedio= Calificacion.objects.values('pelicula').annotate(average_rating=Avg('valor'))
    # comentario= Comentario.objects.values('pelicula')
    contexto = {
      'peli':peli,
      'promedio' : promedio
    #   'comentario': comentario
    }
    return render(request, 'app/verpeli2.html', contexto)



def ranking2(request):
    lista_peliculas = Pelicula.objects.all()
    promedio=Calificacion.objects.values('pelicula__titulo').annotate(average_rating=Avg('valor')).order_by('-average_rating')

    contexto ={
        'lista_peliculas' : lista_peliculas,
        'promedio' : promedio
    }
    return render(request, 'app/ranking2.html',contexto)



def inicio3(request):
    cartelera=Pelicula.objects.filter(enCartelera=1)
    lista_categorias = Categoria.objects.all()
    contexto ={
        'lista_categorias' : lista_categorias,
        'cartelera' : cartelera
    }
    return render(request, 'app/inicio3.html', contexto)


def verpeli3(request,id):
    peli =Pelicula.objects.get(pk=id)
    promedio= Calificacion.objects.values('pelicula').annotate(average_rating=Avg('valor'))
    # comentario= Comentario.objects.all()
    contexto = {
      'peli':peli,
      'promedio' : promedio
    #   'comentario': comentario
    }
    return render(request, 'app/verpeli3.html', contexto)

def verpelis3(request):
   lista_peli = Pelicula.objects.all()

   contexto = {
        'lista_peli' : lista_peli,
   
    }
   return render(request, 'app/verpelis3.html', contexto)



def crearadmin3(request):
    lista_usuario = User.objects.all()
    contexto ={
        'lista_usuario' : lista_usuario
    }

    
    return render(request, 'app/crearadmin3.html',contexto)

def post_crear_admin3(request):
    username=request.POST['username']
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    correo=request.POST['correo']
    contraseña=request.POST['contraseña']
    # admin=request.POST[1]

    usuario=User()
    usuario.username=username
    usuario.first_name=nombre
    usuario.last_name=apellido
    usuario.email=correo
    usuario.set_password(contraseña)
    usuario.is_superuser='1'
  
    usuario.save()



    # return HttpResponse(f'{username} {nombre} {apellido} {correo} {contraseña} ')
    return redirect('app:crearadmin3')
    # return HttpResponse('llegamos!!')

# def post_crear_admin(request):
#     nombre=request.POST['nombre']
#     apellido=request.POST['apellido']
#     correo=request.POST['correo']
#     contraseña=request.POST['contraseña']

#     # usuario=User()
#     # usuario.first_name=nombre
#     # usuario.last_name=apellido
#     # usuario.email=correo
#     # usuario.set_password(contraseña)
  
#     # usuario.save()


#     return HttpResponse(f'{nombre} {apellido} {correo} {contraseña} ')
#     # return redirect('app/login.html') 

def listapeli3(request):
    lista_peliculas = Pelicula.objects.all()
    contexto ={
                'lista_peliculas' : lista_peliculas
    }
    return render(request, 'app/listapeli3.html', contexto)

def crearpelicula3(request):
    lista_categorias = Categoria.objects.all()
    lista_peliculas = Pelicula.objects.all()
    contexto ={
                'lista_categorias' : lista_categorias,
                'lista_peliculas' : lista_peliculas
    }
    return render(request, 'app/crearpelicula3.html', contexto)

def post_crear_pelicula(request):

#obtiene los datos del formulario
    titulo= request.POST['titulo']
    sinopsis= request.POST['sinopsis']
    anio= request.POST['anio']
    actores= request.POST['actores']
    duracion= request.POST['duracion']
    enCartelera='0'
    try:
        enCartelera=request.POST['enCartelera']
        enCartelera='1'
    except:
        pass
    id_categorias=None
    try:   
        id_categorias = request.POST.getlist('categoria')
        # categoria=Categoria.objects.get(pk=id_categorias)
    except:
        pass

# Crea la categoria
    # categoria=Categoria.objects.get(pk=id_categorias)
# #guardar la catgoria en la BD

    # pelicula=Pelicula(titulo=titulo)
    # pelicula=Pelicula()
    # pelicula.titulo=titulo
    # pelicula.sinopsis=sinopsis
    # pelicula.anio=anio
    # pelicula.actores=actores
    # pelicula.duracion=duracion
    # pelicula.enCartelera=enCartelera
    # pelicula.categoria=categoria
    # pelicula.save()
#     categorias=Categoria(categoria_id=id_categorias)
#     categorias.peliculas=
    # return HttpResponse(f'{titulo} {sinopsis} {anio} {actores} {duracion} {enCartelera} {id_categorias} ')
    return redirect('app/crearpelicula3.html')

def listacategoria3(request):
    lista_categorias = Categoria.objects.all()

    contexto ={
                'lista_categorias' : lista_categorias
    }
    return render(request, 'app/listacategoria3.html', contexto)

def crearcategoria3(request):
    lista_categorias = Categoria.objects.all()

    contexto ={
                'lista_categorias' : lista_categorias
    }
    return render(request, 'app/crearcategoria3.html', contexto)


def post_crear_categoria(request):
#obtiene los datos del formulario
    name= request.POST['nombre']
# Crea la categoria
    categoria=Categoria(nombre=name)
#guardar la catgoria en la BD
    categoria.save()

    return redirect('app:crearcategoria3')


def editarpelicula3(request):

    return render(request, 'app/editarpelicula3.html')

def from_login(request):

    return render(request, 'app/from_login.html')

def post_login(request):
    username=request.POST['username']
    contraseña=request.POST['contraseña']

    usuario = authenticate(username=username, password=contraseña)

    if usuario is not None:
        # Inicia la sesión del usuario en el sistema
        login(request, usuario)
        # Redirecciona a una página de éxito
        if usuario.is_superuser :
            return redirect('app:inicio3')
        else:
            return redirect('app:inicio2')
    else:
        # Retorna un mensaje de error de login no válido
        return render(request, 'app/login.html')

    return HttpResponse('llegamos!!')


def registro(request):

    return render(request, 'app/registro.html')

def post_registro(request):
    username=request.POST['username']
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    correo=request.POST['correo']
    contraseña=request.POST['contraseña']

    usuario=User()
    usuario.username=username
    usuario.first_name=nombre
    usuario.last_name=apellido
    usuario.email=correo
    usuario.set_password(contraseña)

  
    usuario.save()

    # return HttpResponse(f'{nombre} {apellido} {correo} {contraseña} ')
    return redirect('app:login')

def salir(request):
	
    logout(request)
    return redirect('/inicio1/')

def olvidecontraseña(request):

    return render(request, 'app/olvidecontraseña.html')

def nuevacontraseña(request):

    return render(request, 'app/nuevacontraseña.html')




