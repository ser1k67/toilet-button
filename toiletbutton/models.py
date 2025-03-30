from django.db import models

# Create your models here.
class Toiletbutton(models.Model):
    name = models.CharField(max_length=40)
    sound_name = models.CharField(max_length=40)
    image = models.ImageField(upload_to="sound_images")
    sound = models.FileField(upload_to="sound_files")
