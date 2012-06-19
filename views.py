#-*- coding: utf-8 -*-

from handlers_and_callback_views import *
from django.http import HttpResponse


def success(request):
	"""
		授权成功跳转页
	"""
	return HttpResponse(u"绑定成功")