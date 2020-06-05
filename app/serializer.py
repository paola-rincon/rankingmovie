from rest_framework import serializers
from app.models import Categoria,Pelicula


class PeliculaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pelicula
        fields = ('id', 'titulo', 'anio', 'sinopsis' , 'fecha_creacion', 'enCartelera', 'duracion')

class CategoriaSerializer(serializers.ModelSerializer):
    
    nombreId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Categoria.objects.all(), source='owner')
    peliculas=PeliculaSerializer(read_only=True)
    

    class Meta:
        model = Categoria
        fields = ('id','nombre', 'peliculas')

