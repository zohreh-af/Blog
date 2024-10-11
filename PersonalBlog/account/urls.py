from django.urls import path
from . import views
app_name = "account"
urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name="register"),
    path("login/",views.UserLoginView.as_view(),name="login"),
    path("logout/",views.UserLogoutView.as_view(),name="logout"),
    path("profile/<int:user_id>/",views.ProfileView.as_view(),name="profile"),
    path("follow/<int:user_id>",views.UserFollowView.as_view(),name='user_follow'),
    #path("unfollow/<int:user_id>",views.UserUnfollowView.as_view(),name='user_unfollow'),
    path("edit_user/",views.EditUserView.as_view(),name="edit_user")
   
    
    
]
