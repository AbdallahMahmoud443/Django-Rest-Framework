from django.db import models

# Create your models here.


class Departments(models.Model):
    DeprtName = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    
    def __str__(self):
        return self.DeprtName


class Countries(models.Model):
    CountryName = models.CharField(max_length=30)
    def __str__(self):
        return self.CountryName 

class Employee(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName  = models.CharField(max_length=30)
    TitleName = models.CharField(max_length=30)
    HasPassport = models.BooleanField()
    Salary = models.IntegerField()
    HireDate = models.DateField()
    Notes = models.CharField(max_length=200)
    Email = models.EmailField(default="",max_length=50)
    PhoneNumber = models.CharField(default="",max_length=20)
    Department = models.ForeignKey("Departments",default=0,on_delete=models.PROTECT,related_name="Employee_Department")
    Country= models.ForeignKey("Countries",default=0,on_delete=models.PROTECT,related_name="Employee_Country")
    