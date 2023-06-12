from rest_framework import serializers
from firstapiapp.models import UserProfile
from django.contrib.auth.models import User
import re 

class registerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
    def create(self, validated_data):
        user =User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    def validate(self,validated_data):
        if validated_data.get('password'):
            userPassword=validated_data['password']
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if  regex.search(userPassword)==None:
                raise serializers.ValidationError('Give special characters for strong password')
            if len(userPassword) < 8:
                raise serializers.ValidationError('Password cannot be less than 8 digits')
        return validated_data     

        


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=UserProfile
        fields=  ['Name','Email']
       
    def validate(self,validated_data):
        if validated_data.get('Name'):
            name=validated_data['Name']
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if not regex.search(name)==None:
            raise serializers.ValidationError('Name cannot contains special characters')
        return validated_data 
       
