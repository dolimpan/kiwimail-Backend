from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length = 30) #이름
    insta = models.CharField(max_length = 30, null = True, blank = True) #인스타그램 ID
    email = models.CharField(max_length = 60) #이메일 주소
    email_ok = models.BooleanField(default = False) #이메일 수신 동의 여부
    post_count = models.BigIntegerField(default = 0) #받은 편지 개수
    bgm_num = models.BigIntegerField(null = True, blank = True) #설정한 배경 음악
    oAuthAttributeName = models.CharField(max_length = 100) #구글 로그인 고유값

    def __str__(self):
        return self.name

class Message(models.Model):
    receiver = models.CharField(max_length=20)
    writer = models.CharField(max_length=20)
    content = models.CharField(max_length=1500)
    writingPad = models.BigIntegerField() #편지지 개수 확보 후 확정하기
    emoticon = models.BigIntegerField(max_length = 10) # 이모티콘 개수 확보 후 확정
    created_at = models.DateTimeField(default = timezone.now)
    disclosure = models.BooleanField(default = False)

    def __str__(self):
        return self.writer + "->" + self.receiver

    @classmethod
    def create(cls, writer, content):
        ret = cls(writer = writer, content=content)
        return ret