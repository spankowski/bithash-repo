from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.
class UserHash(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    second_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True)
    hash = models.CharField(max_length=256, blank=True)
    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs): 
        salt = self.second_name + str(self.date_of_birth)
        self.hash = make_password(self.first_name, salt)
        super(UserHash, self).save(*args, **kwargs)    