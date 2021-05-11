from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, Textarea, FileInput, IntegerField
from django.forms import TextInput, Textarea, FileInput, Select, CheckboxInput

from .models import *


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с логином {username} не найден в системе.')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    nickname = forms.CharField(widget=forms.TextInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nickname'].label = 'Ник'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердите пароль'
        self.fields['phone'].label = 'Номер телефона'
        self.fields['email'].label = 'Электронная почта'

    def clean_email(self):
        email = self.cleaned_data['email']
        domain = email.split('.')[-1]
        if domain in ['ua', 'net']:
            raise forms.ValidationError(f'Регистрация для домена "{domain}" невозможна')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Такой адрес электронной почты уже зарегестрирован')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с именем "{username}" уже зарегестрирован')
        return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError(f'Пароли не совпадают')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'confirm_password', 'phone', 'email']


class TournamentsRegistrationForm(forms.ModelForm):
    class Meta:
        model = TournamentRegistration
        fields = {'tournaments', 'user'}


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = {'user', 'text'}


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title', 'text', 'image_list', 'image_news', 'author', 'categories', 'publish_date', 'publish_time', 'slug',
            'draft'
        ]
        widgets = {
            'title': TextInput(attrs={
                'class': 'commentId',
                'placeholder': 'Название новости',
            }),
            'text': Textarea(attrs={
                'class': 'editContent',
                'placeholder': 'Текст новости',
            }),
            'draft': TextInput(attrs={
                'placeholder': 'Опубликовать'
            }),
            'image': FileInput(attrs={
                'class': 'add-image-form',
            }),
            'url': TextInput(attrs={
                'placeholder': 'url',
            }),
        }


class AddTournamentForm(forms.ModelForm):
    max_teams = forms.IntegerField(required=True)

    # teams_count = forms.IntegerField(initial=0, widget=forms.HiddenInput)

    class Meta:
        model = Tournaments
        fields = [
            'name', 'description', 'image', 'prize', 'game', 'start_date', 'start_registration_date',
            'end_registration_date', 'slug', 'status', 'max_teams'
        ]
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Название турнира'
            }),
            'description': Textarea(attrs={
                'placeholder': 'Описание турнира'
            }),
            'prize': TextInput(attrs={
                'placeholder': 'Призовой фонд',
            }),
            'game': Select(attrs={
                'placeholder': 'Игра',
            }),
            'image': FileInput(attrs={
                'class': 'add-image-form',
            }),
            'start_date': TextInput(attrs={
                'placeholder': 'дата начала регистрации',
                'class': 'datepicker_start',
            }),
            'start_registration_date': TextInput(attrs={
                'placeholder': 'дата начала регистрации',
                'class': 'datepicker_start_registration'
            }),
            'end_registration_date': TextInput(attrs={
                'placeholder': 'дата конца регистрации',
                'class': 'datepicker_end_registration'
            }),
            'status': TextInput(attrs={
                'placeholder': 'статус турнира'
            }),
        }


class CreateKeyForm(forms.ModelForm):
    class Meta:
        model = Key
        fields = {
            'team', 'key'
        }


class CreateTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = {'name', 'tag', 'logo', 'slug'}
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Название тимы',
            }),
            'tag': TextInput(attrs={
                'placeholder': 'Текст новости',
            }),
            'image': FileInput(attrs={
            }),
            'slug': TextInput(attrs={
                'placeholder': 'url',
            }),
        }


class JoinTeamForm(forms.Form):
    key = forms.CharField(label='key', max_length=20)

    class Meta:
        model = Key
        fields = {'key'}


class ExitTeamForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {'team'}
