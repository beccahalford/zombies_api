from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Map
from .serializers import MapSerializer


@csrf_exempt
def map_list(request):

    if request.method == 'GET':
        maps = Map.objects.all()
        serializer = MapSerializer(maps, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MapSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def map_detail(request, pk):
    try:
        zmap = Map.objects.get(pk=pk)
    except Map.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MapSerializer(zmap)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MapSerializer(zmap, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        zmap.delete()
        return HttpResponse(status=204)
