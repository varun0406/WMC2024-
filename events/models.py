from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

from django.urls import reverse
from django.utils.text import slugify
from login.models import Profile
class Organization(models.Model):
    org_name = models.CharField(max_length=255)
    org_contact = models.CharField(max_length=255, blank=True, null=True)
    org_email = models.EmailField(max_length=255, blank=True, null=True)
    org_desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.org_name


class Venue(models.Model):
    venue_name = models.CharField(max_length=255)
    venue_address = models.TextField(blank=True, null=True)
    venue_contact = models.CharField(max_length=255, blank=True, null=True)
    venue_capacity = models.IntegerField()
    image=models.ImageField(upload_to='media/',blank=True,null=True)

    def __str__(self):
        return self.venue_name


class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_desc = models.TextField(blank=True, null=True)
    event_s_time = models.DateTimeField()
    event_e_time = models.DateTimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    Image1=models.ImageField(upload_to='media/',blank=True,null=True)
    Image2=models.ImageField(upload_to='media/',blank=True,null=True)
    Image3=models.ImageField(upload_to='media/',blank=True,null=True)
    Image4=models.ImageField(upload_to='media/',blank=True,null=True)
    Event_Tickets=models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.event_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('Eventpage', kwargs={'slug': self.slug})

    def __str__(self):
        return self.event_name

from django.utils.text import slugify
import uuid

from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import uuid

from django.db import models
import uuid

class Ticket(models.Model):
   
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    tickets = models.SmallIntegerField()
    total_paid_price = models.DecimalField(max_digits=10, decimal_places=2)
    attendee_name = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    email = models.EmailField(default=None)
    discount = models.IntegerField()

    def __str__(self):
        return f"{self.event} - {self.attendee_name} - ${self.total_paid_price}"

# quiz/models.py

class Question(models.Model):
    text = models.CharField(max_length=255)
    Option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    CORRECT_OPTION_CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('option4', 'Option 4')
    ]
    correct_option = models.CharField(
        max_length=7,
        choices=CORRECT_OPTION_CHOICES,
        default='option1'
    )

    def __str__(self):
        return self.text

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title

