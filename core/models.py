from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return f'Review by {self.author.username} - Rating: {self.rating}'

class CustomUser(AbstractUser):
    aadhar = models.CharField(max_length=12)
    user_type = models.CharField(max_length=10) # sender or traveler
    rating = models.FloatField(default=0.0)
    reviews = models.ManyToManyField('Review', blank=True, related_name='reviewed_users')

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )

    def __str__(self):
        return self.username
    
class Parcel(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_parcels')
    traveling_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='travel_parcels')
    description = models.TextField()
    weight = models.FloatField()
    destination = models.CharField(max_length=255)
    deadline = models.DateField()
    status = models.CharField(max_length=10, default='pending')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    confirmed = models.BooleanField(default=False) # to track if sender has confirmed the traveling user

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def confirm_travler(self):
        self.confirmed = True
        self.save()

    def __str__(self):
        return self.description
    
class TravelDetails(models.Model):
    traveler = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    travel_date = models.DateField()

    def __str__(self):
        return f"{self.origin} to {self.destination} on {self.travel_date}"

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_date = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender} to {self.recipient} about Parcel {self.parcel}"

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return  self.message