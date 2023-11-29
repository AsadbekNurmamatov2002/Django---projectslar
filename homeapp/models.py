from django.db import models
from datetime import datetime 
# Create your models here.

class DarsProject(models.Model):
    nichanchi=models.CharField(max_length=200)
    title=models.CharField(max_length=250)
    rasim=models.ImageField(default='')
    vaqt = models.DateTimeField(default=datetime.now(), blank=True)
    body=models.TextField()
    def __str__(self):
        return self.nichanchi
    
class ProjectsModel(models.Model):
    logo=models.CharField(max_length=40)
    toptitle=models.CharField(max_length=250)
    urtatitle=models.CharField(max_length=250)
    bottomtitle=models.CharField(max_length=250)
    span=models.CharField(max_length=250)
    def __str__(self):
        return self.logo
    
class ProjectUrta(models.Model):
    title1=models.CharField(max_length=250)
    title2=models.CharField(max_length=250)
    text=models.TextField()
    yunalish=models.CharField(max_length=25)
    rasim=models.ImageField(default='')
    def __str__(self) -> str:
        return self.title1

    
    

