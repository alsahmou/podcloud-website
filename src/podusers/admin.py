from django.contrib import admin

from .models import Poduser, Episode, Podcast

#Register each model here

admin.site.register(Poduser)
admin.site.register(Episode)
admin.site.register(Podcast)

