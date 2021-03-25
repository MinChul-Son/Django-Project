from django.shortcuts import render

# Create your views here.
# CRUD ==> Create / Read / Update / Delete
# 뷰에는 클래스형 뷰 / 함수형 뷰가 존재

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'
