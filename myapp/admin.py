from django.contrib import admin
from myapp.models import Dummy, UserProfile

# Register your models here.
admin.site.register(Dummy)
admin.site.register(UserProfile)