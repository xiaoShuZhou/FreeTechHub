from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from POST.models import Pic

from POST.models import Post


def Login(request):
    error_msg = ''
    username = request.POST.get('username')
    print(username)
    password = request.POST.get('password')
    print(password)
    user=authenticate(username=username, password=password)
    print(user)
    if user:
        login(request, user)
        print(user)
        account = User.objects.get(username=username)
        id = int(account.id)
        return render(request, 'post.html')
    else:
        if username != None:
            error_msg='Username or password is wrong!'
    return render(request, 'login.html', {"error_msg": error_msg})

def register(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1==password2:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            if user:
                login(request, user)
                msg = 'register successfully!'
                return render(request, 'login.html', {'msg': msg})
        else:
            msg = 'Your passwords are not the same!'
            return render(request, 'register.html', {'msg': msg})
    return render(request, 'register.html')

def Logout(request):
    logout(request)
    return render(request, 'login.html')

def post(request):
    if request.method == "POST":
        post_content = request.Post.get('content')
        post=Post.objects.create(post_text=post_content)
        print(post)
        post.save()
        pic_post_id = Post.objects.get(post_text=post_content).id
        img = Pic(image=request.FILES.get('img'), pic_post_id=pic_post_id)
        print(img)
        img.save()
    return redirect('show/')

def show(request):
    imgs = Pic.objects.all()
    context = {
        'imgs':imgs
    }
    return render(request, 'show.html', context)