from rest_framework import serializers
from .models import Sport_Aquatics_Men, Sport_Aquatics_Women, Sport_Aquatics_Staff, Sport_Weightlifting, Staff, Sport_Athletics_Men, Sport_Athletics_Women, Sport_All_Common_Games_Men, Sport_All_Common_Games_Women

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

class Sport_Weightlifting_serializer(serializers.ModelSerializer):
    class Meta:
        model = Sport_Weightlifting
        fields = '__all__'

class Sport_Athletics_Men_serializer(serializers.ModelSerializer):
    class Meta:
        model = Sport_Athletics_Men
        fields = '__all__'

class Sport_Athletics_Women_serializer(serializers.ModelSerializer):
    class Meta:
        model = Sport_Athletics_Women
        fields = '__all__'

class Staff_serializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class Sport_All_Common_Games_Men_serializer(serializers.ModelSerializer):
    class Meta:
        model = Sport_All_Common_Games_Men
        fields = '__all__'

class Sport_All_Common_Games_Women_serializer(serializers.ModelSerializer):
    class Meta:
        model = Sport_All_Common_Games_Women
        fields = '__all__'
