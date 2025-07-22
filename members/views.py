from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms  import UserCreationForm


def login_user(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password = password)
        if user is not None:
            login(request , user)
            return redirect('home')
        else:
            messages.success(request,("something went wrong please try again..."))
            return redirect('login-user')
        
    else:
      return render(request , 'authenticate/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request , ("You were successfully logged out !!.."))
    return redirect('home')
# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username = username , password=password)
            login(request , user)
            messages.success(request , ('successfully registered'))
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request , 'authenticate/register_user.html',{'form':form})
            