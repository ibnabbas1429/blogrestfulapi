from django.db import models
from django.forms import CharField, DateField

# Create your models here.

class Blog(models.Model):
    Author = models.CharField(max_length=250)
    Title =models.CharField(max_length=150, blank=False, default="title")
    created_on = models.DateTimeField(auto_now_add=True)
    Body = models.TextField(blank=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created_on',)

