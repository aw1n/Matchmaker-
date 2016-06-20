from django import forms
from django.contrib.auth.models import User
from .models import JobPost, JobApp

from jobs.models import Job, Employer, Location

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['position', 'employer', 'location', 'description', 'start_date', 'pub_date']



class JobAppForm(forms.ModelForm):
	class Meta:
		model = JobApp
		fields = ['position', 'employer', 'location', 'uploadCV', 'start_date']