from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from POST.models import Pic
from POST.models import Post

def Login(request):
    error_msg = ''
    username = request.POST.get('username')
    password = request.POST.get('password')
    user=authenticate(username=username, password=password)
    print(user)
    if user:
        login(request, user)
        print(user)
        account = User.objects.get(username=username)
        id = int(account.id)
        return redirect('/post/%d/'% id)
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

def post(request, user_id):
    if request.method == "POST":
        post_content = request.POST.get('content')
        user = User.objects.get(id=user_id)
        post = Post.objects.create(post_text=post_content, user_id=user)
        post.save()
        id = Post.objects.get(post_text=post_content)
        files = request.FILES.getlist('img')
        for file in files:
            img = Pic(image=file, pic_post_id=id)
            img.save()
        return redirect('/show/%d/'% user_id)
    else:
        user = User.objects.get(id=user_id)
        return render(request, 'post.html', {'user': user})

def show(request, user_id):
    texts = Post.objects.filter(user_id=user_id)
    print(type(texts), len(texts), texts[0])
    text=[]
    img=[]
    for i in range(len(texts)):
        text.append(texts[i])
        imgs = Pic.objects.filter(pic_post_id=texts[i].id)
        img.append(imgs)
    return render(request, 'show.html', {'img':imgs, 'text':text})