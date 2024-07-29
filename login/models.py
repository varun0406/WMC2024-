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
    mobile = models.CharField(max_length=10,default="None")
    def __str__(self):
        return self.user_id
    
class KarmaPoints(models.Model):
    karma_points_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100)
    karma_points = models.IntegerField(default=0)
    karma_points_type = models.CharField(max_length=100)
    reference_id = models.CharField(max_length=100,default='No Reference')
    def __str__(self):
        return f"{self.user_id} : {self.karma_points} : {self.karma_points_type}"
    
class Transactions(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    payer_id = models.CharField(max_length=100)
    payee_id = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=100)
    transaction_amount = models.IntegerField(default=0)
    transaction_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.payer_id} : {self.payee_id} : {self.transaction_type} : {self.transaction_amount} : {self.transaction_date}"
    
    
class UserQuery(models.Model):
    query_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100)
    user_email= models.EmailField()
    query = models.TextField()
    query_date = models.DateTimeField(auto_now_add=True)
    query_status = models.CharField(max_length=100,default="Pending")
    def __str__(self):
        return f"{self.user_id} : {self.query} : {self.query_date} : {self.query_status}"
    
    
class Testimonial(models.Model):
        testimonial_id = models.AutoField(primary_key=True)
        username = models.CharField(max_length=100)
        Name= models.CharField(max_length=100)
        Occupation= models.CharField(max_length=100)
        Testimonial_topic=  models.CharField(max_length=100)
        testimonial = models.TextField()
        testimonial_date = models.DateTimeField(auto_now_add=True)
        def __str__(self):
            return f"{self.user_id} : {self.testimonial} : {self.testimonial_date}"