from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import *
from serializers import *

####inicio
@api_view(['GET', 'POST'])
def Cliente_list(request):
    """
    List all tasks, or create a new Cliente.
    """
    if request.method == 'GET':
        tasks = Cliente.objects.all()
        serializer = ClienteSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =postClienteSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Cliente_detail(request, pk):

    """
    Get, udpate, or delete un Cliente 
    """
    try:
        task = Cliente.objects.get(pk=pk)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClienteSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClienteSerializer(task, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
##Finn


####inicio Evento
@api_view(['GET', 'POST'])
def Evento_list(request):
    """
    Crear un nuevo evento u obtener todos
    """
    if request.method == 'GET':
        tasks = Evento.objects.all()
        serializer = EventoSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =postEventoSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Evento_detail(request, pk):

    """
    Get, udpate, or delete un Evento especifico
    """
    try:
        task = Evento.objects.get(pk=pk)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventoSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EventoSerializer(task, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
##Fin Evento

####inicio
@api_view(['GET', 'POST'])
def Categoria_list(request):
    """
    Obtener todas las categorias o crear una nueva.
    """
    if request.method == 'GET':
        tasks = Categoria.objects.all()
        serializer = CategoriaSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =postCategoriaSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Categoria_detail(request, pk):

    """
    Get, udpate, or delete una categoria especifica
    """
    try:
        task = Categoria.objects.get(pk=pk)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriaSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategoriaSerializer(task, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
##Finn
###Inicio Telefono
@api_view(['GET', 'POST'])
def Telefonos_list(request):
    """
    Obtener todos los telefonos o crear uno nuevo
    """
    if request.method == 'GET':
        tasks = Telefonos.objects.all()
        serializer = TelefonosSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =postTelefonosSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Telefonos_detail(request, pk):

    """
    Get, udpate, or delete Telefonos
    """
    try:
        task = Telefonos.objects.get(pk=pk)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TelefonosSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TelefonosSerializer(task, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##Fin Telefono


##Inicio Lugar
@api_view(['GET', 'POST'])
def Lugar_list(request):
    """
    Obtener todos los lugrares o crear uno nuevo.
    """
    if request.method == 'GET':
        tasks = Lugar.objects.all()
        serializer = LugarSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =postLugarSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Lugar_detail(request, pk):

    """
    Get, udpate, or delete Lugar
    """
    try:
        task = Lugar.objects.get(pk=pk)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LugarSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LugarSerializer(task, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##Fin lugar


##Inicio MisEventos
@api_view(['GET', 'POST'])
def Miseventos_list(request):
    """
    Obtener todos Miseventos o crear uno nuevo.
    """
    if request.method == 'GET':
        tasks = Miseventos.objects.all()
        serializer = MiseventosSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =postMiseventosSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Miseventos_detail(request, pk):

    """
    Get, udpate, or delete Miseventos
    """
    try:
        task = Miseventos.objects.get(pk=pk)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MiseventosSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MiseventosSerializer(task, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##Fin Mis eventos fin acceso basico

@api_view(['GET'])
def EventosCliente_list(request,pk):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        tasks = Miseventos.objects.get(cliente_id_cliente=pk)
	  
        serializer = TelefonosSerializer(tasks, many=True)
        return Response(serializer.data)