from django.urls import path
from .views import *
from rest_framework import routers
from .views import HospitalViewSet, OkpoViewSet, Chief_PhysicianViewSet, TherapistViewSet, NurseViewSet, PatientsViewSet

routers = routers.SimpleRouter()

routers.register(r'hospital', HospitalViewSet)
routers.register(r'okpo', OkpoViewSet)
routers.register(r'chief', Chief_PhysicianViewSet)
routers.register(r'therapist', TherapistViewSet)
routers.register(r'nurse', NurseViewSet)
routers.register(r'pathients', PatientsViewSet)


urlpatterns = [
   path('', show_hospital, name='show_hospital'),
   path('bd/', bd, name='bd'),
   path('about/', about, name='about'),
   path('services/', services, name='services'),
   path('doctors/', doctors, name='doctors'),
   path('price/', price, name='price'),
   path('testimonials/', testimonials, name='testimonials'),
   path('contact/', contact, name='contact'),
   path('register/', register, name='register'),
   path('login/', user_login, name='login'),
   path('logout/', user_logout, name='logout'),
]

urlpatterns += routers.urls