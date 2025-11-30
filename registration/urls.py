from django.urls import path
from . import views

app_name = "registration"

urlpatterns = [
<<<<<<< HEAD
    # API Routes
    path('api/register/', views.register_user, name='register_user'),
    path('api/users/', views.list_users, name='list_users'),
    path('api/users/<int:pk>/', views.user_detail, name='user_detail'),

    # HTML Routes (CRUD)
    path('users/', views.users_html, name='users_html'),
    path('users/add/', views.user_create_html, name='user_create_html'),
    path('users/<int:pk>/edit/', views.user_update_html, name='user_update_html'),
    path('users/<int:pk>/delete/', views.user_delete_html, name='user_delete_html'),

    # Auth Routes
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('signup/', views.public_register_view, name='signup_view'),

    # --- ADMIN PROFILE ROUTES ---
    path('admin/profile/', views.admin_profile, name='admin_profile'),
    path('admin/profile/edit/', views.admin_profile_edit, name='admin_profile_edit'),
=======
       path('api/register/', views.register_user, name='register_user'),
       path('api/users/', views.list_users, name='list_users'),  
       path('api/users/<int:pk>/', views.user_detail, name='user_detail'),

       path('users/', views.users_html, name='users_html'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
>>>>>>> 02cfd2272afaecbf5b9240bcb4de7a4c76483c42
]