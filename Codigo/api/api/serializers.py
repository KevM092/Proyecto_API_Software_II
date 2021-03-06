from rest_framework import serializers
from api.models import Cliente,Evento, Categoria,Telefonos, Lugar,Miseventos


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ('id_cliente','nombre', 'usuario', 'email', 'contrase_a','sexo','administrador')

class postClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nombre', 'usuario', 'email', 'contrase_a','sexo','administrador')
	   
	   
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('id_evento' ,'nombre','fecha','hora','descripcion','email','calificacion','precio', 'estado' , 'imagen' , 'lugar_id_lugar', 
    'categoria_id_categoria', 
    'cliente_id_cliente')

	   
class postEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('nombre','fecha','hora','descripcion','email','calificacion','precio', 'estado' , 'imagen' , 'lugar_id_lugar', 
    'categoria_id_categoria', 
    'cliente_id_cliente')
      
    
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id_categoria','nombre')

class postCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre']
	   
	       
class TelefonosSerializer(serializers.ModelSerializer):
    class Meta:
     model = Telefonos
     fields =('id_telefonos','telefono','evento_id_evento')

class postTelefonosSerializer(serializers.ModelSerializer):
    class Meta:
     model = Telefonos
     fields =('telefono','evento_id_evento')
	
		       
class LugarSerializer(serializers.ModelSerializer):
    class Meta:
     model = Lugar
     fields =('id_lugar','nombre','direccion')

class postLugarSerializer(serializers.ModelSerializer):
    class Meta:
     model = Lugar
     fields =('nombre','direccion')
	
class MiseventosSerializer(serializers.ModelSerializer):
    class Meta:
     model = Miseventos
     fields =('id_mis_eventos','cliente_id_cliente','evento_id_evento','mi_puntuacion')

class postMiseventosSerializer(serializers.ModelSerializer):
    class Meta:
     model = Miseventos
     fields =('cliente_id_cliente','evento_id_evento','mi_puntuacion')
	###Fin acceso basico a tablas de de  la App