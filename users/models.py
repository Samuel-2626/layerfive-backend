# python libraries
import uuid

# django apps
from django.db import models

# Create your models here.

class User(models.Model):

  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  phone_number = models.CharField(max_length=11)
  address_line_1 = models.CharField(max_length=255)
  address_line_2 = models.CharField(max_length=255, blank=True , null=True)
  city = models.CharField(max_length=255)
  zip_code = models.PositiveIntegerField()
  state = models.CharField(max_length=50)

  def __str__(self):
    return self.first_name
