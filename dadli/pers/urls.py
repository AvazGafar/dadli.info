from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^', views.index, name = 'index')
	#url for linking to database
	#url(r'^(?P<obj_id>[0-9]+)$', views.obdata, name = "obdata")
	
]