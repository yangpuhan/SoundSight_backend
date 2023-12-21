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
    # 用户的个人信息创建时间戳
    created_time = models.FloatField(default=(datetime.datetime.now()).timestamp())
    # 用户的名字
    name = models.CharField(max_length=50, default="")
    # 用户的年龄
    age = models.IntegerField(default=18)
    # 用户的工作
    job = models.CharField(max_length=50, default="")
    # 用户的爱好
    hobby = models.CharField(max_length=50, default="")
    # 用户的专业
    major = models.CharField(max_length=50, default="")
    # 用户的规则
    rules = models.CharField(max_length=50, default="")

    class Meta:
        indexes = [models.Index(fields=["id"])]

    def serialize(self):
        return {
            'name': self.name,
            'age': self.age,
            'job': self.job,
            'hobby': self.hobby,
            'major': self.major,
            'rules': self.rules,
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
        
