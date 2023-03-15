from django.contrib import admin

from account.models import User, Class, School
# Register your models here.

admin.site.register(User)
admin.site.register(Class)
admin.site.register(School)
