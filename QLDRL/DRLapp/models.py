from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

# Create your models here.


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=False)
    updated_date = models.DateTimeField(auto_now_add=True, null=False)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Falcuty(BaseModel):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Class(BaseModel):
    name = models.CharField(max_length=50, null=False)
    falcuty = models.ForeignKey(Falcuty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(AbstractUser):
    # ROLE_CHOICES = (
    #     ('ctsv', 'Chuyên viên CTSV'),
    #     ('assist', 'Trợ lý sinh viên'),
    #     ('student', 'Sinh viên'),
    # )
    # role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    avatar = CloudinaryField(null=True)
    uclass = models.ForeignKey(Class, related_name='uclass', null=True, on_delete=models.CASCADE)


class Regulation(BaseModel):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Activity(BaseModel):
    name = models.CharField(max_length=50, null=False)
    description = RichTextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField(null=True)
    registered_students = models.ManyToManyField(User, related_name='registered_activities', blank=True)
    point = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Point(models.Model):
    point = models.IntegerField()
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=False)
    activity = models.ForeignKey(Activity, related_name='activity', on_delete=models.CASCADE, null=True)
    regulation = models.ForeignKey(Regulation, related_name='regulation', on_delete=models.CASCADE, null=True)
    confirm = CloudinaryField(null=True)

    def __str__(self):
        return self.point












