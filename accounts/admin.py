from django.contrib import admin
from .models import Employee, FormField, FormResponse

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'department', 'display_dynamic_data')  # Add custom method for dynamic_data
    search_fields = ('full_name', 'job_title', 'department')  # Optional: Add search functionality
    list_filter = ('department',)  # Optional: Add filter options for easier navigation

    def display_dynamic_data(self, obj):
        # Return the dynamic_data as a string (or a truncated version of it)
        return str(obj.dynamic_data)[:50]  # You can adjust the slicing or formatting as needed
    display_dynamic_data.short_description = 'Dynamic Data'  # Custom column header for dynamic_data
        

# Registering other models
admin.site.register(FormField)
admin.site.register(FormResponse)
