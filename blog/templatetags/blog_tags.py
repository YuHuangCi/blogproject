# blog/templatetags/blog_tags

from django import template
from ..models import Post, Category

register = template.Library()


# 定义获得最新推荐的文章函数
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

# 定义归档标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


# 定义分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()
