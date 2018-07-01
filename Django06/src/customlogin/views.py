from django.shortcuts import render
from .forms import *
from django.contrib.auth import login, authenticate
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

def signup(request):
    if request.method=="GET":
        form = UserForm()
        return render(request, "customlogin/templates/signup.html",
                      {'form':form})
    elif request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            #form.cleaned_data : 폼객체에 저장된 값들을 꺼낼때 사용(사전형)
            #cleaned_data는 is_valid 할때만 사용가능함
            #def Func1(q,b,**a) **a : q,b 매개변수 외에 다른 값들이 들어오면
            #                         사전형으로 a 변수가 처리
            # (*a) 여러 매개변수를 리스트형으로 받음
            #create_user(username=form.cleaned_data['username'],
            #            password=form.cleaned_data['password'],
            #            email=form.cleaned_data['email'])
            #create_user(username,password,email): 장고에서 지원하는 User
            #                              모델클래스에 새로운 객체를 만들때 사용
            # 패스워드 확인
            if form.cleaned_data['password'] == form.cleaned_data['password_cheak']:
                #User 모델클래스는 'password_check' 속성을 사용하지 않아 에러 발생
                #new_user = User.objects.create_user(**form.cleaned_data)
                new_user=User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password'])
                               
                # 매개변수명이 같기때문에 사용가능
                #login(request, User객체):해당요청을 보낸 클라이언트가 User객체로
                #                        로그인하는 작업을 함
                login(request, new_user)
                return HttpResponseRedirect(reverse('vote:index'))
            else:
                error = "비밀번호가 맞지않음"
        else:
            error= "유효하지않은 값이 입력됨"
        
        return render(request, "customlogin/templates/signup.html",
                      {'form':form, 'error': error})

def signin(request):
    if request.method=="GET":
        form = LoginForm()
        return render(request, 'customlogin/templates/signin.html',
                      {'form':form})
    elif request.method=="POST":
        form = LoginForm(request.POST) # ID, 비밀번호 실패시 보낼 폼
        username1 = request.POST.get('username') #ID 추출
        password1 = request.POST.get('password') #Password 추출
        # authenticate(username,password) : user모델클래스에 해당 ID와
        # Password로 저장된 객체를 찾아 반환, 객체가 없는 경우 None 반환
        # None반환 2가지 - id없음, pw틀림
        user = authenticate(username=username1,password=password1)
        # (값,변수) is 타입: (값,변수)가 타입과 동일한지 True,False반환
        # user is not None == not(user is None) 동일 문법
        if user is not None: #user변수의 값이 None타입이 아닌가?
            login(request, user) #로그인
            return HttpResponseRedirect(reverse("vote:index"))
        else: # 해당 ID와 비밀번호를 가진 User 객체가 없는 경우
            error ="아이디 또는 비밀번호가 틀렸습니다."
        return render(request, "customlogin/templates/signin.html",
                      {'form':form,'error':error})
    
            
            
            
            
            
            
            
            