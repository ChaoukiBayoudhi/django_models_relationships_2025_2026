from django.db import models
from django.db.models.fields import uuid

class Course(models.Model):
    #id is a primary key
    #uuid is a universal unique identifier
    #it is a 128-bit integer that is unique and can be used to identify a record
    #uuid is more secure than an auto-incrementing integer
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    
class Student(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    
class Profile(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=200)
    portfolio_url = models.URLField(max_length=200)

class Tutor(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    
class Enrollment(models.Model):
    pass