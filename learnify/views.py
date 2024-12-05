from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomLoginForm
from django.contrib.auth.decorators import login_required
from learnify.models import CustomUser, Contact
from django.contrib.auth import get_user_model
from .forms import RegisterForm
from .models import Course,Lesson,UserCourse
from django.http import JsonResponse
from .models import Profile
from .forms import ProfileForm





User = get_user_model()

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if profile.is_completed:
        # Render the profile in read-only mode
        return render(request, 'profile_read_only.html', {'profile': profile})

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.is_completed = True  # Mark the profile as completed
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form, 'profile': profile})

@login_required
def profile_edit_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    # Handle form submission for editing
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('profile')  # Redirect to the read-only profile after editing
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form, 'profile': profile})  # Reuse the existing template
@login_required
def user_dashboard(request):
    user_courses = UserCourse.objects.filter(user=request.user)  # Fetch user's courses
    context = {
        'user_courses': user_courses,
    }
    return render(request, 'dashboard.html', context)




def course_page(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = Lesson.objects.filter(course_id=course_id)
    return render(request, 'course-details.html', {'course': course, 'lessons': lessons})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

 
 

def login_view(request):
    if request.method == 'POST':
        form=CustomLoginForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect('/dashboard/') # Redirect to the home page after successful login
    else:
        form=CustomLoginForm()
    
    return render(request, 'login.html', {'form': form})

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact=Contact(name=name,
                        email=email,
                        subject=subject,
                        message=message
                        )

        contact.save()

        return redirect('/contact/')

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
def courses(request):
    course = Course.objects.all()
    return render(request, 'course.html' ,{'course': course})
def coursedetails(request):
    return render(request, 'course-details.html')
def events(request):
    return render(request, 'events.html')
def pricing(request):
    return render(request, 'pricing.html')
def starterpage(request):
    return render(request, 'starter-page.html')
def trainers(request):
    return render(request, 'trainers.html')


