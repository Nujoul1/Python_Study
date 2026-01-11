"""定义 learning_logs的URL模式"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有Topic的页面
    path('topics/', views.topics, name='topics'),
    # 显示特定Topic的页面
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]