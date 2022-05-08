from rest_framework import serializers
from controlapp.models import Switches

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Switches
        fields = '__all__'

