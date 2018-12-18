from django.shortcuts import render

# Create your views here.

def myjsonview(request ):
    contexto = {
        'a': 1,
        'b': 2,
        'c': 3
    }
    response = HttpResponse(json.dumps(contexto), content_type='application/json')
return response