from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField


class PendingDoctor(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    qualifications = models.CharField(max_length=255)
    experience_years = models.PositiveIntegerField(null=True, blank=True)
    about = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='doctors/', null=True, blank=True)
    location_text = models.CharField(max_length=200, blank=True)
    hospital_text = models.CharField(max_length=200, blank=True)
    specialties_text = models.CharField(max_length=500, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    admin_notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Pending Doctor'
        verbose_name_plural = 'Pending Doctors'

    def __str__(self):
        return f"{self.name} - {self.status}"


class PendingHospital(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=200)
    address = models.TextField(blank=True, null=True)
    contact_numbers = models.TextField(blank=True, null=True)
    facilities = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='records/images/', null=True, blank=True)
    location_text = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    admin_notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Pending Hospital'
        verbose_name_plural = 'Pending Hospitals'

    def __str__(self):
        return f"{self.name} - {self.status}"
