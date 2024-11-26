

from django.db import models




    
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the role (e.g., Admin, Viewer)
    description = models.TextField(blank=True, null=True)  # Optional description for the role

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True,default="ex@gmail.com")
    roles = models.CharField(max_length=200, default="User")

    is_active = models.BooleanField(default=True)
    permissions = models.CharField(max_length=200, default="per")
    # permissions = models.ManyToManyField(Permission, related_name="roles")
    # created_at = models.DateTimeField(auto_now_add=True)
    
   
    def __str__(self):
        return self.username
    


 