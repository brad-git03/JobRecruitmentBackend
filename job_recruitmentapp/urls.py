from django.urls import path
from . import views

app_name = "jobs" 

urlpatterns = [

       # HTML CRUD 
         path('list/', views.jobs_html, name='jobs_html'),
       path('add/', views.job_create_html, name='job_create_html'),
       path('<int:pk>/edit/', views.job_update_html, name='job_update_html'),
       path('<int:pk>/delete/', views.job_delete_html, name='job_delete_html'),
]