from django.db import models

# Create your models here.


class User_Registration(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
        ('O-', 'O-'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('bkash', 'Bkash'),
        ('nagad', 'Nagad'),
        ('rocket', 'Rocket'),
        ('card', 'Card'),
    ]
    GUEST_NUMBER_CHOICES=[
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
    ]
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15, blank=True)
    batch = models.CharField(max_length=10, blank=True)
    guests = models.PositiveIntegerField(default=0)
    total_amount = models.PositiveIntegerField(default=0)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, blank=True, null=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)
    

    def __str__(self):
        return self.fullname
    
class WebsiteRegistration(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    e_mail = models.EmailField()
    password = models.CharField(max_length=100)
    confirmpassword = models.CharField(max_length=100)

    def __str__(self):
        return self.username 
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    class Meta:
        verbose_name_plural = "Students"


class Group_Registration(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
        ('O-', 'O-'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('bkash', 'Bkash'),
        ('nagad', 'Nagad'),
        ('rocket', 'Rocket'),
        ('card', 'Card'),
    ]

    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, blank=True, null=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)

class GroupEventInfo(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    number_of_students = models.PositiveIntegerField()
    cost_per_person = models.DecimalField(max_digits=10, decimal_places=2)
    # total_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_cost = self.number_of_students * self.cost_per_person
        super().save(*args, **kwargs)

    def __str__(self):
        return self.fullname
    
class adminuser(models.Model):
   email = models.EmailField(unique=True)

class DeletedUserCount(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Deleted User Count: {self.count}"