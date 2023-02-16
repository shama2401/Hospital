from rest_framework import serializers
from .models import Hospital, Okpo, Therapist, Chief_Physician, Nurse, Patients


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class OkpolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Okpo
        fields = '__all__'


class TherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = '__all__'


class Chief_PhysicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chief_Physician
        fields = '__all__'


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'


class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'


