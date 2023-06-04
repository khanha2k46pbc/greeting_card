from django.contrib import admin
from .models import User, Upload_image, Stored_image
# Register your models here.
admin.site.register(User)
admin.site.register(Upload_image)
admin.site.register(Stored_image)