from rest_framework import serializers

from drfproviderapp.models import Employee

# ModelSerializer => provide two thing :
    # Serialization => Convert QuerySet into dictionary convert into json format
    # deserialization => Convert json into dictionary convert into QuerySet send into database
    # Every Model Should Have serializers
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Employee
        fields = "__all__"
