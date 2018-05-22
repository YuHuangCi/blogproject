
from django.conf.urls import url, include
from django.contrib import admin

# 区分大小写
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('blog.urls')),
    url(r'',include('comments.urls')),
]
