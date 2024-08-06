from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User 
from django.contrib import messages
from .models import Contact, Course, Faculties, Enroll
from django.contrib.auth  import authenticate,  login, logout

def loginPage(request):
    return render(request,"login.html")

def home(request):
    return render(request,"home.html")

def handleRegister(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        if not (username and email and password and fname and lname):
            messages.error(request, 'All fields are required.')
            return redirect('login') 
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname 
            user.last_name = lname  
            user.save()
            messages.success(request, 'Registration successful.')
            return redirect('home')  
        except Exception as e:
            messages.error(request, 'Username already exists. Please choose a different one.')
            return redirect('log')
        
def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST.get('loginusername')  
        loginpassword = request.POST.get('loginpassword')  
        if loginusername and loginpassword:
            user = authenticate(request,username=loginusername, password=loginpassword)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged In")
                return redirect("home")
            else:
                messages.error(request, "Invalid credentials! Please try again")
                return redirect("log")
        else:
                messages.error(request, "Please provide both username and password.")

        return redirect("log")

    return HttpResponse("404 - Not found")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        sub = request.POST.get('sub', '')
        msg = request.POST.get('msg', '')

        if not name or not email or not sub or not msg:
            messages.error(request, "All fields are required.")
            return render(request, 'contact.html')

        contact = Contact(name=name, email=email, sub=sub, msg=msg)
        contact.save()
        messages.success(request, "Your Query will be replied with in 24 hours")
    return render(request, 'contact.html')

def courses(request):
    all_courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': all_courses})

def about(request):
    faculties = Faculties.objects.all()
    return render(request, 'about.html', {'faculties': faculties})


def blog(request):
    return render(request,"blog.html") 

def enroll(request,sno):
    course = Course.objects.get(id=sno)
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        price = course.price

        if not name or not email or not price:
            messages.error(request, "All fields are required.")
            return render(request,'courseview.html',{'course':course})

        enroll = Enroll(name=name, email=email, price=price)
        enroll.save()
        messages.success(request, "Your class will begin within 2days")
    return render(request,'courseview.html',{'course':course})