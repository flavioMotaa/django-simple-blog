from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title