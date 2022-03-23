from curses import meta
from dataclasses import field
from importlib.metadata import requires
from tkinter.ttk import Style
from turtle import title
from typing_extensions import Required
from urllib import request
from rest_framework import serializers
from api_basic.models import Snippet,LANGUAGE_CHOICES,STYLE_CHOICES
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Snippet
        fields=['id','title','code','linenos','language']