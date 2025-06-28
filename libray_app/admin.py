from django.contrib import admin
from .models import Author,Books,students

# Register your models here.
admin.site.register(Books)
admin.site.register(Author)
admin.site.register(students)
