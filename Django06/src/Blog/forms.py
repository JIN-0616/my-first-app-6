from django.forms.models import ModelForm
from .models import Post,Image,File

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('pub_date', 'auther')
    #*리스트형태로 담음, **사전형태로 담음
    def __init__(self, *ages, **kwargs):
        super(PostForm,self).__init__(*ages, **kwargs)
        #사용자가 글종류를 선택하지 않았을 때의 기본값
        self.fields['type'].empty_label = None

"""class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ('images',)"""
