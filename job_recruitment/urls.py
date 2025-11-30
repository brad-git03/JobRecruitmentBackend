<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from . import views  # This looks for views.py in the job_recruitment folder
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- HOMEPAGE IS HANDLED HERE ---
    path('', views.homepage_view, name='home_html'),
    path('dashboard/', views.admin_dashboard_view, name='admin_dashboard'),

    # --- APP LINKS ---
    path('jobs/', include('job_recruitmentapp.urls')),
    path('registration/', include('registration.urls')),
    # If you created the userapp, keep this line. If not, comment it out:
    path('candidate/', include('userapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
"""
URL configuration for job_recruitment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage_view, name='home_html'),
    path('jobs/', include('job_recruitmentapp.urls')),
    path('registration/', include('registration.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 02cfd2272afaecbf5b9240bcb4de7a4c76483c42
