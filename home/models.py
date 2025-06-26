from django.db import models

# Create your models here.

class Userdata(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    password = models.TextField()
    image = models.ImageField(upload_to='userimages')

    def __str__(self):
        return self.username