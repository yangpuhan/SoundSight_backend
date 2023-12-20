from user_auth.models import User
from django.db import models
import datetime

# 音频信息表 AudioInfo
class AudioInfo(models.Model):
    # 音频信息的ID
    id = models.BigAutoField(primary_key=True)
    # 音频的checkCode
    checkCode = models.CharField(max_length=64)
    # 音频对应的文本
    json_text = models.JSONField(default=dict)
    # 音频的创建时间戳
    created_time = models.FloatField(default=(datetime.datetime.now()).timestamp())
    # 音频对应的用户外键
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        indexes = [models.Index(fields=["checkCode"])]
        
    def serialize(self):
        return {
            'id': self.id,
            'checkCode': self.checkCode,
            'text': self.json_text,
            'created_time': self.created_time,
            'user': self.user.serialize() if self.user else None,
        }
    
class FullAudio(models.Model):
    id = models.BigAutoField(primary_key=True)
    checkCode = models.CharField(max_length=64)
    full_text = models.TextField()
    summary = models.JSONField(default=dict)
    updated_time = models.FloatField(default=(datetime.datetime.now()).timestamp())
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        indexes = [models.Index(fields=["checkCode"])]
        
    def serialize(self):
        return {
            'id': self.id,
            'checkCode': self.checkCode,
            'summary': self.summary,
            'full_text': self.full_text,
            'updated_time': self.updated_time,
            'user': self.user.serialize() if self.user else None,
        }
    def __str__(self):
        return {
            'id': self.id,
            'checkCode': self.checkCode,
            'summary': self.summary,
            'full_text': self.full_text,
            'updated_time': self.updated_time,
            'user': self.user.serialize() if self.user else None,}.__str__()

    


