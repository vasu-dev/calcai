from django.db import models
from .validators import validate_file_extension,validate_file_size

class Video(models.Model):
    name= models.CharField(unique=True,max_length=50)
    url = models.URLField(blank=True,max_length=250)
    file= models.FileField(validators=[validate_file_extension,validate_file_size])

    def __str__(self):
        return self.name + ": " + str(self.file)
