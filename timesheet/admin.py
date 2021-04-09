from django.contrib import admin
from .models import Timesheet

class TimesheetAdmin(admin.ModelAdmin):
    list_display = ['get_workItem', 'hours', 'get_workTitle', 'workDate', 'remark']
    
    def get_workItem(self, obj):
        return obj.workItem.title
    get_workItem.short_description = 'Work Item'
    
    def get_workTitle(self, obj):
        return obj.workItem.work.title
    get_workTitle.short_description = 'Project'

    def get_manager(self, obj):
        return obj.workItem.work.manager.username
    get_manager.short_description = 'Manager'
     

admin.site.register(Timesheet, TimesheetAdmin)
