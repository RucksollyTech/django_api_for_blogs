from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from django.utils import timezone
User = settings.AUTH_USER_MODEL

from django.contrib.auth.models import User as User2



class Blogs(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True) 
    title = models.CharField(max_length=500,default="Blogs Title")
    body = models.TextField(default="Blogs body")
    date= models.DateTimeField(auto_now_add = True)
    most_viewed = models.IntegerField(default=1)
    last_modified =models.DateTimeField(auto_now_add = False,blank=True,null = True)
    
    class Meta:
        ordering= ["-most_viewed"]
    
    def __str__(self):
        return self.title




class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    about= models.TextField()
    image = models.ImageField(upload_to ="media/", null=True,blank=True)
    date= models.DateTimeField(auto_now_add = True)
    
    
    def get_reset_token(self, expires_sec=600):
        s = Serializer(settings.SECRET_KEY, expires_sec)
        return s.dumps({'user_id': self.user.id}).decode('utf-8')


    @staticmethod
    def verify_reset_token(token):
        s = Serializer(settings.SECRET_KEY)
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User2.objects.get(pk=user_id)
    
    def __str__(self):
        return self.user.email


def user_did_save(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
post_save.connect(user_did_save, sender=User)




# class Schools(models.Model):
#     user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True) 
#     name= models.TextField()
#     state= models.TextField()
#     most_viewed = models.IntegerField(default=1)
#     logo = models.ImageField(upload_to ="media/", null=True,blank=True)
#     address= models.TextField(default="School information")
#     info= models.TextField(default="School information")
#     date= models.DateTimeField(auto_now_add = True)
    
#     class Meta:
#         ordering= ["-most_viewed"]
        
#     def __str__(self):
#         return self.name


# class Materials(models.Model):
#     user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True) 
#     course_name = models.CharField(max_length=10000,default="Chemistry")
#     author = models.CharField(max_length=10000,null=True,blank=True)
#     material_title = models.CharField(max_length=10000,default="Fundamental")
#     material = models.FileField(upload_to="media/bkk")
#     schools = models.ForeignKey(Schools,on_delete=models.SET_NULL,null=True,blank=True )
#     pages = models.IntegerField(default=1)
#     detailed_summary_of_material = models.TextField(null=True,blank=True,default="Materials Details")
#     price = models.DecimalField(max_digits=10,decimal_places = 1,null = True,blank=True)
#     date= models.DateTimeField(auto_now_add = True)
#     levels = models.IntegerField(null=True,blank=True,default=100)
#     students = models.ManyToManyField(User,blank=True, related_name="material_students" )
#     image = models.ImageField(upload_to ="media/", null=True,blank=True)
#     most_viewed = models.IntegerField(default=1)
#     last_modified =models.DateTimeField(auto_now_add = False,blank=True,null = True)
    
#     class Meta:
#         ordering= ["-most_viewed"]
    
#     def __str__(self):
#         return self.course_name




