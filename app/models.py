from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=20)


class Employee(models.Model):
    fullname = models.CharField(max_length=30)
    birth_date = models.DateField()
    position = models.ForeignKey(Position, on_delete = models.CASCADE)
    wage = models.IntegerField()




