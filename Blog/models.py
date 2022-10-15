from django.utils import timezone
from email.policy import default
from django.db import models

# Create your models here.
class BlogModel(models.Model):
    author = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.author} => {self.title}"
