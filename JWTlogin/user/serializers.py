from rest_framework import serializers
from .models import prac

class UserSearilizer(serializers.ModelSerializer):
    class Meta:
        model = prac
        fields = ['email','name','insta']