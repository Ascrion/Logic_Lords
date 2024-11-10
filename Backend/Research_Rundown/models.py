from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email

class UserFiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    name = models.CharField(max_length=100)  # Name of the PDF file uploaded by the user
    file_content = models.TextField()  # Field to store the extracted text content of the PDF
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"
