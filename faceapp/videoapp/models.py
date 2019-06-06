from django.db import models
from .validators import validate_file_extension,validate_file_size

class Video(models.Model):
    name= models.CharField(max_length=500)
    url = models.URLField(blank=True,max_length=250)
    videofile= models.FileField(validators=[validate_file_extension,validate_file_size])

    def __str__(self):
        return self.name + ": " + str(self.videofile)
