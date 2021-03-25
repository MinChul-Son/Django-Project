from django.shortcuts import render

# Create your views here.
# CRUD ==> Create / Read / Update / Delete
# 뷰에는 클래스형 뷰 / 함수형 뷰가 존재

from django.views.generic.list import ListView
from .models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
