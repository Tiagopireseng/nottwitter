from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('login/', views.login_api, name='login'),
    path('user/', views.get_user_data, name='get_user_data'),
    path('tweets/', views.TweetViewSet.as_view({"get":"list"}), name='tweets'),
]
