# blog/views.py

from django.shortcuts import render, get_object_or_404
import markdown


from comments.forms import CommentForm

# 引入Category类

from .models import Post, Category


def index(request):
    # return HttpResponse('欢迎访问我的博客首页')
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={
        'post_list': post_list

    })


def detail(request, pk):
    # 如果存在就传对应id的post,否则返回一个404
    post = get_object_or_404(Post, pk=pk)
    # 在顶部引入markdown 模块
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc'
                                  ])
    # 顶部引入评论表单 CommentForm

    form = CommentForm()
    # 获取这篇文章post下的全部评论
    comment_list = post.comment_set.all()  # 通过外键调取数据,采用树的结构

    # 讲文章、表单、以及文章下的评论列表作为模板变量传给detail.HTML模板, context的作用
    # 从而渲染相应的数据
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
    }

    return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})