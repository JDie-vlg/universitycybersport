from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, Textarea, FileInput, IntegerField, NumberInput
from django.forms import TextInput, Textarea, FileInput, Select, CheckboxInput

from .models import *


class AddServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = [
            'user', 'host', 'server_username', 'secret', 'ssh_port', "server_port"
        ]
        widgets = {
            'host': TextInput(attrs={
                'class': 'commentId',
                'placeholder': 'IP',
            }),
            'server_username': TextInput(attrs={
                'class': 'commentId',
                'placeholder': 'username',
            }),
            'secret': TextInput(attrs={
                'class': 'commentId',
                'placeholder': 'password',
            }),
            'ssh_port': NumberInput(),
            'server_port': NumberInput(),
        }


class StartServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = [
            'host', 'server_username', 'secret', 'ssh_port', "server_port"
        ]
        widgets = {
            'host': TextInput(attrs={
                'class': 'commentId',
                'placeholder': 'IP',
            }),
            'server_username': TextInput(attrs={
                'class': 'commentId',
                'placeholder': 'username',
            }),
            'secret': TextInput(attrs={
                'class': 'commentId',
                'placeholder': 'password',
            }),
            'ssh_port': NumberInput(),
            'server_port': NumberInput(),
        }
