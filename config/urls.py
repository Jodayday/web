from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',          include('core.urls')),       # 홈
    path('downloads/', include('downloads.urls')), # 자료실
    path('blog/',     include('blog.urls')),       # 블로그
    path('support/',  include('support.urls')),    # 원격지원
    path('contact/',  include('contact.urls')),    # 문의
    path('faq/',       include('faq.urls')),         # FAQ
]
