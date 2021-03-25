from django.urls import path
from .views import BookmarkListView

urlpatterns = [
    # http://localhost:8000/bookmark/
    path('', BookmarkListView.as_view(), name='list'),
]
