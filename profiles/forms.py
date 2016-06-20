
from django import forms



from .models import UserJob, Profile


class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=50)
	file = forms.FileField()


class UserJobForm(forms.ModelForm):
	class Meta:
		model = UserJob
		fields = [
			#"user",
			"position",
			"location",
			"employer_name",
			
			]


class ProfileForm(forms.ModelForm):
	class Meta:
		file = forms.FileField()
		model = Profile
		fields = [
			#"user",
			"location",
			"picture",
			"Description",
			"CV",
			"skills",
			"project",
			"projecturl",
			]