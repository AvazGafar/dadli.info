from django.contrib import admin

from .models import Objinfo, Cats, Catobj, Tags, Tagobj
#Ustags

admin.site.register(Objinfo)
admin.site.register(Cats)
admin.site.register(Catobj)
admin.site.register(Tags)
admin.site.register(Tagobj)
#admin.site.register(Ustags)

