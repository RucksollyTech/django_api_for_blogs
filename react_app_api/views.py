from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Blogs
from .serializers import BlogsSerializer
from django.contrib.auth.models import User

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
        













