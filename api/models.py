from django.db import models

class Student(models.Model):
    GENDER=(
        ('f','female'),
        ('m','male'),
        ('u','undisclosed')
    )
    name=models.CharField(max_length=100)
    roll_number=models.IntegerField(unique=True)
    email=models.EmailField()
    gender=models.CharField(max_length=1, choices=GENDER)
    percentage=models.FloatField()
    institute=models.ForeignKey("Institute", on_delete=models.CASCADE, null=True, blank= True)
    def __str__(self):
        return self.name
    


class Institute(models.Model):
    TYPE=(
        ('s','school'),
        ('c','college')
    )
    name=models.CharField(max_length=100)
    type_of_institute=models.CharField(max_length=50,choices=TYPE)
    def __str__(self):
        return self.name
    