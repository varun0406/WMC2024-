from django.db import models
from django.utils.text import slugify
# Create your models here.
from django.urls import reverse

   
    
    
class Statistics(models.Model):
    Donaters_UserID=models.CharField(max_length=100,default="unknown")
    Name=models.CharField(max_length=100,default="unknown")
    value = models.PositiveSmallIntegerField()
    ranking = models.PositiveSmallIntegerField()
    slug = models.SlugField(blank=True)
    def get_absolute_url(self):
        return reverse("Donation_STATS:Donaters_Dashboard", kwargs={"slug": self.slug})
    @property
    def data(self):
        return f"{self.Donaters_UserID : {self.value}}"
  
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Donaters_UserID)
        super().save(*args, **kwargs)
    
    
    
    def __str__(self):
        return f"{self.Donaters_UserID} : {self.value}"






class Donation(models.Model):
    donation_id = models.AutoField(primary_key=True)
    Donaters_UserID = models.ForeignKey(Statistics,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    donation_amount = models.IntegerField(default=0) 
    donation_date = models.DateTimeField(auto_now_add=True)
    donation_category = models.CharField(max_length=100)
    donation_description = models.CharField(max_length=100)
   
   
    def  __str__(self):
        return f"{self.user_name} : {self.donation_amount} : {self.donation_date} : {self.donation_category} : {self.donation_description}"
       