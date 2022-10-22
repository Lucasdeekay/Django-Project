from django.db import models


class Profile(models.Model):
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    image = models.ImageField()

    def __str__(self):
        return self.username

