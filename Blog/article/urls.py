from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.home,name="home"),
    path("all_posts/",views.all_posts,name="all_posts"),
    path("view_details/<int:pk>/",views.view_details,name="view_details"),
    path("delete/<int:pk>/",views.delete,name="delete"),
    path("create_post/",views.create_post,name="create_post"),
    path("edit_article/<int:pk>/",views.edit_article,name="edit_article"),
    path("delete_articles/<int:pk>/",views.delete_articles,name="delete_articles"),
    path("login/",views.login_page,name="login"),
    path("logout/",views.signout,name="logout"),
    path("signup/",views.signup,name="signup"),
]
