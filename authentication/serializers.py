# Serializers in Django REST Framework 
# are responsible for converting objects into data types 
# understandable by javascript and front-end frameworks

from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from authentication.models import User

class RegisterSerialzier(serializers.ModelSerializer):

    password = serializers.CharField(max_length = 128, min_length = 6, write_only = True)
    #coz you dont want to send the password at all to front end that is why write only 
    
    class Meta:
        model = User
        fields = ('user_type','username','email','password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        # ** is used as the user may send extra parameters

    
class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length = 128, min_length = 6, write_only = True)
        #if you remove this write only password will be sent to frontend
    
    class Meta:
        model = User
        fields = ('user_type','email','password','username','token',)

        read_only_fields = ['token']