"""dadli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
#from . views import home

#urlpatterns = [
    #url(r'^', include('authent.urls')),
    #url(r'^account/', include('social_django.urls', namespace='social')),
    #url(r'^account/', include('django.contrib.auth.urls', namespace='auth')),

    #url(r'^admin/', include(admin.site.urls)),
#]
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^comp1/', include('comp1.urls')), #asagidan
    url(r'^$', include('pers.urls')), #asagidan
    url(r'^i18n/', include('django.conf.urls.i18n')), #for multi-language
    url(r'^', include('authent.urls')), #yuxaridan
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    #url(r'^settings/$', settings, name='settings'),
    #url(r'^settings/password/$', password, name='password'),
]

    #url(r'^$', home, name='home'),


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
    #url(r'^$', core_views.home, name='home'),


    #url(r'^login/$', auth_views.login, name='login'),
    #url(r'^logout/$', auth_views.logout, name='logout'),

    #url(r'^account/', include('django.contrib.auth.urls', namespace='auth')),#yuxaridan

     # <--


# bu hisseden sonrasi muellim yazandi
#from django.conf.urls import url, include
#from django.contrib import admin
#from django.conf.urls.i18n import i18n_patterns  # for multi-language
#from django.utils.translation import ugettext_lazy as _  # for multi-language

# from django.contrib.auth import views as auth_views
# from dadli.core import views as core_views

#urlpatterns = [

#muellimyazan
    #url(r'^admin/', admin.site.urls),
    #url(r'^comp1/', include('comp1.urls')),
    #url(r'^$', include('pers.urls')),
    #url(r'^i18n/', include('django.conf.urls.i18n')),  # for multi-language


    # lenmis
    # url(r'^$', core_views.home, name='home'),
    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^oauth/', include('social_django.urls', namespace='social')),
    # url(r'', views.index),
#]

# urlpatterns += i18n_patterns(

# _(r'^dual-lang/'), include('duallang.urls')),
# (r'^', include('home.urls')),
# url(_(r'^$'), include('pers.urls')),
# url(_(r'^comp1/'), include('comp1.urls')),
# url(_(r'^oauth/'), include('social_django.urls', namespace='social')),
# )