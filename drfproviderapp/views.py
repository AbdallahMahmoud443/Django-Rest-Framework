from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from drfproviderapp.models import Countries, Departments, Employee
from drfproviderapp.serializers import CountriesSerializer, DepartmentSerializer, EmployeeSerializer
from rest_framework import status,mixins,generics,viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

# use to add basic Authentication 
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


#  --------------------- Function Based View --------------------- 

@api_view(['GET','POST']) # => This Decorator covert (FBV) TO (FB API view)
def EmployeeListAPI(request):
    if request.method == "GET":
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee,many=True) # many=True => query have many records
        return Response(serializer.data) # return json Response
    
    if request.method == "POST":
        serializer = EmployeeSerializer(data=request.data) # send data to serializer and serializer send data to model
        if serializer.is_valid(): # valid data based on validation rules in model
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED) # return data and status code
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) # return error 
    
@api_view(['GET','PUT','DELETE'])
def EmployeAPI(request,pk):
    # before verythings must check if employee exists or not 
    try:
        employee = Employee.objects.get(pk=pk) # employee id 
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer =EmployeeSerializer(employee) # query set of employees
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer =EmployeeSerializer(employee,request.data) # employee data and request data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) # return error
    
    elif request.method == "DELETE":
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# ----------------------- Class Based View -----------------------
class EmployeeListAPI(APIView):
    
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
class EmployeeAPI(APIView):
    # method for getting employee
    def GetEmployee(self,pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Http404
        
    def get(self,request,pk):
        employee = self.GetEmployee(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
         employee = self.GetEmployee(pk)
         serializer = EmployeeSerializer(employee,request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_200_OK)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
    def delete(self,request,pk):
        employee = self.GetEmployee(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --------------------- Mixins --------------------- 

'''
In Django, mixins are used to add functionality to views, forms, and models, allowing developers to reuse code and improve the efficiency of their applications. Mixins are typically defined as classes, and can be added to other classes by using inheritance
'''

# inherited form another class like CreateModelMixin,ListModelMixin
# ListModelMixin => help us to get all record
# CreateModelMixin => hulp us to insert new record

class MixinEmployeeListAPI(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    # must named as same
    queryset = Employee.objects.all() # must add your query 
    serializer_class = EmployeeSerializer # serializer class must added

    def get(self,request):
        return self.list(request) # Get All Record
    
    def post(self,request):
        return self.create(request) # Create New Record

class MixinEmployeeAPI(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    # must named as same
    queryset = Employee.objects.all() # must add your query 
    serializer_class = EmployeeSerializer # serializer class must added

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)

# -------------------- Generic API View --------------------- 

class GenericEmployeeListAPI(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class GenericEmployeeAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class =EmployeeSerializer



#  --------------------- ViewSets --------------------- 
# 1- Create your class that inherited form viewsets.ModelViewSet
# Add Custom pagination To Customize Pagination 

class CustomPagination(PageNumberPagination):
        page_size =2

class ViewSetsEmployeesAPI(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # pagination
    # pagination_class = CustomPagination

    # filter_backends => class
    # Name_fields => Columns Names for searching or filtering

    # filters only 
    # filter_backends = [DjangoFilterBackend] # To Apply Filter in endpoint level
    # filterset_fields = ['FirstName','LastName','Salary']

    # search only 
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['FirstName','LastName','Salary']

    # Filter And Search together
    # filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    # filterset_fields = ['FirstName','LastName','Salary']
    # search_fields = ['FirstName','LastName','Salary']

    # Search With Experssion 
    # search_fields = ["^FirstName","^LastName"] # Start With (Char) of word
    # search_fields = ["=FirstName","=LastName"] # World Exact 

    # Ordering 
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['FirstName','LastName'] # sorting will be on this two columns (-FirstName,-LastName) => descending
    ordering = ['id'] # defualt sorting based on id (-id => descending)


    
class ViewSetsDepartmentsAPI(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
    #! Authentication Will Appy on this endpoint only  (locally) must login as user to access these endpoint
    # authentication_classes =[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    
class ViewSetsCountriesAPI(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


