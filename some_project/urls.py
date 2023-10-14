from django.contrib import admin
from django.urls import path
from some_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name = "index"),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
]
