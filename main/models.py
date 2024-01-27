from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=25)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Teacher(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=25)

    def __str__(self):
        return self.first_name

