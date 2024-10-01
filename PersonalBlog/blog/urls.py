from django.urls import path
from . import views
app_name = "blog"
urlpatterns = [
    path('',views.HomepageListView.as_view(),name="home"),
    path("posts/",views.PostListView.as_view(),name="posts_page"),
    path("posts/<slug:slug>",views.PostDetailView.as_view(),name="post_detail"),
    path("delete_post/<slug:slug>",views.DeleteView.as_view(),name="delete_post"),
    path("create_post/",views.CreatePostView.as_view(),name="create_post"),
    path("update_posts/<slug:slug>",views.UpdatePostView.as_view(),name="update_post"),
    
    
    
]
