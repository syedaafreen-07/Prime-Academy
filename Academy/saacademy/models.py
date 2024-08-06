from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    sub = models.CharField(max_length=10)
    msg = models.TextField()


    def __str__(self):
        return self.name
    

class Course(models.Model):
    sno = models.IntegerField(default=1)
    name = models.CharField(max_length=255)           
    description = models.TextField()                   
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    image = models.ImageField(upload_to='course/')     
    category = models.CharField(max_length=255)       
    rating = models.IntegerField()                      
    def __str__(self):
        return self.name


class Faculties(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='course/')
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Enroll(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    price = models.BigIntegerField()

    def __str__(self):
        return self.name