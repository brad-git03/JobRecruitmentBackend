from django.shortcuts import render

def homepage_view(request):
    return render(request, 'homepage.html')

def admin_dashboard_view(request):
    return render(request, 'admin_dashboard.html')
