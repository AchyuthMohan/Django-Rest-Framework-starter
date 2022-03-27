from curses import meta
from dataclasses import field
from importlib.metadata import requires
from tkinter.ttk import Style
from turtle import title
# from typing_extensions import Required
from urllib import request
from rest_framework import serializers
from api_basic.models import Snippet
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    owner=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Snippet
        fields=['id','title','code','linenos','language','owner']

class UserSerializer(serializers.ModelSerializer):
    snippets=serializers.PrimaryKeyRelatedField(many=True,queryset=Snippet.objects.all())

    class Meta:
        model=User
        fields=['id','username','snippets']