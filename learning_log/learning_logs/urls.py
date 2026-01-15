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
    # 用于添加新Topic的页面
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新的Entry的页面
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 用于编辑已有Entry的页面
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]