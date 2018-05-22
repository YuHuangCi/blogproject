# comments/forms.py
from django import forms
from .models import Comment


# 通过创建表单类,使用表单的一些功能
class CommentForm(forms.ModelForm):
    class Meta:
        # 指定表单对应的数据库模型类
        model = Comment
        # 指定表单显示的字段
        fields = ['name', 'email', 'url', 'text']