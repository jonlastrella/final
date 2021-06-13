from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('signup', views.signup),
    path('signin', views.signin),
    path('signout', views.signout),
    path('dashboard', views.dashboard),
    path('profile/<int:userid>', views.profile),
    path('edit/<int:userid>', views.edit),
    path('aboutMe', views.aboutMe),
    path('postToProfile', views.postToProfile),
    path('news', views.news),
    path('profilePicture', views.profilePicture),
    # path('block/<int:userid>', views.block),
    # path('newsFilter', views.newsFilter),

    # path('addFriend'), views.addFriend),
]
