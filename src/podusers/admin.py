from django.contrib import admin

from .models import Poduser, Episode, Podcast

admin.site.register(Poduser)
admin.site.register(Episode)
admin.site.register(Podcast)

