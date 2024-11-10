from django import forms
from .models import UserFiles

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UserFiles
        fields = ['name']  # Only include fields that actually exist in the UserFiles model
