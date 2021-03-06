from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from .models import Poduser, Episode, Podcast
from .forms import PoduserForm, LoginForm, PodcastForm, EpisodeForm, UserPodcastForm, UserEpisodeForm
from django.core import serializers
from ipware import get_client_ip 
import hashlib  


# Home page
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

# Forgot password page
def forgot_password_view(request, *args, **kwargs):
    return render(request, 'forgot-password.html', {})

# Creates a new account 
def signup_view(request):
    username = None
    if request.method == 'GET':
        form = PoduserForm()
    else:
        form = PoduserForm(request.POST or None, request.FILES)
        if request.session.has_key('username'):
            request.session.flush()
        if form.is_valid(): # If the form is valid, the passwords are retreived to be encrypted and then saved using encrypted_form
            username = form.cleaned_data['username'] # Username is retreived to be put into the session and automatically log in the user once they signup
            password = form.cleaned_data['password']
            password_confirmation = form.cleaned_data['password_confirmation']
            request.session['username'] = username 
            encrypted_form = form.save(commit=False)
            encrypted_form.password = (hashlib.md5(password.encode())).hexdigest()
            encrypted_form.password_confirmation = (hashlib.md5(password_confirmation.encode())).hexdigest()
            encrypted_form.save()
            form = PoduserForm()
            return redirect('/user-dashboard/')

    context = {
        'form': form
    }
    return render(request, 'signup.html', context) 

# Logs in the user into their account
def login_view(request, *args, **kwargs):
    username = None 
    form = LoginForm(request.POST or None, request.FILES)
    if request.session.has_key('username'): # If the user reaches this page (presses on logout btn) 
        request.session.flush() # flush ensures that the session data is deleted and the user is properly logged out 
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        encrypted_password = (hashlib.md5(password.encode())).hexdigest()
        # User's input password is encrypted and then compared with the stored encrypted password value
        if Poduser.objects.filter(username=request.POST['username'], password=encrypted_password).exists(): 
            request.session['username'] = username
            return redirect('/user-dashboard/')
        else:
            username = None 
    else: 
        form = LoginForm()
    context = {
        'form': form,
        'name': username
    }
    return render(request, 'login.html', context)

# Shows user's dashboard with podcasts listed 
def user_view(request, *args, **kwargs):
    if 'username' in request.session:
        username = request.session['username']
    queryset = Podcast.objects.filter(username = username)
    queryset_poduser = Poduser.objects.get(username = username)
    context = {
        'username': username,
        'object_list': queryset,
        'poduser': queryset_poduser
    }
    return render(request, "user-dashboard.html", context)

# Creates a podcast
# User inputs into UserForm and then the inputs + username are put in the POST request to be inputted
# into the DB using form
def create_podcast_view (request):
    if request.method == 'GET':
        userForm = UserPodcastForm()
    else:
        userForm = UserPodcastForm(request.POST or None, request.FILES)
        if userForm.is_valid():
            request.POST = {
                'username': request.session['username'],
                'name': userForm.cleaned_data['name'],
                'author': userForm.cleaned_data['author'],
                'description': userForm.cleaned_data['description'],
                'published_date': userForm.cleaned_data['published_date'],
                'podcast_image': userForm.cleaned_data['podcast_image']
            }
            form = PodcastForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/user-dashboard/')
            else:
                print(form.errors)
        else: 
            print(userForm.errors)

    context = {
        'userForm': userForm
    }
    return render(request, 'create-podcast.html', context)

# Creates a new episode
# User inputs into UserForm and then the inputs + podcast id are put in the POST request to be inputted
# into the DB using form
def create_episode_view(request, id):
    if request.method == 'GET':
        userForm = UserEpisodeForm()
        print('request method GET')
    else:
        userForm = UserEpisodeForm(request.POST or None, request.FILES)
        if userForm.is_valid():
            print('valid episode user form')
            request.POST = {
                'podcast_id': id,
                'name': userForm.cleaned_data['name'],
                'description': userForm.cleaned_data['description'],
                'episode_mp3': userForm.cleaned_data['episode_mp3'],
                'episode_image': userForm.cleaned_data['episode_image'],
                'published_date': userForm.cleaned_data['published_date']
            }
            form = EpisodeForm(request.POST or None, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('../')
            else:
                print(form.errors)
        else: 
            print(userForm.errors)

    context = {
        'userForm': userForm
    }
    return render(request, 'create-episode.html', context)

# Shows the podcast with its episodes and details    
def podcast_view(request, id):
    obj = Podcast.objects.get(id=id)
    queryset = Episode.objects.filter(podcast_id = id)
    host_ip = request.get_host()
    context = {
        'object': obj, 
        'object_list': queryset,
        'ip': host_ip
    }
    return render(request, 'podcast-dashboard.html', context)

# Deletes podcasts
def delete_podcast_view(request, id):
    obj = get_object_or_404(Podcast, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/user-dashboard/')
    context = {
        'object': obj 
    }
    return render(request, 'delete-podcast.html', context)

# Deletes episodes
def delete_episode_view(request, id):
    obj = get_object_or_404(Episode, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/user-dashboard/')
    context = {
        'object': obj
    }
    return render(request, 'delete-episode.html', context)

# Returns XML file as a string 
def server_podcast_rss_feed(request):
    request.method = 'GET'
    queryset_podcast = Podcast.objects.filter(id = request.GET['id']).values('name')
    queryset_episode = Episode.objects.filter(podcast_id = request.GET['id']).values('name', 'published_date', 'episode_image', 'episode_mp3')
    podcast_name = list(queryset_podcast)[0]['name']
    podcast_image_url = list(Podcast.objects.filter(id = request.GET['id']))[0].podcast_image.url
    episodes_media_list = list(Episode.objects.filter(podcast_id = request.GET['id']))
    episodes_list = list(queryset_episode)
    episodes = []
    host_ip = request.get_host()
    for episode, media in (zip(episodes_list, episodes_media_list)):
        episode_details = '  <item>' +'\n    <pubDate>' + str(episode['published_date']) + '</pubDate>' + '\n  \
            <itunes:image href="' + request.scheme + '://' + host_ip + media.episode_image.url + '"/>' + '\n    \
            <title>' + episode['name'] + '</title>' + '\n    <enclosure url="' + request.scheme + '://' + host_ip \
            + media.episode_mp3.url +  '"/>' + '\n  </item>'
        episodes.append(episode_details)    
    combined = "\n"
    combined = combined.join(episodes)

    context = {
        'xml': '<rss version="2.0">' '\n <channel>' + '\n   <title>' + podcast_name + '</title>' + ' \n   \
        <itunes:image href="' + request.scheme + '://' + host_ip + podcast_image_url + '"/> \n' +  combined \
            + '\n </channel>' + '\n</rss>'
    }

    return redirect(request, '', context)

