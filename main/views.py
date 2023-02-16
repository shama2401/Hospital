from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages                         #  Для распознования
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, UserLoginForm
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from rest_framework import viewsets
from .serializers import *

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()

class OkpoViewSet(viewsets.ModelViewSet):
    queryset = Okpo.objects.all()
    serializer_class = OkpolSerializer


class TherapistViewSet(viewsets.ModelViewSet):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer


class Chief_PhysicianViewSet(viewsets.ModelViewSet):
    queryset = Chief_Physician.objects.all()
    serializer_class = Chief_PhysicianSerializer

class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer

class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'login user')
            return redirect('/')
        else:
            messages.error(request, 'Error login')
    else:
        form = UserLoginForm()
    return render(request, 'register/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Register Success')
            return redirect('/')
        else:
            messages.error(request, 'Register Error')
    else:
        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form':form})


def show_hospital(request):
    hospital = Hospital.objects.all()
    c_physician = Chief_Physician.objects.all()
    therapist = Therapist.objects.all()
    nurse = Nurse.objects.all()
    patients = Patients.objects.all()
    return render(request, 'main/show_hospital.html', {'hospital':hospital,'c_physician':c_physician,'therapist':therapist, 'nurse':nurse, 'patients':patients})


def bd(request):
    return render(request, 'main/bd.html')


def about(request):
    return render(request, 'main/about.html')


def services(request):
    return render(request, 'main/services.html')


def doctors(request):
    return render(request, 'main/doctors.html')


def price(request):
    return render(request, 'main/price.html')


def testimonials(request):
    return render(request, 'main/testimonials.html')


def contact(request):
    return render(request, 'main/contact.html')
