from django import forms
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest

from .models import Poduser, Podcast, Episode

from django.forms import Field
from django.utils.translation import ugettext_lazy
from passlib.hash import pbkdf2_sha256
import hashlib


#class PoduserForm(forms.ModelForm):
#    class Meta: 
#        model = Poduser
#        fields = [
#            'name',
#            'phone_number',
#            'email',
#            'city',
#            'country',
#            'bio',
#            'profile_picture',
#            'password',
#            'password_confirmation', 
#            'username',
#            
#        ]
#        
#        widgets = {
#            'bio': forms.TextInput(),
#            'password': forms.PasswordInput(),
#            'password_confirmation': forms.PasswordInput(),
#            'name': forms.TextInput(),
#            'username': forms.TextInput(),
#            'email': forms.TextInput(),
#            'phone_number': forms.TextInput(),
#            'city': forms.TextInput(),
#            'country': forms.TextInput(),
#
#
#        }
#    
#    def clean_password(self):
#        cleaned_data = super(PoduserForm, self).clean()
#        print(cleaned_data, 'cleaned data')
#        password = cleaned_data.get("password")
#        password_confirmation = cleaned_data.get("password_confirmation")
#        print(password, 'password')
#        print(password_confirmation, 'confirmation')
#
#        if password != password_confirmation:
#            raise forms.ValidationError(
#                "Passwords do not match"
#            )

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

    #def encrypt(self):
    #    print('encrypting function')
    #    cleaned_data = super(PoduserForm, self).clean()
    #    password = cleaned_data.get("password")
    #    password_confirmation = cleaned_data.get("password_confirmation")
    #    password = (hashlib.md5(password.encode())).hexdigest() 
    #    password_confirmation = (hashlib.md5(password_confirmation.encode())).hexdigest()
    #    print('encrypted password', password)
    #    return password

    def clean(self):
        print('encrypting function')
        cleaned_data = super(PoduserForm, self).clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")
        password = (hashlib.md5(password.encode())).hexdigest()
        print('encrypted password', password)
        password_confirmation = (hashlib.md5(password_confirmation.encode())).hexdigest()
        print('encrypted confirmation', password_confirmation)

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
