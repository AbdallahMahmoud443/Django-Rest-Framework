"""
URL configuration for drfproviderproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from drfproviderapp import views

# With ViewSets work with Router 
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token # to get token of login user (this view return token as response)
'''
    #! from postman send post request to this view and put (username,password) to return token of specific user
'''

router = DefaultRouter()
router.register('api/viewsetsemployees',views.ViewSetsEmployeesAPI)
router.register('api/viewsetsdepartments',views.ViewSetsDepartmentsAPI)
router.register('api/viewsetscountries',views.ViewSetsCountriesAPI)



urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('get-api-auth-token/',obtain_auth_token,name="api_auth_token") # get token of user 
]


'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/emplyeeslist/',views.EmployeeListAPI),
    path('api/employee/<int:pk>',views.EmployeAPI),
    
    path('api/cbvemployeeslist/',views.EmployeeListAPI.as_view()),
    path('api/cbvemployee/<int:pk>',views.EmployeeAPI.as_view())

    path('api/mixemployeelist/',views.MixinEmployeeListAPI.as_view()),
    path('api/mixemployee/<int:pk>',views.MixinEmployeeAPI.as_view()),

    path('api/genericemployeelist/',views.GenericEmployeeListAPI.as_view()),
    path('api/genericemployee/<int:pk>',views.GenericEmployeeAPI.as_view()),
]
'''