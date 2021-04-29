from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('users/search', views.user_search, name='user_search'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('users/create', views.create_user, name='create_user'),
    path('users/' + '<int:pk>' + '/update', views.update_user, name='update_user'),
    path('users/' + '<int:pk>' + '/delete', views.delete_user, name='delete_user'),
]