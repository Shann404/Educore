from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Course,Lesson,UserCourse,Profile


admin.site.register(CustomUser, UserAdmin)
admin.site.register(UserCourse)
admin.site.register(Profile)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'video_url')


# Register your models here.
