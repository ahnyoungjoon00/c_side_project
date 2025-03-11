from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

# def signup_view(request):
#     pass
#     # return render(request, 'accounts/home.html')

# def login_view(request):
#     pass

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 자동 로그인
            return redirect('home')  # 회원가입 후 홈으로 리다이렉트
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # 로그인 후 홈으로 리다이렉트
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})