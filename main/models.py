from django.db import models
from django.urls import reverse

class CustomBooleanField(models.BooleanField):

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return int(value) # return 0/1

class Hospital(models.Model):
    okpo = models.ForeignKey('Okpo', on_delete=models.CASCADE, verbose_name='ОКПО')
    employees = models.CharField(max_length=100, verbose_name='Сотрудники')
    public_private = CustomBooleanField(default=True, verbose_name='Государственная')
    class Meta:
        verbose_name = 'Больница'
        verbose_name_plural = 'Больницы'
        # ordering = ['-created']  # автосортировка
    def __str__(self):
        return f'{self.okpo}, {self.employees}, {self.public_private}'

class Okpo(models.Model):
    okpo = models.IntegerField(unique=True, db_index=True, verbose_name='ОКПО')

    def __str__(self):
        return f'{self.okpo}'

class Therapist(models.Model):
    okpo = models.ForeignKey('Hospital', on_delete=models.CASCADE, verbose_name='ОКПО')
    direction = models.DateTimeField(max_length=200, verbose_name='Направление')
    therapist_surgeon = CustomBooleanField(default=True, verbose_name='Терапевт')
    name = models.CharField(max_length=200, verbose_name='Ф.И.О.')
    pin_passport = models.CharField(max_length=14, verbose_name='ПИН-КОД паспорта')
    age = models.IntegerField(verbose_name='Возраст')
    work_experience = models.IntegerField(verbose_name='Стаж работы')
    phone_number = models.CharField(max_length=200, verbose_name='Номер телефона')
    nurse = models.OneToOneField('Nurse', verbose_name='Медсестра', on_delete=models.CASCADE,
        primary_key=True)
    patients = models.ManyToManyField('Patients', verbose_name='Пациенты')

    class Meta:
        verbose_name = 'Лечащий врач'
        verbose_name_plural = 'Лечащие врачи'
        # ordering = ['-created']  # автосортировка

    def __str__(self):
        return f'{self.okpo}, {self.direction}, {self.therapist_surgeon}, {self.name}, \
            {self.pin_passport}, {self.age}, {self.work_experience}, {self.phone_number}'

class Chief_Physician(models.Model):
    okpo = models.ForeignKey('Hospital', on_delete=models.CASCADE, verbose_name='ОКПО')
    name = models.CharField(max_length=200, verbose_name='Ф.И.О.')
    pin_passport = models.CharField(max_length=14, verbose_name='ПИН-КОД паспорта')
    age = models.IntegerField(verbose_name='Возраст')
    work_experience = models.IntegerField(verbose_name='Стаж работы')
    phone_number = models.CharField(max_length=200, verbose_name='Номер телефона')
    therapist = models.ManyToManyField('Therapist', verbose_name='Лечащий врач')

    class Meta:
        verbose_name = 'Главный врач'
        verbose_name_plural = 'Главные врачи'
        # ordering = ['-created']  # автосортировка

    def __str__(self):
        return f'{self.okpo}, {self.name}, \
            {self.pin_passport}, {self.age}, {self.work_experience}, {self.phone_number}'

class Nurse(models.Model):
    okpo = models.ForeignKey('Hospital', on_delete=models.CASCADE, verbose_name='ОКПО')
    name = models.CharField(max_length=200, verbose_name='Ф.И.О.')
    pin_passport = models.CharField(max_length=14, verbose_name='ПИН-КОД паспорта')
    age = models.IntegerField(verbose_name='Возраст')
    phone_number = models.CharField(max_length=200, verbose_name='Номер телефона')
    patients = models.ForeignKey('Patients', verbose_name='Пациенты', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Медсестра'
        verbose_name_plural = 'Медсестры'
        # ordering = ['-created']  # автосортировка

    def __str__(self):
        return f'{self.okpo}, {self.name}, \
            {self.pin_passport}, {self.age}, {self.phone_number}'

class Patients(models.Model):
    okpo = models.ForeignKey('Hospital', on_delete=models.CASCADE, verbose_name='ОКПО')
    name = models.CharField(max_length=200, verbose_name='Ф.И.О.')
    pin_passport = models.CharField(max_length=14, verbose_name='ПИН-КОД паспорта')
    age = models.IntegerField(verbose_name='Возраст')
    phone_number = models.CharField(max_length=200, verbose_name='Номер телефона')
    diagnosis = models.TextField(verbose_name='Причина обращения в больницу')
    complaint = models.CharField(max_length=1000, verbose_name='Жалоба', null=True)

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        # ordering = ['-created']  # автосортировка

    def __str__(self):
        return f'{self.okpo}, {self.name}, \
            {self.pin_passport}, {self.age}, {self.phone_number}, {self.diagnosis}, {self.complaint}'
