from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona
from django.core import serializers

# Create your views here.

def personaJson(request):
    personas = serializers.serialize('json', Persona.objects.all())
    response = HttpResponse(personas, content_type='application/json')
    return response


