from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    #create relationship(don't inhrit from User!)
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    #Add any additional attribute you want
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)


    def __str__(self):
        #built in attribute of django.contrib.auth.models.User!
        return self.user.username