from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from .models import Poduser, Episode, Podcast
from .forms import PoduserForm, LoginForm, PodcastForm, EpisodeForm, UserPodcastForm, UserEpisodeForm
from django.core import serializers
from ipware import get_client_ip   


# Create your views here.
#def home_view(request, *args, **kwargs):
#    print(request.get_host(), 'host IP')
#    ip, is_routable = get_client_ip(request)
#    print (request.META['SERVER_PORT'], 'port number')
#    print(request.scheme, 'request scheme')
#    if ip is None:
#        print('IP is NONE')
#    else:
#        print('IP is valid')
#        if is_routable:
#            print('IP is public')
#        else:
#            print('private IP')
#            print(ip, 'IP')
#    return HttpResponse("<h1>Welcome to PodCloud</h1>")
#    #return render(request, "home.html", {})

def home_view(request, *args, **kwargs):
    print('page rendered')
    return render(request, "home.html", {})

def signup_view(request):
    print('sign up page rendered')
    username = None
    if request.method == 'GET':
        form = PoduserForm()
        print('request method GET')
    else:
        print('request method POST')
        form = PoduserForm(request.POST or None, request.FILES)
        if request.session.has_key('username'):
            request.session.flush()
        print(form.errors)
        if form.is_valid():
            username = form.cleaned_data['username']
            request.session['username'] = username
            form.save()
            form = PoduserForm()
            return redirect('/welcome/')

    context = {
        'form': form
    }
    return render(request, 'signup.html', context)

def login_view(request, *args, **kwargs):
    print('page rendered')
    username = None 
    form = LoginForm(request.POST or None, request.FILES)
    if request.session.has_key('username'):
        request.session.flush()
    if form.is_valid():
        username = form.cleaned_data['username']
        if Poduser.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            request.session['username'] = username
            print('correct username and password')
            print(request.session.session_key, 'key at username and pass')
            return redirect('/welcome/')
        else:
            username = None 
            print('incorrect username and password')
    else: 
        form = LoginForm()
    context = {
        'form': form,
        'name': username
    }
    return render(request, 'login.html', context)

def welcome_view(request, *args, **kwargs):
    print(request.session.session_key, 'key at welcome')
    if 'username' in request.session:
        username = request.session['username']
        print(username)
    queryset = Podcast.objects.filter(username = username)
    queryset_poduser = Poduser.objects.get(username = username)
    print(queryset_poduser, 'poduser object')
    context = {
        'username': username,
        'object_list': queryset,
        'poduser': queryset_poduser
    }
    return render(request, "user-dashboard.html", context)

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
                return redirect('/welcome/')
            else:
                print(form.errors, 'form errors')
                print('invalid episode form')
        else: 
            print('invalid user epsiode form')
            print(userForm.errors)

    context = {
        'userForm': userForm
    }
    return render(request, 'create-episode.html', context)

def create_podcast_view (request):
    if request.method == 'GET':
        userForm = UserPodcastForm()
        print('request method GET')
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
                print('vallid form')
                print(form.errors)

                form.save()
                return redirect('/welcome/')
            else:
                print(form.errors, 'form errors')
                print('invalid form')
        else: 
            print('invalid user form')
            print(userForm.errors)

    context = {
        'userForm': userForm
    }
    return render(request, 'create-podcast.html', context)
    
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

def episode_view(request, id):
    obj = Episode.objects.get(id=id)
    context = {
        'object': obj
    }
    return render(request, 'episode-dashboard.html', context)

def delete_episode_view(request, id):
    obj = get_object_or_404(Episode, id=id)
    print(obj)
    if request.method == 'POST':
        obj.delete()
        return redirect('/welcome/')
    context = {
        'object': obj
    }
    return render(request, 'delete-episode.html', context)


def delete_podcast_view(request, id):
    obj = get_object_or_404(Podcast, id=id)
    print(obj)
    if request.method == 'POST':
        obj.delete()
        return redirect('/welcome/')
    context = {
        'object': obj 
    }
    return render(request, 'delete-podcast.html', context)


from .models import Poduser, Podcast, Episode
from django.http import HttpResponse

def xml_view(request):
    queryset = Episode.objects.all()
    queryset = serializers.serialize('xml', queryset)
    return HttpResponse(queryset, content_type='application/xml')


#def example(request):
#    #print(request.GET)
#    request.method == 'GET'
#    print(request.GET['id'], 'ID in URL')
#    queryset_podcast = Podcast.objects.filter(id = request.GET['id']).values('name', 'podcast_image')
#    queryset_episode = Episode.objects.filter(podcast_id = request.GET['id']).values('name', 'published_date', 'episode_image', 'episode_mp3')
#    #print(queryset_podcast, 'podcast printed')
#    #print(queryset_episode, 'episodes list')
#    print(list(queryset_podcast)[0]['name'], 'list podcast')
#    podcast_name = list(queryset_podcast)[0]['name']
#    print(podcast_name, 'podcast name')
#    podcast_list_name = list(podcast_name)
#    podcast_dict_name = podcast_name + "/>"
#    print(podcast_dict_name, 'podcast dict name')
#    print(podcast_list_name, 'podcast list name')
#    #print(queryset_podcast.name, 'podcast name')
#    #dict = {
#        #'Podcast': queryset_podcast,
#        #'Episode': queryset_episode
#    #}
#    dict = {
#        '<podcast name = ': podcast_dict_name,
#    }
#    l = [queryset_podcast, queryset_episode]
#    return HttpResponse('<podcast name = "' + podcast_name + '"> <episode name="episode 1"/>  <episode name="episode 2"/> <episode name="episode 3"/>  </podcast>')
#    #print(dir(queryset_one))
#    #return HttpResponse(value=podcast_name)
#    #return HttpResponse('{<podcast name = "aaa" <episode name="Episode 1" <episode name = "Episode 2"/>}')
#    #return HttpResponse('<queryset_podcast/>'.format(val))
#    #return HttpResponse("{}".format(dict))
#    #return HttpResponse(status=<100>, content="some content")
#    #l1 = [podcast_name]
#    #return HttpResponse("{}".format(l1))
#    #return HttpResponse("{}".format('<podcast_name/>'))
#    return HttpResponse ('{<podcast name = />}', podcast_name)

def example(request):
    request.method = 'GET'
    queryset_podcast = Podcast.objects.filter(id = request.GET['id']).values('name')
    queryset_episode = Episode.objects.filter(podcast_id = request.GET['id']).values('name', 'published_date', 'episode_image', 'episode_mp3')
    podcast_name = list(queryset_podcast)[0]['name']
    podcast_image_url = list(Podcast.objects.filter(id = request.GET['id']))[0].podcast_image.url
    episodes_media_list = list(Episode.objects.filter(podcast_id = request.GET['id']))
    episodes_list = list(queryset_episode)
    episodes = []
    host_ip = request.get_host()
    print(host_ip, 'host IP')
    ip = get_client_ip(request)
    port = request.META['SERVER_PORT']
    #for episode, media in (zip(episodes_list, episodes_media_list)):
    #    episode_details = '<episode name = "' + episode['name'] + '"\n imgurl = ' + '"http://127.0.0.1:8000' + media.episode_image.url + '" \n audiourl = ' + '"http://127.0.0.1:8000' + media.episode_mp3.url + '"\n date = "' + str(episode['published_date']) + '"/>'
    #    episodes.append(episode_details)
    for episode, media in (zip(episodes_list, episodes_media_list)):
        episode_details = '  <item>' +'\n    <pubDate>' + str(episode['published_date']) + '</pubDate>' + '\n    <itunes:image href="' + request.scheme + '://' + host_ip + media.episode_image.url + '"/>' + '\n    <title>' + episode['name'] + '</title>' + '\n    <enclosure url="' + request.scheme + '://' + host_ip + media.episode_mp3.url +  '"/>' + '\n  </item>'
        episodes.append(episode_details)    
    combined = "\n"
    combined = combined.join(episodes)
    return HttpResponse('<rss version="2.0">' '\n <channel>' + '\n   <title>' + podcast_name + '</title>' + ' \n   <itunes:image href="' + request.scheme + '://' + host_ip + podcast_image_url + '"/> \n' +  combined + '\n </channel>' + '\n</rss>')

