from django.db import models
from django.contrib.auth.models import User

class Work(models.Model):
    title =  models.CharField(max_length=30)
    description = models.TextField()
    manager =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class WorkItem(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    resources = models.ManyToManyField(User, related_name="resouce")
    allocatedHour = models.DecimalField(max_digits = 6, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return self.title