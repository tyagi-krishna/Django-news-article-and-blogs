from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import View
from newsapi import NewsApiClient
from  django.contrib.auth.decorators import login_required
from .models import Blog
from .serializers import BlogsSerializer


class MySignUpView(View):
    form_class = UserCreationForm
    template_name = 'registration/sign_up.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            u = User.objects.create_user(
                    form.cleaned_data.get('username'),
                    request.POST['email'],
                    form.cleaned_data.get('password1'),
                    is_active = True
            )
            # TODO Display message and redirect to login
            return HttpResponseRedirect('/login/')
        return render(request, self.template_name, {'form': form})
    
def home(request):
    return render(request, 'header.html')
    


@login_required
def profile(request):
    username = request.user.username
    newsapi = NewsApiClient(api_key='01e393602d0549c6a24d35cfa3af59d5')
    all_articles = newsapi.get_everything(q='everything')

    return render(request, 'dashboard.html', {'username': username, 'all_articles': all_articles})

def blog(request):
    blog = Blog.objects.all()
    username = request.user.username
    serializer = BlogsSerializer(blog, many=True)
    return render(request, 'blogs.html', {'data': serializer.data, 'username': username})
    
def add_blog(request):
    username = request.user.username
    if request.method=='POST':
        blog=Blog()
        blog.creator = request.user.username
        blog.title = request.POST.get('title')
        blog.intro = request.POST.get('intro')
        blog.body = request.POST.get('body')
        blog.save()
        print(blog.creator)
        return redirect('blog')
    

    else:
        return render(request, 'add_blog.html', {'username': username})
    
def delete_blog(request):
    username = request.user.username
    print(username)
    blog = Blog.objects.filter(creator=username)
    serializer = BlogsSerializer(blog, many=True)
    return render(request, 'delete_blog.html', {'data': serializer.data, 'username': username})
    
def delete(request, title):
    blog_to_delete = Blog.objects.filter(title=title)
    blog_to_delete.delete()
    return redirect('blog')
    