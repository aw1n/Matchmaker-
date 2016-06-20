from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import JobPostForm, JobAppForm
from .models import JobApp, JobPost


User = get_user_model()

def index(request):
    return render(request,'base.html',locals())

def jobpost(request):
    field_class = ['position', 'employer', 'location', 'description', 'start_date', 'pub_date']
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.organizer = request.user.username
            form.save()
            messages.add_message(request, messages.INFO, 'Job Post Created Successfully')
            return HttpResponseRedirect('/')
        else:
            print form.errors
    else:
        form = JobPostForm()
    for key in form.fields.keys():
        if key in field_class:
            field = form.fields[key]
            field.widget.attrs['class'] = 'form-control'
    return render(request, 'jobpost/job_post.html', locals())


def individual_post(request, slug):
    single_post = JobPost.objects.get(slug=slug)
    return render(request, 'jobpost/view_post.html', locals())

@login_required
def all_posts(request):
    posts = JobPost.objects.all()
    return render(request,'jobpost/posts.html',locals())






@login_required
def jobapp(request):
    title = "Job Application"
    jobapp, created = JobApp.objects.get_or_create(user=request.user)
    form = JobAppForm(request.POST or None, request.FILES or None, instance=jobapp)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect("profile_user")
    context = {
        "form": form,
        "title": title,
                }
    return render(request, "jobpost/apply_job.html", context)


@login_required
def jobpostview(request):
    user = get_object_or_404(User, username=request.user)
    jobpost, created = JobPost.objects.get_or_create(user=user)
    job, created = Job.objects.get_or_create(user=user)

    #jobs = user.userjob_set.all()
    context = {
       "jobpost": jobpost,
       "job" : job
        #"jobs": jobs,
                }
    return render(request, "jobpost/job_view.html", context)
