"""PodCloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from podusers.views import (
    episode_view,
    home_view, 
    signup_view,
    welcome_view,
    login_view, 
    create_podcast_view, 
    create_episode_view, 
    podcast_view, 
    delete_podcast_view, 
    delete_episode_view,
    xml_view,
    example,
    forgot_password_view,
    
) 
from podusers.models import Poduser, Podcast
from django.conf.urls.static import static
from django.conf import settings    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('welcome/', welcome_view, name='welcome'),
    path('login/', login_view, name='login'),
    path('create_podcast/', create_podcast_view, name='create_podcast'),
    path('podcast/<int:id>/create_episode/', create_episode_view, name='create_episode'),
    path('podcast/<int:id>/', podcast_view, name='podcast'),
    path('podcast/<int:id>/delete/', delete_podcast_view, name='podcast_delete'),
    path('episode/<int:id>/', episode_view, name='episode'),
    path('episode/<int:id>/delete/', delete_episode_view, name='episode_delete'),
    path('episode/xml', xml_view, name='xml_file' ),
    path('hi/', example, name='example'),
    path('', home_view, name='home'),
    path('forgot-password', forgot_password_view, name='forgot_password')

    #path('episode/<int:id>.mp3')
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
