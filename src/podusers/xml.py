from django.core import serializers
from .models import Poduser, Podcast, Episode
from django.http import HttpResponse

def list(request):
    queryset = Episode.objects.all()
    queryset = serializers.serialize('xml', queryset)
    return HttpResponse(queryset, content_type='application/xml')