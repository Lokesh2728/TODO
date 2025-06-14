from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=100,null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.title