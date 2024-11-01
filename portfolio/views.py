# views.py im Portfolio-App-Ordner

from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Skill, Project, Certificate, ContactMessage
from .serializers import SkillSerializer, ProjectSerializer, CertificateSerializer, ContactMessageSerializer

def home(request):
    return render(request, 'home.html')

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all().order_by('-level')
    serializer_class = SkillSerializer
    permission_classes = [permissions.AllowAny]  # Erlaubt öffentlichen Zugriff

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [permissions.AllowAny]
