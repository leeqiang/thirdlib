#-*- coding: utf-8 -*-
"""
	Oauth2.0 工具
"""
from django.conf import settings

from weibo.oauth2 import APIClient
from qq.oauth2 import APIClient as QQAPI

from account.models import SinaAccount, QQAccount


_API = {
	'SINA': APIClient,
	'QQ': QQAPI
}

_acounts = {
	'SINA': ("sinaaccount", SinaAccount),
	'QQ': ("qqaccount", QQAccount)
}

def _auth(third, flag=1):
	"""
		返回某第三方的认证函数或者实例model
		默认返回认证函数
	"""

	def API(third):
		return _API.get(third)

	def accounts(third):
		return _acounts.get(third)

	if not flag:
		return accounts(third)

	key = "%s_CONSUMER_KEY" % third
	secret = "%s_CONSUMER_SECRET" % third
	callback = "%s_CALLBACK" % third

	auth = API(third)(
		getattr(settings, key),
		getattr(settings, secret),
		getattr(settings, callback)
	)
	return auth
