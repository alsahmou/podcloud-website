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
from podusers.models import Poduser, Podcast
from django.conf.urls.static import static
from django.conf import settings
from podusers.views import (
    home_view, 
    signup_view,
    login_view,
    forgot_password_view,
    user_view, 
    create_podcast_view, 
    podcast_view, 
    create_episode_view, 
    delete_podcast_view, 
    delete_episode_view,
    server_podcast_rss_feed 
)     

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('forgot-password', forgot_password_view, name='forgot_password'),
    path('user-dashboard/', user_view, name='user-dashboard'),
    path('user-dashboard/create-podcast', create_podcast_view, name='create-podcast'),
    path('user-dashboard/podcast/<int:id>/', podcast_view, name='podcast'),
    path('user-dashboard/podcast/<int:id>/create_episode/', create_episode_view, name='create_episode'),
    path('podcast/<int:id>/delete/', delete_podcast_view, name='podcast_delete'),
    path('user-dashboard/episode/<int:id>/delete/', delete_episode_view, name='episode_delete'),
    path('podcast/xml', server_podcast_rss_feed, name='xml_file' ),
    path('podcast-xml', server_podcast_rss_feed, name='example')
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
