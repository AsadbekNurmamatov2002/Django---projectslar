from django.db import models

# Create your models here.


class Profil(models.Model):
    title=models.CharField(max_length=250)
    rasim=models.ImageField(default='')
    
    def __str__(self):
        return self.title
    
class Darsliklar(models.Model):
    raqam=models.CharField(max_length=60)
    mavzu=models.CharField(max_length=250, blank=True, null=True)
    dars=models.TextField()
    img=models.ImageField(default='', null=True, blank=True)
    def __str__(self) -> str:
        return self.mavzu
    

