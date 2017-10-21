from django.db import models
from json import dumps

# Create your models here.
class User(models.Model):

  ROLE = (
    ('L','parking_owner'),
    ('C','car_owner'),
    ('B','Both'),
  )

  phone = models.CharField(max_length=20)
  name = models.CharField(max_length=20)
  gender = models.BooleanField()
  role = models.CharField(max_length=1, choices=ROLE)
  can_share = models.BooleanField(default=False)
  plate = models.CharField(max_length=20)
  parking_position = models.CharField(max_length=20)
  setting = models.CharField(max_length=200)

  def __repr__(self):
    return dumps({"name": self.name, "role": self.role})

class Order(models.Model):
  parking_owner = models.ForeignKey('User', related_name='parking_owner') 
  car_owner = models.ForeignKey('User', related_name='car_owner') 
  start_position = models.CharField(max_length=20) 
  target_position = models.CharField(max_length=20) 
  charge = models.CharField(max_length=20) 
  finished = models.BooleanField(default=False) 