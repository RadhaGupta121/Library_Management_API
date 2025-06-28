from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    # id, name, country
    country_name=[('India','IN'),('America','USA')]
    name=models.CharField(max_length=200)
    country=models.CharField(choices=country_name, max_length=20)
    
    def __str__(self):
        return f'{self.name} {self.country}'
class Books(models.Model):
    # id, title, author_id, is_borrowed, price, added_date)
    title=models.CharField(max_length=200)
    author_id=models.ForeignKey(Author,on_delete=models.CASCADE)
    is_borrowed=models.BooleanField(default=False)
    price=models.PositiveBigIntegerField(default=200)
    added_date=models.DateTimeField(auto_now_add=True)
    is_available=models.BooleanField(default=True)
    quantity=models.PositiveIntegerField(default=10)

    def __str__(self):
        return f'{self.title}'


class students(models.Model):
    dept=[('CS','ComputerScience'),('ME','MechanicalEng'),('EE','Electrical Eng')]
    name=models.CharField(max_length=300,null=False)
    department=models.TextField(choices=dept)
    student_id=models.BigIntegerField(unique=True,null=False)

    def __str__(self):
        return f"{self.name}"

class Audit(models.Model):
    student=models.ForeignKey(students,on_delete=models.CASCADE)
    books_borrowed=models.ForeignKey(Books,on_delete=models.CASCADE,default=False)
    borrowed_date=models.DateTimeField(default=timezone.now)
    return_date=models.DateTimeField(null=True,blank=True)
    is_returned=models.BooleanField(default=False)
    penality=models.BooleanField(default=False)
    overdue_amount=models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.student.name} {self.books_borrowed.title}"

