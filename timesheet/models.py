from django.db import models
from django.contrib.auth.models import User

from work.models import WorkItem

class Timesheet(models.Model):
    hours = models.DecimalField(max_digits = 5, decimal_places=2)
    workItem = models.ForeignKey(WorkItem, on_delete=models.CASCADE)
    workDate = models.DateField()
    remark = models.TextField(blank=True, null=True)
    loggedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")    


    def __str__(self):
        return f"{self.workItem.title} | {self.hours} hrs"
