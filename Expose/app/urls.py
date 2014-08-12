from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'home$', views.home, name='home'),
    url(r'login$', views.login, name='login'),
    url(r'specific$', views.specific, name = 'specific'),
    url(r'about$', views.about, name = 'about'),
    url(r'signup$', views.signup, name = 'signup'),
    url(r'articles$', views.articles, name= 'articles'),
    url(r'donate$', views.donate, name= 'donate'),
    url(r'welcome$', views.welcome, name= 'welcome'),
    url(r'specific2$', views.specific2, name= 'specific2'),
)


