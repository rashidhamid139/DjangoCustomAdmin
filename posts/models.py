from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length =100)
    cover = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title



class City(models.Model):
    name = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title