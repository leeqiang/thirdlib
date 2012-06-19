#-*- coding: utf-8 -*-
"""
	帐号模型
"""

from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
	"""
		base.com account
	"""
	access_token = models.CharField(max_length=200)
	user = models.OneToOneField(User, null=True, blank=True)
	expires_in = models.IntegerField()

	class Meta:
		abstract = True


class SinaAccount(Account):
	"""
		weibo.com account
	"""
	remind_in = models.IntegerField()
	uid = models.IntegerField()

	def __unicode__(self):
		return self.user.username

class QQAccount(Account):
	"""
		t.qq.com account
	"""
	name = models.CharField(max_length=50)
	refresh_token = models.CharField(max_length=100)
	openid = models.CharField(max_length=100, null=True, blank=True)
	openkey = models.CharField(max_length=100, null=True, blank=True)

	def __unicode__(self):
		return self.name


