from django.db import models

class student(models.Model):
    First_name=models.CharField(max_length=35)
    Last_name=models.CharField(max_length=35)
    father_name=models.CharField(max_length=35)
    roll_number=models.IntegerField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    grade=models.IntegerField(null=True,blank=True)
    # passing_year=models.CharField(max_length=30)

    def __str__(self): 
       return f"{self.First_name}"
