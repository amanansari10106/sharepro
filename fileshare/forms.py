# forms.py
from django import forms
from .models import FileUploadModel

class FileForm(forms.ModelForm):

	class Meta:
		model = FileUploadModel
		fields = ['name', 'file']
