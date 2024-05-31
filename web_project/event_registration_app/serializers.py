from rest_framework import serializers
from .models import User_Registration,WebsiteRegistration,Student,GroupEventInfo,adminuser

class User_RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Registration
        fields = '__all__'

class WebsiteRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
       model = WebsiteRegistration
       fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
class GroupEventInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupEventInfo
        fields = '__all__'

class adminuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = adminuser
        fields = '__all__'
