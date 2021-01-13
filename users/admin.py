from django.contrib import admin
from .models import User


@admin.register(User)
class RoomAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'address_line_1', 'city', 'zip_code', 'state')
