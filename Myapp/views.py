from django.shortcuts import render ,redirect
from django.http import HttpResponse
def dashboard(request):
    return render(request,'myapp/dashboard.html')

def teamleader(request):
    return render(request,'myapp/Admin.html')

def management(request):
    return render(request,'myapp/Management.html')

def approval(request):
    return render(request,'myapp/approval.html')

def portal(request):
    return render(request,'myapp/portal.html')

def profile(request):
    # Logic to fetch user profile data and render the profile template
    return render(request, 'myapp/profile.html')
  
from django.shortcuts import render
import requests

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user credentials against Frappe API
        if authenticate_frappe_user(username, password):
            # User exists in Frappe, determine user role
            role = determine_user_role(username)
            if role:
                return render(request, 'myapp/portal.html', {'role': role})
            else:
                return render(request, 'myapp/signin.html', {'error_message':'Invalid user role'})
        else:
            # User does not exist in Frappe or invalid credentials
            return render(request, 'myapp/signin.html', {'error_message':'Invalid username or password'})
    else:
        return render(request, 'myapp/signin.html')

def authenticate_frappe_user(username, password):
    # Make a request to the Frappe API to check if the user exists
    frappe_api_url = 'https://twilight.frappe.cloud/api/method/login'
    payload = {
        'usr': username,
        'pwd': password
    }
    response = requests.post(frappe_api_url, data=payload)

    # Check if the request was successful and the user exists
    if response.status_code == 200:
        data = response.json()
        if data.get('message') == 'Logged In':
            return True
    return False

def determine_user_role(username):
    # Use additional logic to determine the user's role based on their username
    # For demonstration purposes, let's assume all authenticated users have the 'employee' role
    return 'employee'
