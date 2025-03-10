from django.contrib import admin
from .models import Employee, FormField, FormResponse

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'department', 'display_dynamic_data') 
    search_fields = ('full_name', 'job_title', 'department')  
    list_filter = ('department',)  

    def display_dynamic_data(self, obj):
        return str(obj.dynamic_data)[:50]  
    display_dynamic_data.short_description = 'Dynamic Data'  
        

admin.site.register(FormField)
admin.site.register(FormResponse)
