from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('users/search', views.user_search, name='user_search'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('user/info/', views.user_info, name='user_info'),
    path('users/list/', views.users_list, name='users_list'),
    path('users/<int:pk>', views.update_user_role, name='update_user_role'),
    path('users/create', views.create_user, name='create_user'),
    path('users/' + '<int:pk>' + '/update', views.update_user, name='update_user'),
    path('users/' + '<int:pk>' + '/delete', views.delete_user, name='delete_user'),
    path('users/get_current_user', views.get_current_user, name='get_current_user')
]