# models.py im Portfolio-App-Ordner
from django.db import models
from django.core.signing import TimestampSigner
from django.utils import timezone
from django.conf import settings  # Importiert für MEDIA_URL

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('coding', 'Coding Skills'),
        ('professional', 'Professional Skills'),
        ('soft', 'Soft Skills')
    ]
    
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)  # Kein default-Wert

    def __str__(self):
        return self.title
    
    def get_image_url(self):
        if self.image:
            return self.image.url
        return None  # Gibt None zurück, wenn kein Bild vorhanden ist

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='certificates/')
    issuing_organization = models.CharField(max_length=200)
    date_issued = models.DateField()
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Resume(models.Model):
    # Felder und Methoden für Resume hier definieren
    # Beispiel:
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
