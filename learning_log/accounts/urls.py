"""为应用程序accounts 定义URL模式"""

from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    # 包含默认身份验证URL
    path('', include('django.contrib.auth.urls')),
]