from django.db import models

# Create your models here.

from django.urls import reverse
from django.utils.text import slugify
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
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.event_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('Eventpage', kwargs={'slug': self.slug})

    def __str__(self):
        return self.event_name

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    attendee_name = models.CharField(max_length=255, blank=True, null=True)  # Optional

    def __str__(self):
        return f"{self.event} - {self.ticket_type} - {self.price}"
