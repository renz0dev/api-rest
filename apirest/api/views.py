from django.http import JsonResponse
from . models import Curso
import json
from django.views.decorators.csrf import csrf_exempt


def index(request):
    context = {
        'status':True,
        'content':'mi primer api rest con django'
    }
    
    return JsonResponse(context)

def curso(request):
    listado_cursos = Curso.objects.all()

    context = {
        'status':True,
        'content':list(listado_cursos.values())
    }

    return JsonResponse(context)

@csrf_exempt
def post_curso(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        json_data = json.loads(body_unicode)
        
        titulo = json_data['titulo']
        descripcion = json_data['descripcion']
        image = json_data['image']

        nuevo_curso = Curso.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            image=image
        )

        dic_nuevo_curso = {
            'id':nuevo_curso.id,
            'descripcion':nuevo_curso.descripcion,
            'image':nuevo_curso.image
        }

        context = {
            'status':True,
            'content':dic_nuevo_curso
        }

        return JsonResponse(context)
        
""" uso de drf """

from rest_framework import generics
from rest_framework import serializers

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class CursoList(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer