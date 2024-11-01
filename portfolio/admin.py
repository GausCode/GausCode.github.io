from django.contrib import admin
from .models import Skill, ContactMessage, Project, Certificate, Resume  # Fügt Resume hinzu

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    search_fields = ('title', 'description')

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuing_organization', 'date_issued')
    search_fields = ('title', 'issuing_organization')
    list_filter = ('date_issued',)


