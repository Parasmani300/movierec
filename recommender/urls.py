from django.conf.urls import url
from recommender import views
from django.urls import path

app_name = 'recommender'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    url(r'^update_user/(?P<id>.*?)/$',views.update_profile,name="update_user")
]