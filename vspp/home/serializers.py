from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    #phone = serializers.CharField(required=False)
    class Meta:
        model = Client
        fields = "__all__"

    #def validate_phone(self, value):
        #if value < str(2):
            #raise serializers.ValidationError("El número de telefono no puede estar vacío")

       # return value
    
    def validate_user(self, value):
        #print(value, type(value))
        if value.username == "valdo":
            raise serializers.ValidationError("El usuario 'valdo' no puede tener relación")
        return value




