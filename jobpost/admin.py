from django.contrib import admin

# Register your models here.
from .models import JobPost 
from .models import JobApp 


admin.site.register(JobPost)
admin.site.register(JobApp)
