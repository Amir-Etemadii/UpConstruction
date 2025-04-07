from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blogs'),
    path('detail/<int:pk>', views.blog_detail, name='blog_detail'),
]