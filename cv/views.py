from django.shortcuts import render
from Dashboard.models import Post
# Create your views here.



def Main(request):
    post = Post.objects.filter(Status='p')
    return render(request,"cv/index.html",{'post':post})

def post_body(request,slug):
    post=Post.objects.all().filter(Slug=slug)
    return render(request,"cv/blog.html",{'post':post,'slug':slug})
