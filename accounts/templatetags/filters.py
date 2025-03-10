from django import template

register = template.Library()

@register.filter
def get_dynamic_value(dynamic_data, field_label):
    """Retrieve the dynamic field value safely from the employee's JSON data."""
    return dynamic_data.get(field_label, '')

@register.filter
def get_filter_value(request_get, field_label):
    """Retrieve the dynamic filter value from the request GET parameters."""
    return request_get.get(f'filter_{field_label}', '')
    