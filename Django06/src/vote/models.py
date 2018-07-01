from django.db import models
#장고가 생성한 User모델클래스
from django.contrib.auth.models import User 
#모델: 데이터를 어떤 형식으로 저장할지 표현하는 것
#모델 클래스 정의 후 객체를 만들어 사용
#class 클래스명(models.Model):
#MakeMigration, Migrate 시 setting.py -> INSTALLED_APPS 변수에
#애플리케이션 이름이 들어가 있어야 사용할 수 있음

#모델 정의를 다 한 후 해야되는 행동
#1.모델클래스가 변경된 애플리케이션에서 MakeMigration
# 프로젝트 오른쪽클릭 ->django->make migration 선택
# ->애플리케이션이름 입력
#2.변경사항을 데이터베이스에 적용 - Migrate
# 프로젝트 오른쪽클릭 ->django->migrate 선택
# Create your models here.
class Question(models.Model):
    #User 모델클래스를 외래키로 참조
    auther = models.ForeignKey(User,on_delete=models.CASCADE)
    #models.CharField : 글자수제한이 있는 문자열을 저장하는 클래스, max_length 필수
    question_text = models.CharField('질문 제목',max_length=200)
    #models.DateTimeField : 날짜와 시간을 저장하는 클래스
    pub_date = models.DateTimeField('생성일자')
    #str : 객체를 표현할 때 나오는 문자열
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField('답변 제목',max_length=100)
    #투표값 저장 공간
    #models.IntegerField : 정수값을 저장할 수 있는 클래스
    votes = models.IntegerField('투표 수',default=0)
    #외부키(왜래키)참조 - 1:n 관계
    #models.ForeignKey : 왜래키, 다른 테이블을 참조,
    #Question 객체 1개 : Choice 객체 n개
    #on_delete : 연결한 객체가 삭제됬을때, 자신도 삭제될지 옵션을 지정
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.choice_text
    
    #객체명.question.pub_date 단독접근시 변수 접근경로설정 예시