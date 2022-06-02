from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

def login(request):
    if request.method == 'POST': # 아이디와 비번을 입력하고 로그인 버튼을 눌렀을 때
        form = AuthenticationForm(request, request.POST) # 인증하는 코드
        if form.is_valid():
            auth_login(request, form.get_user()) # 로그인 코드
        return redirect('index')
    else: # login 페이지를 처음 들어갔을 때
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
def logout(request):
    auth_logout(request)
    return redirect('index')