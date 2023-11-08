from rest_framework import serializers
from .models import Blog

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id',  'title', 'intro', 'body','creator', 'date_added']