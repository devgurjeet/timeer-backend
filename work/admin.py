from django.contrib import admin
from django.db.models import Sum

from .models import Work, WorkItem

class WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'manager']

class WorkItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_workTitle', 'get_manager', 'allocatedHour','get_hoursSpent']
    #ordering = ['title']

    def get_workTitle(self, obj):
        return obj.work.title
    get_workTitle.short_description = 'Project'

    def get_manager(self, obj):
        return obj.work.manager.username
    get_manager.short_description = 'Manager'

    def get_hoursSpent(self, obj):
        return obj.timesheet_set.all().aggregate(Sum('hours'))["hours__sum"]
        # return 0
    get_hoursSpent.short_description = 'Time Spent'  


admin.site.register(Work, WorkAdmin)
admin.site.register(WorkItem, WorkItemAdmin)