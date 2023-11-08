from django.db import models
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    intro = models.TextField()
    body = models.TextField()
    creator = models.CharField(max_length=100, default='None')
    date_added = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-date_added']
        
    def __str__(self):
        return self.title