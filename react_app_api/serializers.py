from rest_framework import serializers
from .models import Profile, Blogs
from django.contrib.auth.models import User



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











