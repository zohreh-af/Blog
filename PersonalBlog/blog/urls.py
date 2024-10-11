from django.urls import path
from . import views
app_name = "blog"
urlpatterns = [
    path('',views.HomepageView.as_view(),name="home"),
    path("posts/",views.PostListView.as_view(),name="posts_page"),
    path("posts/<slug:slug>",views.PostDetailView.as_view(),name="post_detail"),
    path("delete_post/<int:post_id>",views.DeleteView.as_view(),name="post_delete"),
    path("create_post/",views.CreatePostView.as_view(),name="create_post"),
    path("update_posts/<int:post_id>",views.UpdatePostView.as_view(),name="post_update"),
    path('reply/<int:post_id>/<int:comment_id>',views.PostAddReplyView.as_view(),name="add_reply"),
    path("like/<int:post_id>/", views.PostLikeView.as_view(), name="post_like"),
    
]
