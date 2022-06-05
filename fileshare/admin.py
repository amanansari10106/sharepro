from django.contrib import admin

# Register your models here.
from .models import FileUploadModel, TextReflectorModel

admin.site.register(FileUploadModel)
admin.site.register(TextReflectorModel)