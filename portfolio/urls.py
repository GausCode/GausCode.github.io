# /portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('skills/', views.SkillViewSet.as_view({'get': 'list'}), name='skill-list'),
    path('contact/', views.ContactMessageViewSet.as_view({'get': 'list', 'post': 'create'}), name='contact-list'),
    path('projects/', views.ProjectViewSet.as_view({'get': 'list'}), name='project-list'),
    path('certificates/', views.CertificateViewSet.as_view({'get': 'list'}), name='certificate-list'),
]
