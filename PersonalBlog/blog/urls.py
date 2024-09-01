from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name="home"),
    path("posts/",views.postList,name="posts_page"),
    path("posts/<slug:slug>",views.postDetail,name="post_detail"),
    path("author/<pk:id>",views.authorDetail,name="author_detail"),
    
]
