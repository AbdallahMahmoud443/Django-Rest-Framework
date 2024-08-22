from rest_framework import serializers

from drfproviderapp.models import Countries, Departments, Employee

# ModelSerializer => provide two thing :
    # Serialization => Convert QuerySet into dictionary convert into json format
    # deserialization => Convert json into dictionary convert into QuerySet send into database
    # Every Model Should Have serializers
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Employee
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
    # Nested Serializer
    employees = EmployeeSerializer(read_only=True,many=True,source='Employee_Department') # source is important  (Employee_Department) Relation Name
    class Meta:
        model = Departments
        fields = "__all__"
        
class CountriesSerializer(serializers.ModelSerializer):
    # Nested Serializer 
    # (source='Employee_Country') => make array of employees in countries
    employees = EmployeeSerializer(read_only=True,many=True,source='Employee_Country') # source is important  (Employee_Country) Relation Name
    class Meta:
        model = Countries
        fields = "__all__"