from django.urls import path
from . import views
app_name = "blog"
urlpatterns = [
    path('',views.HomepageListView.as_view(),name="home"),
    path("posts/",views.PostListView.as_view(),name="posts_page"),
    path("posts/<slug:slug>",views.PostDetailView.as_view(),name="post_detail"),
    
]
