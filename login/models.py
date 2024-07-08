from django.db import models

# Create your models here.
class Profile(models.Model):
    user_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    picture = models.URLField(default='/img')
    KarmaPoints = models.IntegerField(default=0)
    Account_Balance = models.IntegerField(default=0)
    user_type = models.CharField(max_length=100, default="User")
    Membership_license = models.CharField(max_length=100,default="None")
    Total_Donation = models.IntegerField(default=0)
    def __str__(self):
        return self.user_id
