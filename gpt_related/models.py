from user_auth.models import User
from django.db import models
import datetime

# 音频信息表 AudioInfo
class AudioInfo(models.Model):
    # 音频信息的ID
    id = models.BigAutoField(primary_key=True)
    # 音频的checkCode
    checkCode = models.CharField(max_length=64)
    # 音频的简易指令
    instruction = models.CharField(max_length=64)
    # 音频对应的文本
    text = models.TextField()
    # 音频的创建时间戳
    created_time = models.FloatField(default=(datetime.datetime.now()).timestamp())
    # 音频的更新时间戳
    updated_time = models.FloatField(default=(datetime.datetime.now()).timestamp())
    # 音频对应的用户外键
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        indexes = [models.Index(fields=["checkCode"])]
        
    def serialize(self):
        return {
            'id': self.id,
            'checkCode': self.checkCode,
            'text': self.text,
            'created_time': self.created_time,
            'updated_time': self.updated_time,
            'user': self.user.serialize() if self.user else None,
        }

