from django.shortcuts import render,HttpResponse
from .models import Post 
# Create your views here.


def Main(request):
    return render(request,'Dashboard/index.html')

def Add_Post(request):
    if(request.method=="POST"):
        
        slug = request.POST['slug']
        title = request.POST['title']
        
        content = request.POST['content']
        post = Post(Title=title,Slug=slug,MainText=content)
        post.save()
        return HttpResponse("ok")
def Show_Users(request):
    if(request.method=="GET"):
        return render(request,'Dashboard/show_users.html')