from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from .models import Profile,Blogs
from .serializers import UserSerializer,ProfileSerializer,UserSerializerWithToken,BlogsSerializer
import json
from django.conf import settings
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status
from pypaystack import Transaction
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from rest_framework.views import APIView
from django.core.mail import EmailMultiAlternatives,send_mail
from decouple import config

JWT_authenticator = JWTAuthentication()

@api_view(['GET','POST'])
def home(request,*args,**kwargs):
    
    
    return Response({"hello": "Hello World6"},status=200)


@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def create_blog(request):
    data = request.data
    # user=request.user
    user = User.objects.get(pk=1)
    blogs = Blogs.objects.create(
        user=user,
        title=data['title'],
        body=data['body']
    )
    serializer = BlogsSerializer(blogs)
    

    return Response(serializer.data,status=200)
    


@api_view(['GET','POST'])
def blogs(request,*args,**kwargs):
    obj = Blogs.objects.all()
    serializer = BlogsSerializer(obj,many=True)
    if obj:
        return Response(serializer.data,status=200)
    else:
        return Response(None,status=200)



@api_view(['GET','POST'])
def blog_detail(request,pk,*args,**kwargs):
    pk=int(pk)
    obj = Blogs.objects.get(pk=pk)
    serializer = BlogsSerializer(obj)
    if obj:
        return Response(serializer.data,status=200)
    else:
        return Response(None,status=200)
        
        
# @api_view(['GET','POST'])
# def create_blog(request,*args,**kwargs):
#     pk=int(pk)
#     obj = Blogs.objects.get(pk=pk)
#     serializer = BlogsSerializer(obj)
#     if obj:
#         return Response(serializer.data,status=200)
#     else:
#         return Response(None,status=200)
        
        

# @api_view(['GET'])
# def school_detail(request,pk,*args,**kwargs):
#     pk=int(pk)
#     obj = Schools.objects.get(id=pk)
#     if not obj :
#         return Response({'detail': 'There is no such school'},status=status.HTTP_400_BAD_REQUEST)
#     try:
#         most_sch = Schools.objects.all()[:4]
#         sch_courses = Courses.objects.filter(schools=obj).all()[:30]
#         all_courses= CoursesSerializer(sch_courses,many=True)
#         obj2 = Materials.objects.filter(schools=obj).all()[:4]      
#         serializer = SchoolsSerializer(obj)
#         most_v= SchoolsSerializer(most_sch,many=True)
#         main_obj = MaterialsSerializer(obj2,many=True)
        
#         context={
#             "school" :serializer.data,
#             "most_schools" : most_v.data,
#             "most_materials" : main_obj.data,
#             "courses" : all_courses.data
#         }
#     except:
#         context={
#             "school" :serializer.data,
#             "most_schools" : [],
#             "most_materials" : [],
#             "courses" : []
#         }
#     obj.most_viewed = obj.most_viewed + 1
#     obj.save()
#     return Response(context,status=200)


# @api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
# def userPaid(request,pk,*args,**kwargs):
#     pk=int(pk)
#     user = request.user
#     obj = Courses.objects.filter(students=user.id).first()
#     serializer = CoursesSerializer(obj)
#     if obj:
#         return Response(serializer.data,status=200)
#     else:
#         return Response(None,status=200)
        
        














