from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Course,Lesson,UserCourse,Profile,Contact


admin.site.register(CustomUser, UserAdmin)
admin.site.register(UserCourse)
admin.site.register(Profile)
admin.site.register(Contact)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'video_url')


# Register your models here.
