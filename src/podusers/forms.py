from django import forms
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from .models import Poduser, Podcast, Episode
from django.forms import Field
from django.utils.translation import ugettext_lazy
import hashlib

#UserForm is what is visibile to the user
#Form is what is sent to the DB

#Poduser model forms
class PoduserForm(forms.ModelForm):
    class Meta: 
        model = Poduser
        fields = [
            'name',
            'phone_number',
            'email',
            'city',
            'country',
            'bio',
            'profile_picture',
            'password',
            'password_confirmation', 
            'username'
        ]

        widgets = {
            'bio': forms.TextInput(attrs={'class': 'bio-class'}),
            'password': forms.PasswordInput(),
            'password_confirmation': forms.PasswordInput()
        }


    def clean(self):
        cleaned_data = super(PoduserForm, self).clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password != password_confirmation:
            raise forms.ValidationError(
                "password and password_confirmation does not match"
            )
      

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    fields = [
        'username',
        'password'
    ]
 
#Podcast model forms
class PodcastForm(forms.ModelForm):
    class Meta: 
        model = Podcast
        fields = [
            'username',
            'name',
            'description',
            'author',
            'published_date',
            'podcast_image', 
        ]

class UserPodcastForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(required=False)
    author = forms.CharField(required=False)
    published_date = forms.DateField(required=False)
    podcast_image = forms.ImageField(required=False)

    fields = [
        'name',
        'description',
        'author',
        'published_date',
        'podcast_image',
    ]

#Episode model forms
class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = [
            'podcast_id',
            'name',
            'description',
            'episode_mp3',
            'episode_image',
            'published_date'
        ]
    
class UserEpisodeForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(required=False)
    episode_mp3 = forms.FileField(required=False)
    episode_image = forms.ImageField(required=False)
    published_date = forms.DateField(required=False)
    
    fields = [
        'name',
        'description',
        'episode_mp3',
        'episode_image',
        'published_date'
    ]
