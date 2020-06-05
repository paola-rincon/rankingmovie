from django.urls import path 
from . import views 

app_name = 'app' 



urlpatterns = [
    path('', views.index, name='index'),
    # path('peliculas/', views.movies, name='movies'),
    # path('peliculas/<int:id>', views.movie, name='movie'),
    # path("categorias/", views.categories, name="categories"),
  
# URLS anonimo
    
    path('inicio1/', views.inicio1, name='inicio1'),
    path('categorias1/', views.categorias1, name='categorias1'),
    path('categorias1/<int:id>/', views.categoria1, name='categoria1'),
    path('verpelis1/', views.verpelis1, name='verpelis1'),
    path('verpelis1/<int:id>/', views.verpeli1, name='verpeli1'),


    path('ultipeli1/', views.ultipeli1, name='ultipeli1'),
    path('cartelera1/', views.cartelera1, name='cartelera1'),
    path('buscarpeli1/', views.buscarpeli1, name='buscarpeli1'),
 
    path('ranking1/', views.ranking1, name='ranking1'),
   
# URLS usuario

    path('inicio2/', views.inicio2, name='inicio2'),
    path('categorias2/', views.categorias2, name='categorias2'),
    path('categorias2/<int:id>/', views.categoria2, name='categoria2'),
    path('verpelis2/', views.verpelis2, name='verpelis2'),
    path('verpelis2/<int:id>/', views.verpeli2, name='verpeli2'),
    path('ultipeli2/', views.ultipeli2, name='ultipeli2'),
    path('cartelera2/', views.cartelera2, name='cartelera2'),
    path('buscarpeli2/', views.buscarpeli2, name='buscarpeli2'),
    path('ranking2/', views.ranking2, name='ranking2'),

 # URLS admin

    path('inicio3/', views.inicio3, name='inicio3'),
    path('listacategoria3/', views.listacategoria3, name='listacategoria3'),
    path('listapeli3/', views.listapeli3, name='listapeli3'),
    path('crearadmin3/', views.crearadmin3, name='crearadmin3'),
    path('crearpelicula3/', views.crearpelicula3, name='crearpelicula3'),
    
    path('listacategoria3/', views.listacategoria3, name='listacategoria3'),
    path('listacategoria3/crear/', views.crearcategoria3, name='crearcategoria3'),
    path('listacategoria3/crear_post/', views.post_crear_categoria, name="post_crear_categoria"),
    # path('crearcategoria3/crear_post', views.crearcategoria3, name='crearcategoria3'), 
    path('listapeli3/', views.listapeli3, name='listapeli3'),
    path('listapeli3/crear/', views.crearpelicula3, name='crearpelicula3'),
    path('listapeli3/crear_post/', views.post_crear_pelicula, name="post_crear_pelicula"),
    

    path('editarpelicula3/', views.editarpelicula3, name='editarpelicula3'),
    path('verpelis3/', views.verpelis3, name='verpelis3'),
    path('verpelis3/<int:id>/', views.verpeli3, name='verpeli3'),

# URLS registros
    
    path('login/', views.login, name='login'),
    path('post_login/', views.post_login, name='post_login'),
    path('registro/', views.registro, name='registro'),
    path('post_registro/', views.post_registro, name='post_registro'),
    path('logout/', views.salir, name='salir'),

    path('olvidecontraseña/', views.olvidecontraseña, name='olvidecontraseña'),
    path('nuevacontraseña/', views.nuevacontraseña, name='nuevacontraseña'),
    

]