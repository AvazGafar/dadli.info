from django.shortcuts import render
from .models import Objinfo as d1, Cats, Catobj, Tags, Tagobj

def index(request):
	ob = d1.objects.all()
	context = {"ob": ob}
	return render(request, 'pers/home.html', context)
	

#def obdata(request, obj_id):
#	return str(obj_id)
	