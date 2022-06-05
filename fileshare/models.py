
from django.db import models
import os
from sharepro import settings
from django.contrib.auth.models import User

# Create your models here.
class FileUploadModel(models.Model):
    f_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='files/')

    def delete(self, *args, **kwargs):
        fpath = str(settings.BASE_DIR) + "/" + "filesdir" + "/" + str(self.file)
        if os.path.exists(fpath):
            os.remove(fpath)
        super().delete(*args, **kwargs)

class TextReflectorModel(models.Model):
    tr_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, unique=True)
    text = models.TextField(default="Enter text here")
    
