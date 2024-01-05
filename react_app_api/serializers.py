from rest_framework import serializers
from .models import Profile, Blogs
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username','email','first_name', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email','first_name']


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    email = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Profile
        fields = ["id","user","email","image","about"]
    
    def get_user(self,obj):
        return f"{obj.user.first_name}"
    def get_email(self,obj):
        return obj.user.email


class BlogsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only= True)
    # name = serializers.SerializerMethodField(read_only= True)
    class Meta:
        model = Blogs
        fields = [
            "id","title","body","date","most_viewed","last_modified","user"
        ]
    # def get_name(self,obj):
    #     return "name_of_user"
    def get_user(self,obj):
        obj2 = Profile.objects.filter(user=obj.user).first()
        return ProfileSerializer(obj2).data







# class TutorialSerializer(serializers.ModelSerializer):
#     students= serializers.SerializerMethodField(read_only= True)
#     materials= serializers.SerializerMethodField(read_only= True)
#     tutor= serializers.SerializerMethodField(read_only= True)
#     class Meta:
#         model = Tutorial
#         fields = [
#             "id","course_name","topic","level","detail","started","tutorial_time",
#             "price","link","course_image","students","name_of_tutor","tutors_image","expire_time",
#             "last_seen","date","levels","about_teacher","materials","waiting_tutor","tutor"
#         ]
#     def get_students(self,obj):
#         return obj.students.count()
#     def get_tutor(self,obj):
#         ids = None
#         if obj.which_tutor:
#             ids = obj.which_tutor.id
#         return ids
#     def get_materials(self,obj):
#         return obj.materials.count()
    
    
# class SchoolsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Schools
#         fields = [
#             "id","name","state","address","info","logo","date"
#         ]
















