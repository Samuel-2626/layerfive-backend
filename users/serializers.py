from rest_framework import serializers
from  .models import User


class UserSerializer(serializers.ModelSerializer):

  class Meta:
    
    model = User
    fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'address_line_1', 'address_line_2', 'city', 'zip_code', 'state',)