from django.urls import path
from .views import *
#{% url 'vote:index' %} reverse{'vote:index'}
app_name = 'vote'

urlpatterns =[
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    #path의 경우 앞부분에 / 자동으로 붙음
    path('vote/<int:question_id>/', vote, name='vote'),
    path('result/<int:question_id>/', result, name='result'),
    path('registerQ/', registerQ, name='registerQ'),
    path('deleteQ/<int:question_id>/',deleteQ, name='deleteQ'),
    #매개변수 /<int:question_id>/ <--> def deleteQ(request, question_id)
    path('registerC/<int:question_id>/', registerC, name='registerC'),
    path('deleteC/<int:choice_id>/',deleteC,name='deleteC'),
    path('updateQ/<int:question_id>/',updateQ,name='updateQ'),
    # /<>/ : <>기준으로 값을 받으므로  주의, 앞부분 /는 자동으로 붙으나
    # 뒷부분은 /를 꼭 붙여줘야 함
]