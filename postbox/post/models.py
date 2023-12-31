from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length = 30) #�̸�
    insta = models.CharField(max_length = 30, null = True, blank = True) #�ν�Ÿ�׷� ID
    email = models.CharField(max_length = 60) #�̸��� �ּ�
    email_ok = models.BooleanField(default = False) #�̸��� ���� ���� ����
    post_count = models.BigIntegerField(default = 0) #���� ���� ����
    bgm_num = models.BigIntegerField(null = True, blank = True) #������ ��� ����
    oAuthAttributeName = models.CharField(max_length = 100) #���� �α��� ������

    def __str__(self):
        return self.name

class Message(models.Model):
    receiver = models.CharField(max_length=20)
    writer = models.CharField(max_length=20)
    content = models.CharField(max_length=1500)
    writingPad = models.BigIntegerField() #������ ���� Ȯ�� �� Ȯ���ϱ�
    emoticon = models.BigIntegerField(max_length = 10) # �̸�Ƽ�� ���� Ȯ�� �� Ȯ��
    created_at = models.DateTimeField(default = timezone.now)
    disclosure = models.BooleanField(default = False)

    def __str__(self):
        return self.writer + "->" + self.receiver

    @classmethod
    def create(cls, writer, content):
        ret = cls(writer = writer, content=content)
        return ret