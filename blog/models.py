from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField( max_length=50)
    img = models.ImageField(upload_to='./media/img/', null=True, blank=True)
    video = models.FileField(upload_to='./media/video/',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])], blank=True)
    desc = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    username = models.CharField(max_length=50,default ="")

