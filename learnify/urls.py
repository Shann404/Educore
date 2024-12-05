from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin



urlpatterns = [

    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('coursedetails/', views.coursedetails, name='courses'),
    path('courses/', views.courses, name='dashboard'),
    path('events/', views.events, name='events'),
    path('pricing/', views.pricing, name='pricing'),
    path('starterpage/', views.starterpage, name='starterpage'),
    path('trainers/', views.trainers, name='trainers'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('courses/<int:course_id>/', views.course_page, name='course_page'),
    path('admin/', admin.site.urls),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),  # New route for editing
    path('dashboard/profile/', views.profile_view, name='profile'),
    path('feedback/', views.feedback, name='feedback'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



