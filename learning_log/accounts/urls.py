"""为应用程序accounts 定义URL模式"""

from django.urls import path, include
from accounts import views

app_name = 'accounts'
urlpatterns = [
    # 包含默认身份验证URL
    path('', include('django.contrib.auth.urls')),
    # 注册页面
    path('register/', views.register, name='register'),
]