from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import UserRegisterForm

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()

            login(request, user)  # Auto-login after registration

            # Redirect to the login page
            return redirect('login')  # Assuming 'login' is the name of your login view
    else:
        form = UserRegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})





from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect('home')  # Redirect to home page after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})




def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')


from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Change Password View
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # After password is changed, update session so the user remains logged in
            update_session_auth_hash(request, form.user)
            return redirect('login')  # Redirect to login page after successful password change
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, 'accounts/change_password.html', {'form': form})




@login_required
def home(request):
    return render(request, 'home.html')



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FormField
from .forms import DynamicForm

@login_required
def form_builder(request):
    if request.method == "POST":
        label = request.POST.get("label")
        field_type = request.POST.get("field_type")

        if label and field_type:
            FormField.objects.create(user=request.user, label=label, field_type=field_type)
            return redirect("form_builder")

    fields = FormField.objects.filter(user=request.user)  # Fetch user-specific fields
    form = DynamicForm()
    return render(request, "accounts/form_builder.html", {"fields": fields, "form": form})

# employee_management/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    # Render the profile page, passing in the username of the logged-in user
    return render(request, 'profile.html', {'username': request.user.username})



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import FormField

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import FormField

@csrf_exempt
def save_field_order(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            for field_data in data.get("order", []):
                field_id = field_data.get("id")
                position = field_data.get("position")
                
                # Update field position in the database
                FormField.objects.filter(id=field_id).update(position=position)

            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    return JsonResponse({"status": "invalid request"}, status=400)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import FormField

@csrf_exempt
def save_form(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("Received form data:", data)  # Debugging
            return JsonResponse({"message": "Form saved successfully", "data": data})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)

@login_required
def profile_setup(request):
    if request.method == "POST":
        # Handle the form submission and create an Employee object
        # For simplicity, assume you're creating the Employee object directly from the form data
        full_name = request.POST.get("full_name")
        date_of_birth = request.POST.get("date_of_birth")
        gender = request.POST.get("gender")
        marital_status = request.POST.get("marital_status")
        address = request.POST.get("address")
        phone_number = request.POST.get("phone_number")
        job_title = request.POST.get("job_title")
        department = request.POST.get("department")

        # Create the Employee object
        Employee.objects.create(
            user=request.user,
            full_name=full_name,
            date_of_birth=date_of_birth,
            gender=gender,
            marital_status=marital_status,
            address=address,
            phone_number=phone_number,
            job_title=job_title,
            department=department,
        )

        messages.success(request, "Profile setup completed successfully.")
        return redirect('profile')  # Redirect to the profile page after setting it up

    return render(request, 'accounts/profile_setup.html')

from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Employee  # Import the Employee model

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Employee, DynamicField

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Employee  # Import Employee model
from .forms import EmployeeForm  # Import EmployeeForm

@login_required
def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)  
            employee.user = request.user  # Associate employee with logged-in user
            employee.save()
            
            # Handle AJAX request (JSON response)
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({"success": True, "redirect_url": "/accounts/employee_list/"})
            
            messages.success(request, "Employee added successfully!")
            return redirect("employee_list")  # Redirect to employee list page
        
        else:
            # Handle form errors (for AJAX requests)
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({"success": False, "errors": form.errors})
            
            messages.error(request, "Please correct the errors below.")

    else:
        form = EmployeeForm()

    return render(request, "accounts/create_employee.html", {"form": form})



from django.shortcuts import render
from django.db.models import Q
from .models import Employee, DynamicField

def employee_list(request):
    search_query = request.GET.get('search', '')
    employees = Employee.objects.all()
    dynamic_fields = DynamicField.objects.all()

    # Apply search filters
    if search_query:
        employees = employees.filter(
            Q(full_name__icontains=search_query) |
            Q(job_title__icontains=search_query) |
            Q(department__icontains=search_query) |
            Q(phone_number__icontains=search_query)
        )

    # Apply dynamic field filters
    filter_conditions = Q()
    for field in dynamic_fields:
        filter_value = request.GET.get(f'filter_{field.label}', '').strip()
        if filter_value:
            filter_conditions &= Q(dynamic_data__icontains={field.label: filter_value})

    employees = employees.filter(filter_conditions)

    return render(request, 'accounts/employee_list.html', {
        'employees': employees,
        'search_query': search_query,
        'dynamic_fields': dynamic_fields
    })

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Employee

@login_required
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == "POST":
        employee.delete()
        messages.success(request, "Employee deleted successfully!")
        return redirect("employee_list")  # Update with your actual employee list view name

    return redirect("employee_list")  # Redirect back if not a POST request

