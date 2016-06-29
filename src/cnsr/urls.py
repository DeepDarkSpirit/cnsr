"""cnsr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib import admin
admin.autodiscover()
from django.conf.urls import patterns,include,url
from main  import views
from django.conf import settings
from django.conf.urls.static import static
#####

urlpatterns = patterns('',

    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT }),  
    url(r'^$', views.shouye),
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', views.hello),
    url(r'^benke/$', views.benke),
    url(r'^boshi/$', views.boshi),
    url(r'^gonggongxiaoxi/$', views.gonggongxiaoxi),
    url(r'^guojihezuo/$', views.guojihezuo),
    url(r'^jiaoxuechengguo/$', views.jiaoxuechengguo),
    url(r'^jiaoxuelunwen/$', views.jiaoxuelunwen),
    url(r'^jiaoxuejiaocai/$', views.jiaoxuejiaocai),
    url(r'^jiaoxuejiaogai/$', views.jiaoxuejiaogai),
    url(r'^jiaoxuegongzuo/$', views.jiaoxuegongzuo),
    url(r'^keyanchengguo/$', views.keyanchengguo),
    url(r'^keyanlunwen/$', views.keyanlunwen),
    url(r'^keyanzhuanli/$', views.keyanzhuanli),
    url(r'^keyanzhuzuoquan/$', views.keyanzhuzuoquan),
    url(r'^keyangongzuo/$', views.keyangongzuo),
    url(r'^lianxiwomen/$', views.lianxiwomen),
    url(r'^login/$', views.login),
    url(r'^liuxuesheng/$', views.liuxuesheng),
    url(r'^shiyanshijianjie/$', views.shiyanshijianjie),
    url(r'^shiziduiwu/$', views.shiziduiwu),
    url(r'^shouye/$', views.shouye),
    url(r'^shuoshi/$', views.shuoshi), 
    url(r'^tongzhi/(.+)/$', views.tongzhi),
    url(r'^tianjiadongtaixiaoxi/$', views.tianjiadongtaixiaoxi),
    url(r'^tianjiajiaoxuegongzuo/$', views.tianjiajiaoxuegongzuo),
    url(r'^tianjiakeyangongzuo/$', views.tianjiakeyangongzuo),
    url(r'^tianjiachengguo/$', views.tianjiachengguo),
    url(r'^tongzhitonggao/$', views.tongzhitonggao),
    url(r'^xiaoxi/$', views.xiaoxi),
    url(r'^xinwendongtai/$', views.xinwendongtai),
    url(r'^xueshengxinxi/$', views.xueshengxinxi),
    url(r'^xueshuhuodong/$', views.xueshuhuodong),
    url(r'^current_datetime/$', views.current_datetime),
    url(r'^addNewsResualt/$', views.addNewsResualt),
    url(r'^addKeyanResualt/$', views.addKeyanResualt),
    url(r'^addStudentResualt/$', views.addStudentResualt),
    url(r'^addTeacherResualt/$', views.addTeacherResualt),
    url(r'^addCourseResualt/$', views.addCourseResualt), 
    url(r'^addAchievementResualt/$', views.addAchievementResualt), 
    url(r'^deleNews/$', views.deleNews),  
    url(r'^editNews/$', views.editNews),   
    url(r'^editNewsResult/$', views.editNewsResult),   
    url(r'^quanxianguanli/$', views.quanxianguanli),   
    url(r'^xueshengguanli/$', views.xueshengguanli),     
    url(r'^jiaoshiguanli/$', views.jiaoshiguanli),   
    url(r'^delTeacher/(.+)/$', views.delTeacher), 
    url(r'^delStudent/(.+)/$', views.delStudent),    
    url(r'^tianjiaquanxianguanli/(.+)/(.+)/$', views.tianjiaquanxianguanli),  
    url(r'^tianjiajiaoshi/$', views.tianjiajiaoshi),  
    url(r'^tianjiaxuesheng/$', views.tianjiaxuesheng),   
#     url(r'^quanxianguanliResult/(.+)/(.+)/$', views.quanxianguanliResult),  
    url(r'^quanxianguanliResult/$', views.quanxianguanliResult), 
    url(r'^baobiaotongji/$', views.baobiaotongji),  
    url(r'^chart/$', views.chart),   
) 
