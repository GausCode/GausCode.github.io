# serializers.py im Portfolio-App-Ordner
from rest_framework import serializers
from .models import Skill, ContactMessage, Project, Certificate, Resume
from django.contrib.auth.models import User

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'url', 'image_url']  # `id` hinzugefügt für eindeutige Identifizierung im Frontend

    def get_image_url(self, obj):
        # Falls ein Bild vorhanden ist, gib die URL zurück
        return obj.get_image_url()

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'

