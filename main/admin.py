from django.contrib import admin

# Register your models here.
from .models import Member, Facilitators, Course, Department, Assignment, Announcement,Material,Submission

admin.site.register(Member)
admin.site.register(Facilitators)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Assignment)
admin.site.register(Announcement)
admin.site.register(Material)
admin.site.register(Submission)
