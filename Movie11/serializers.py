from rest_framework import serializers
from .models import *

class AudienceSerializer(serializers.ModelSerializer):
    class  Meta:
       model = Audience
       fields = '__all__'