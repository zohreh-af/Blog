from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomepageListView.as_view(),name="home"),
    path("posts/",views.PostListView.as_view(),name="posts_page"),
    path("posts/<slug:slug>",views.PostDetailView.as_view(),name="post_detail"),
    path("author/<int:id>",views.AuthorDetailView.as_view(),name="author_detail"),
    
]
