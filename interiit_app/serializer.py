from rest_framework import serializers
from .models import Sport_Aquatics_Men, Sport_Aquatics_Women, Sport_Aquatics_Staff

class Sport_Aquatics_Men_serializer(serializers.ModelSerializer):
    class Meta:
        model = Sport_Aquatics_Men
        fields = '__all__'

class Sport_Aquatics_Women_serializer(serializers.ModelSerializer):
    class Meta:
        model = Sport_Aquatics_Women
        fields = '__all__'

class Sport_Aquatics_Staff_serializer(serializers.ModelSerializer):
    class Meta:
        model = Sport_Aquatics_Staff
        fields = '__all__'
