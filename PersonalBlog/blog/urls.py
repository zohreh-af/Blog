from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name="index"),
    path("posts/",views.postList,name="posts"),
    path("posts/<slug:slug",views.postDetail,name="post_detail"),
    
]
