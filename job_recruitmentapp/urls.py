from django.urls import path
from . import views

app_name = "jobs" 

urlpatterns = [
<<<<<<< HEAD
    # Job CRUD
    path('list/', views.jobs_html, name='jobs_html'),
    path('add/', views.job_create_html, name='job_create_html'),
    path('<int:pk>/edit/', views.job_update_html, name='job_update_html'),
    path('<int:pk>/delete/', views.job_delete_html, name='job_delete_html'),

    # Dashboard Features
    path('applicants/', views.application_list, name='application_list'),
    path('tasks/', views.pending_tasks, name='pending_tasks'),
    path('settings/', views.system_settings, name='system_settings'),

    # Interview Routes
    path('interviews/', views.interview_list, name='interview_list'),
    path('interviews/schedule/<int:application_id>/', views.interview_create, name='interview_create'),

    # --- NEW REVIEW ROUTE (Fixes the button) ---
    path('review/<int:pk>/', views.review_application, name='review_application'),
=======

       # HTML CRUD 
         path('list/', views.jobs_html, name='jobs_html'),
       path('add/', views.job_create_html, name='job_create_html'),
       path('<int:pk>/edit/', views.job_update_html, name='job_update_html'),
       path('<int:pk>/delete/', views.job_delete_html, name='job_delete_html'),
>>>>>>> 02cfd2272afaecbf5b9240bcb4de7a4c76483c42
]