"""Django06 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#해당 파일이 view 함수를 알아야 되므로 from ~ import로 함수 추가
#urls와 views가 다른 파일위치이므로 절대경로로 표현
from vote.views import *
from customlogin.urls import *
from django.conf import settings
from django.conf.urls.static import static

#vote폴더안에 view파일 중 모든함수 추가 
urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls, name="admin"),
    #path(문자열, 함수명) : 웹 클라이언트가 문자열에 해당하는 URL로
    #                    접근 시 매칭된 함수를 호출함
    #http://127.0.0.1:8000 주소로 접근시
    #vote 어플리케이션 내의 index함수 호출
#     path('', index, name='index'),
#     #http://127.0.0.1:8000/detail/1/
#     #detail 함수에 question_id에 1을 전달 후 호출
#     path('detail/<int:question_id>/', detail, name='detail'),
#     path('vote/<int:question_id>/', vote, name='vote' ),
#     path('result/<int:question_id>/', result, name='result')
    path('vote/', include('vote.urls')),
    #http://127.0.0.1:8000/vote/로 시작되는 URL들을
    #vote폴더 안에있는 urls 파이썬파일로 처리하도록 매칭
    
    #include하면서 그룹이름을 정하고싶은 경우
    #path('vote',include('vote.urls', namespace='vote') )
    path('login/', include('customlogin.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('blog/', include('Blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






