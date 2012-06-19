#-*- coding: utf-8 -*-

from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from account.utils import _auth


def authenticate_handler(request,
						   third='SINA'):
	"""
		对帐号oauth2进行授权
	"""
	auth = _auth(third)
	auth_url = auth.get_authorize_url()
	return redirect(auth_url)


@login_required
def oauth_callback(request,
					third="SINA"):
	"""
		返回一个code
		保存用户的access_token 和其他信息
	"""
	code = request.REQUEST.get('code')
	openid = request.REQUEST.get('openid', None)
	openkey = request.REQUEST.get('openkey', None)
	
	if not code:
		# 非法的callback
		return HttpResponse("code not found.")

	auth = _auth(third)

	if not hasattr(request.user, _auth(third, flag=0)[0]):
		resource = auth.request_access_token(code)
		account = _auth(third, flag=0)[1](
			user = request.user,
		)

		_fields = {
			'SINA': ('access_token', 'remind_in', 'expires_in', 'uid'),
			'QQ': ('openid', 'openkey', 'access_token', 'expires_in', 'name', 'refresh_token')
		}
		for _f in _fields.get(third):
			if _f in resource:
				account.__setattr__(_f, resource[_f])
			elif _f in locals():
				account.__setattr__(_f, locals()[_f])
			else:
				pass
		account.save()
	return redirect("/success")