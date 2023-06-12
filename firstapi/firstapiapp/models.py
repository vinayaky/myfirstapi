from django.db import models
import uuid
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user= models.ForeignKey(User, on_delete= models.SET_NULL,null=True,blank=True)
    Name=models.CharField(max_length=20)    
    Email=models.EmailField(unique=True)    
    Bio=models.TextField(max_length=500,null=True)  
    Image=models.ImageField('image/') 
    created_at=models.DateField(auto_now=True)
    update_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.Name
