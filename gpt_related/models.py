from user_auth.models import User
from django.db import models
import datetime

# 音频信息表 AudioInfo
class AudioInfo(models.Model):
    # 音频信息的ID
    id = models.BigAutoField(primary_key=True)
    # 音频对应的文本
    text = models.TextField()
    # 音频的创建时间戳
    created_time = models.FloatField(default=(datetime.datetime.now()).timestamp())
    # 音频对应的用户外键
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # polish后的文本
    polish_text = models.TextField(default="")
    # 是否已经summary
    is_summary = models.BooleanField(default=False)
    # 是否已经发送
    is_send = models.BooleanField(default=False)
    # 是否已经结束
    is_end = models.BooleanField(default=False)
    
    class Meta:
        indexes = [models.Index(fields=["id"])]
        
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


# 用户要求表
class UserRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    # 对应的用户外键
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # 用户的instruction
    instruction = models.TextField(default="default instruction")
    # 用户的meeting name
    meeting_name = models.TextField(default="")
    
# 用户语音总结表
class AudioSummary(models.Model):
    id = models.BigAutoField(primary_key=True)
    # 对应的用户外键
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # 最后一次的summary
    summary = models.TextField(default="")
    
# 用户的语音整合表
class AudioIntegration(models.Model):
    id = models.BigAutoField(primary_key=True)
    # 对应的用户外键
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # 最后一次的integration
    integration = models.TextField(default="")
    # 包含的音频的id列表
    audio_id_list = models.TextField(default="")