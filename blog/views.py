from django.shortcuts import render
from blog.models import BlogsPost
from blog.models import PostType

# Create your views here.
def blog_index(request):
    blog_list = BlogsPost.objects.all()  # 获取所有数据
    return render(request,'index.html', {'blog_list':blog_list})   # 返回index.html

def blog_detail(request,id):
    blog_detail=BlogsPost.objects.get(id)
    return render(request,'detail.html', {'blog_detail':blog_detail})

def blog_type(request):
    type_list=PostType.objects.all()
    return render(request,'type.html',{'type_list':type_list})