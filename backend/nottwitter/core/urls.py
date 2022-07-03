from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'seguir', views.SeguirViewSet)
router.register(r'tweet', views.TweetViewSet)


urlpatterns = [
    path('', views.base, name='base'),
    path('login/', views.login_api, name='login'),
    path('user/', views.get_user_data, name='get_user_data'),
    path('', include(router.urls)),
]
