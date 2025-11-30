<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# Import safely to avoid circular dependency issues
try:
    from .models import JobPosting, JobApplication, Interview
    from registration.models import UserRegistration
except ImportError:
    pass

# --- JOB CRUD ---
def jobs_html(request):
    jobs = JobPosting.objects.all().order_by('-id')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_create_html(request):
    if request.method == 'POST':
        JobPosting.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            job_position=request.POST.get('position'),
            slots=request.POST.get('slots'),
            status=request.POST.get('status'),
            salary=request.POST.get('salary')
        )
        messages.success(request, "Job created successfully.")
        return redirect('jobs:jobs_html')
    return render(request, 'jobs/jobs_create.html')

def job_update_html(request, pk):
    job = get_object_or_404(JobPosting, pk=pk)
    if request.method == 'POST':
        job.title = request.POST.get('title')
        job.description = request.POST.get('description')
        job.job_position = request.POST.get('job_position')
        job.slots = request.POST.get('slots')
        job.status = request.POST.get('status')
        job.salary = request.POST.get('salary')
        job.save()
        messages.success(request, "Job updated.")
        return redirect('jobs:jobs_html')
    return render(request, 'jobs/jobs_update.html', {'job': job})

def job_delete_html(request, pk):
    job = get_object_or_404(JobPosting, pk=pk)
    if request.method == 'POST':
        job.delete()
        messages.success(request, "Job deleted.")
        return redirect('jobs:jobs_html')
    return render(request, 'jobs/jobs_delete.html', {'job': job})


# --- DASHBOARD FEATURES ---

def application_list(request):
    """View all applicants"""
    try:
        applications = JobApplication.objects.all().order_by('-applied_at')
    except:
        applications = []
    return render(request, 'jobs/application_list.html', {'applications': applications})

def pending_tasks(request):
    """Show jobs with pending applications"""
    try:
        pending_apps = JobApplication.objects.filter(status='Pending')
    except:
        pending_apps = []
    return render(request, 'jobs/pending_tasks.html', {'tasks': pending_apps})

def system_settings(request):
    """Simple settings page"""
    return render(request, 'jobs/settings.html')


# --- INTERVIEW LOGIC ---

def interview_list(request):
    try:
        interviews = Interview.objects.filter(status='Scheduled').order_by('date_time')
    except:
        interviews = []
    return render(request, 'jobs/interview_list.html', {'interviews': interviews})

def interview_create(request, application_id):
    application = get_object_or_404(JobApplication, id=application_id)
    
    if request.method == 'POST':
        Interview.objects.create(
            application=application,
            date_time=request.POST.get('date_time'),
            location=request.POST.get('location'),
            notes=request.POST.get('notes')
        )
        
        application.status = "Interview Scheduled"
        application.save()
        
        messages.success(request, f"Interview scheduled for {application.applicant.first_name}.")
        return redirect('jobs:interview_list')

    return render(request, 'jobs/interview_form.html', {'application': application})


# --- NEW: REVIEW APPLICATION VIEW ---
def review_application(request, pk):
    """
    Detailed view of an application.
    Allows Admin to Accept or Reject.
    """
    if not request.session.get('user_id'):
        return redirect('registration:login_view')

    application = get_object_or_404(JobApplication, pk=pk)

    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'accept':
            application.status = 'Accepted'
            messages.success(request, "Application Accepted.")
        elif action == 'reject':
            application.status = 'Rejected'
            messages.error(request, "Application Rejected.")
        
        application.save()
        return redirect('jobs:pending_tasks')

    return render(request, 'jobs/application_review.html', {'application': application})
=======
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password


from .models import JobPosting
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



# ---------- JOBS LIST ----------
def jobs_html(request):
    jobs = JobPosting.objects.all().order_by('id')
    return render(request, 'jobs/job_list.html', {
        'jobs': jobs,
    })

# ---------- CREATE JOB ----------
def job_create_html(request):
    if request.method == 'POST':
   
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        # the form uses name="position" for the position field
        job_position = request.POST.get('position', '').strip()
        slots_raw = request.POST.get('slots', '').strip()
        status = request.POST.get('status', '').strip()
        salary_raw = request.POST.get('salary', '').strip()


    
        # basic required-field validation
        if not title or not description or not job_position or not slots_raw:
            messages.error(request, "Title, description, position and slots are required.")
            return render(request, 'jobs/jobs_create.html', {
                'title': 'Add Job',
                'job': None,
                'form': {
                    'title': title,
                    'description': description,
                    'position': job_position,
                    'slots': slots_raw,
                    'status': status,
                    'salary': salary_raw,
                }
            })

      
        # convert slots to int and salary to Decimal, with proper error handling
        from decimal import Decimal, InvalidOperation
        try:
            slots = int(slots_raw)
        except (ValueError, TypeError):
            messages.error(request, "Slots must be a whole number.")
            return render(request, 'jobs/jobs_create.html', {
                'title': 'Add Job',
                'job': None,
                'form': {
                    'title': title,
                    'description': description,
                    'position': job_position,
                    'slots': slots_raw,
                    'status': status,
                    'salary': salary_raw,
                }
            })

        try:
            salary = Decimal(salary_raw)
        except (InvalidOperation, ValueError, TypeError):
            messages.error(request, "Salary must be a valid number (e.g. 50000.00).")
            return render(request, 'jobs/jobs_create.html', {
                'title': 'Add Job',
                'job': None,
                'form': {
                    'title': title,
                    'description': description,
                    'position': job_position,
                    'slots': slots_raw,
                    'status': status,
                    'salary': salary_raw,
                }
            })

        job = JobPosting(
            title=title,
            description=description,
            job_position=job_position,
            slots=slots,
            status=status,
            salary=salary,
        )

        job.save()

        messages.success(request, "Job created successfully.")
        return redirect('jobs:jobs_html')


    return render(request, 'jobs/jobs_create.html', {
        'title': 'Add Job',
        'job': None,
    })

# ---------- UPDATE JOB ----------
def job_update_html(request, pk):
    job = get_object_or_404(JobPosting, pk=pk)

    if request.method == 'POST':
     
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        job_position = request.POST.get('job_position', '').strip()
        slots = request.POST.get('slots', '').strip()
        status = request.POST.get('status', '').strip()
        salary = request.POST.get('salary', '').strip()


        if not title or not description or not job_position:
            messages.error(request, "Title, description and job_position are required.")
            return render(request, 'jobs/jobs_update.html', {
                'title': 'Edit Job',
                'job': job,
            })


        job.title = title
        job.description = description
        job.job_position = job_position
        job.slots = slots
        job.status = status
        job.salary = salary

        job.save()

        messages.success(request, "Job updated successfully.")
        return redirect('jobs:jobs_html')

    return render(request, 'jobs/jobs_update.html', {
        'title': 'Edit Job',
        'job': job,
    })

# ---------- DELETE JOB ----------
def job_delete_html(request, pk):
    job = get_object_or_404(JobPosting, pk=pk)

    if request.method == 'POST':
        job.delete()
        messages.success(request, "Job deleted successfully.")
        return redirect('jobs:jobs_html')

    return render(request, 'jobs/jobs_delete.html', {
        'job': job
    })


>>>>>>> 02cfd2272afaecbf5b9240bcb4de7a4c76483c42
