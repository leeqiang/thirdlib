##腾讯微博 － 新浪微博 Oauth2.0 认证

weibo oauth2代码来自: http://code.google.com/p/sinaweibopy/
qqweibo oauth2代码来自: https://github.com/jinuljt/qqweibov2

本代码只对两种微博进行了整合，设计了帐号模型进行保存授权信息。

##测试前需在settings.py内设定：

```
SINA_CONSUMER_KEY = ''
SINA_CONSUMER_SECRET = ''
SINA_CALLBACK = ''

QQ_CONSUMER_KEY = ''
QQ_CONSUMER_SECRET = ''
QQ_CALLBACK = ''
```

##授权地址及callback
 - ./manage.py syncdb
 - ./manage.py runserver

访问:  http://127.0.0.1/sina/authenticate
