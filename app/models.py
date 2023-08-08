from django.db import models

# Create your models here.
class School(models.Model):
    scname=models.CharField(max_length=100)
    scprincipal=models.CharField(max_length=100)
    sclocation=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.scname
    
class Student(models.Model):
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()
    scname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='panda')
    #related_name used for fetching details of child class without using child
    #  class object with the help of parent class

    def __str__(self) -> str:
        return self.sname
