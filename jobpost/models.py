from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from jobs.models import Job, Employer, Location



User = settings.AUTH_USER_MODEL





def upload_location(instance, filename):
    #extension = filename.split(".")[1]
    location = str(instance.user.username)
    return "%s/%s" %(location, filename)




class JobPost(models.Model):
    #user = models.OneToOneField(User)
    
    position = models.CharField(max_length=200)
    employer = models.CharField(max_length=120)
    slug = models.SlugField()
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now=True)
    pub_date=models.DateTimeField('published', default='')
    start_date = models.DateTimeField(null=True, blank=True)
  


    def __unicode__(self): #__str__(self):
        return self.position

    
    def save(self, *args,**kwargs):
        self.slug = slugify(self.position)
        super(JobPost,self).save(*args,**kwargs)


class JobApp(models.Model):
    user = models.OneToOneField(User)
    position = models.CharField (max_length=200)
    employer = models.CharField(max_length=120)
    slug = models.SlugField()
    location = models.CharField(max_length=100)
    uploadCV = models.FileField(upload_to=upload_location, null= False, blank=False)
    timestamp = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(null=True, blank=True)
  
    
  
    def __unicode__(self): #__str__(self):
        return self.user.username


    def get_absolute_url(self):
        #url = reverse("question_single", kwargs={"id": self.id})
        url = reverse("profile", kwargs={"username": self.user.username})
        return url

    def like_link(self):
        url = reverse("like_user", kwargs={"id": self.user.id})
        return url
