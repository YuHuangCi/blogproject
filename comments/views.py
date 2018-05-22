# comments/views.py
from django.shortcuts import render, get_object_or_404, redirect

# from ..comments.forms import CommentForm
# from ..blog.models import Post
from .forms import CommentForm

from blog.models import Post


def post_comment(request, post_pk):
    # 第一步:获取评论文章,使得之后文章和评论关联起来
    """
    第二步: 通过get_object_or_404,
            判断是否拿到Post
    """
    post = get_object_or_404(Post, pk=post_pk)
    """
    1.Http 请求有get和post两种,一般用户通过用户表单提交的数据都是
    post请求
    2.因此只用当用户的请求为post时才需要处理表单的数据
    """
    # 不管是前端还是用户提供的数据都有可能是错误的,所以我们判断
    if request.method == 'POST':
        """
        1.用户提交的数据存在于request.POST中,这是一个类字典对象
        2.我们处理这些数据使其能够成为构造CommentForm的实例
        3.生成表单数据
        """
        form = CommentForm(request.POST)

        if form.is_valid():
            """
            1.调用form.is_valid(),判断表单的数据是否符合要求
            2.如果数据符合要求,使用表单的save(),讲数据保存到数据库
            3.save(参数),如果设置参数=False,则不将表单数据保存到数据库
            """
            comment = form.save(commit=False)  # 生成comment模型类的实例

            # 将评论和被评论的文章关联起来
            comment.post = post

            # 将评论的数据保存到数据库,使用save方法
            comment.save()
            """
            1.评论完之后应该跳转到详情页面,使用redirect
            2.redirect()接受一个模型的实例时,调用这个实例的get_absolute_url方法
            3.通过这个实例的url方法,实现跳转的功能
            """
            return redirect(post)

        else:
            """
            1.如果数据不合法,则重新跳转回详情页,并且渲染表单的错误
            2.我们传入三个模板变量给detail.html
            3.使用post.comment_set.all() 反向查询全部评论
            """
            # 通过外键拿到所有的评论
            comment_list = post.comment_set.all()
            # 拿到三个变量给模板
            context = {'post':post,
                       'form': form,
                       'comment_list':comment_list
            }
            return render(request, 'blog/detail.html', context=context)
        # 如果不是post请求,则说明用户没有提交数据, 重新定向到文章详情页
    return redirect(post)






