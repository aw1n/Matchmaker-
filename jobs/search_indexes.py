import datetime
from haystack import indexes
from .models import Job, Employer, Location 


class JobIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	author = indexes.CharField(model_attr='user')
	text = models.CharField(max_length=120, unique=True)
	pub_date = indexes.DateTimeField(model_attr='pub_date')

	def get_model(self):
		return Job

	def index_queryset(self, using=None):
    	"""Used when the entire index for model is updated."""
    	return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())