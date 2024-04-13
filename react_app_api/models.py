from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
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

class Blogsz(models.Model):
    title = models.CharField(max_length=500,default="Blogs Title")
    
    class Meta:
        ordering= ["-id"]
    
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


