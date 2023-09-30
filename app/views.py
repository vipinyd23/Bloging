from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Category, blogs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import auth,User
from django.contrib import messages
# Create your views here.

def home(request):
    blog=blogs.objects.all()[:11]
    cats=Category.objects.all()
    data={
        "blog":blog ,
        "cats":cats
    }
    return render(request,'home.html',data)

def posts(request, url):
    post = blogs.objects.get(url=url)
    cats = Category.objects.all()

    # print(post)
    return render(request, 'posts.html', {'blogs': post, 'cats': cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = blogs.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'blogs': posts})

def signup(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'hi {username},account created')
            print("success")
            return redirect('login')
    else:
            form=UserCreationForm()
    
    return render(request,'signup.html',{'form':form})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
          
        if user is not None:

            auth.login(request,user)
           
            return redirect('home')
            # return redirect("login")
        else:
            messages.info(request,'invalid')
            return redirect('login')
    else:
         return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('home')


def post(request):
    if request.method=='POST':
        title=request.POST.get('title')
        date_posted=request.POST.get('date_posted')
        content=request.POST.get('content')
        author=request.POST.get('author')
        cat=request.POST.get('category')
        # cat = Category.objects.all()
        en=blogs(title=title,date_posted=date_posted,content=content,author=author,category=cat)
        en.save()
    cats = Category.objects.all()
    return render(request,'post.html',{'cats':cats})   
        
# def signup(request):

#     if request.method=='POST':
#         first_name=request.POST['first_name']
#         last_name=request.POST['last_name']
#         username=request.POST['username']
#         email=request.POST['email']
#         password1=request.POST['password1']
#         password2=request.POST['password2']

#         user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password1=password1,password2=password2)
#         user.save()
#         # print("done")
#         # return redirect('/')
#     else:
#         return render(request,'signup.html')



def about(request):

    # obj1= blogs()
    # obj1.title= 'Khana Khajana'
    # obj1.date_posted= '23'
    # obj1.content='this is content1'
    # obj1.author='Vipin Yadav'

    # obj2 = blogs()
    # obj2.title= 'Study'
    # obj2.date_posted= '23'
    # obj2.content='this is content2'
    # obj2.author='Aman Yadav'

    # obj3 = blogs()
    # obj3.title= 'News'
    # obj3.date_posted= '2'
    # obj3.content='this is content3'
    # obj3.author='Anuj Yadav'

    # obj=[obj1,obj2,obj3]
    obj=blogs.objects.all()

    return render(request,'about.html',{'obj': obj})