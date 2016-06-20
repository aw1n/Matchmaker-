from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Job, Location, Employer 

import operator

from django.db.models import Q



User = get_user_model()


def search(request):
    q = request.GET.get("q")
    if q:
       # you may want to use `__istartswith' instead
       results = Job.objects.filter(text__icontains=q)
    else:
       # you may want to return Customer.objects.none() instead
       results = Job.objects.all()     

    context = dict(results=results, q=q)
    return render(request, "jobs/search_result.html", context)