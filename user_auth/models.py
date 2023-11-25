from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# 用户历史表 UserHistory
class UserHistory(models.Model):
    # 用户历史的ID
    id = models.BigAutoField(primary_key=True)
    # 用户的ID
    user_id = models.BigIntegerField()
    # 用户的历史
    history_json = models.TextField()
    # 用户的历史创建时间戳
    created_time = models.FloatField(default=(datetime.datetime.now()).timestamp())

    class Meta:
        indexes = [models.Index(fields=["id"])]

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'history_json': self.history_json,
            'created_time': self.created_time,
        }

# 用户个人信息表 UserProfile
class UserProfile(models.Model):
    # 用户个人信息的ID
    id = models.BigAutoField(primary_key=True)
    # 用户的ID
    user_id = models.BigIntegerField()
    # 用户的个人信息
    profile_json = models.TextField()
    # 用户的个人信息创建时间戳
    created_time = models.FloatField(default=(datetime.datetime.now()).timestamp())

    class Meta:
        indexes = [models.Index(fields=["id"])]

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'profile_json': self.profile_json,
            'created_time': self.created_time,
        }

# 用户表 User
class User(AbstractUser):
    # 用户的ID
    id = models.BigAutoField(primary_key=True)
    # 用户的个人信息(外键)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    # 用户的历史(外键)
    history = models.ForeignKey(UserHistory, on_delete=models.CASCADE, null=True)
    # 用户的个人信息创建时间戳
    created_time = models.FloatField(default=(datetime.datetime.now()).timestamp())

    def serialize(self):
        return {
            'id': self.id,
            'profile': self.profile.serialize() if self.profile else None,
            'history': self.history.serialize() if self.history else None,
            'created_time': self.created_time,
        }
        
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