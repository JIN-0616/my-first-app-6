#admin.py
#관리자사이트에서 모델클래스를 조회,삽입,삭제,수정하고자 할때 설정하는 파이썬파일

from django.contrib import admin
# 상대경로(같은폴더에 있는 파일이므로) 
#해당 파일에서 모델클래스를 알아야되므로 from - import를 사용
from .models import Question, Choice #from .model import *

#관리자 페이지에서 효과적으로 객체정보를 볼수있는 ModelAdmin클래스 상속
class ChoiceAdmin(admin.ModelAdmin):
    fields = ['choice_text', 'question']
    list_display =('choice_text', 'votes', 'question')
#fields -고정변수, 리스트에 변수이름을 str으로 저장
#list_display -- 특정속성을 listup해줌

#admin.site.register(클래스명)
#해당 모델클래스를 관리자사이트에 등록

admin.site.register(Question)
# admin사이트에 Question 클래스 내용을 보여줌

admin.site.register(Choice, ChoiceAdmin)
# Choice 모델클래스를 관리자 페이지에서 볼수 있도록 등록