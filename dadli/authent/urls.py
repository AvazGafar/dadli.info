'''
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^', include('dadli.urls')),
    url(r'^account/', include('social_django.urls', namespace='social')),
    url(r'^account/', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^admin/', include(admin.site.urls)),
]
'''
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index ),
    url(r'^profile/$', views.update_profile),
    url(r'^account/logout/$', views.Logout),
]