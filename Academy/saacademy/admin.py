from django.contrib import admin
from .models import Contact, Course, Faculties, Enroll

# Register your models here.
admin.site.register(Contact)
admin.site.register(Course)
admin.site.register(Faculties)
admin.site.register(Enroll)
