from django.db import models
from social_django.models import UserSocialAuth


class Objinfo(models.Model):
	objt = models.CharField(max_length = 250)
	adres = models.CharField(max_length = 250, default = 'NULL')
	erazi = models.CharField(max_length = 250, default = 'NULL')
	metro = models.CharField(max_length = 250, default = 'NULL')
	city_reg = models.CharField(max_length = 250, default = 'NULL')
	city = models.CharField(max_length = 250, default = 'NULL')
	country = models.CharField(max_length = 250, default = 'NULL')
	zip = models.CharField(max_length = 10, default = 'NULL')
	fammeal = models.CharField(max_length = 100, default = 'NULL')
	menu = models.CharField(max_length = 5000, default = 'NULL')
	delivery = models.BooleanField(default = False)
	tel1 = models.CharField(max_length = 14, default = 'NULL')
	tel2 = models.CharField(max_length = 14, default = 'NULL')
	tel3 = models.CharField(max_length = 14, default = 'NULL')
	mob1 = models.CharField(max_length = 14, default = 'NULL')
	mob2 = models.CharField(max_length = 14, default = 'NULL')
	mob3 = models.CharField(max_length = 14, default = 'NULL')
	mob4 = models.CharField(max_length = 14, default = 'NULL')
	mob5 = models.CharField(max_length = 14, default = 'NULL')
	info = models.TextField(max_length = 5000, default = 'NULL')
	pic0 = models.URLField(max_length = 1000, default = 'NULL')
	pic1 = models.URLField(max_length = 1000, default = 'NULL')
	pic2 = models.URLField(max_length = 1000, default = 'NULL')
	pic3 = models.URLField(max_length = 1000, default = 'NULL')
	pic4 = models.URLField(max_length = 1000, default = 'NULL')
	pic5 = models.URLField(max_length = 1000, default = 'NULL')
	pic6 = models.URLField(max_length = 1000, default = 'NULL')
	pic7 = models.URLField(max_length = 1000, default = 'NULL')
	pic8 = models.URLField(max_length = 1000, default = 'NULL')
	pic9 = models.URLField(max_length = 1000, default = 'NULL')

	def __str__(self):
		return self.city + " - " + self.erazi + " - " + self.objt
	
		
	
	
	
class Cats(models.Model):
	cat_az = models.CharField(max_length = 50, default = 'NULL')
	cat_en = models.CharField(max_length = 50, default = 'NULL')
	cat_ru = models.CharField(max_length = 50, default = 'NULL')
	cat_tr = models.CharField(max_length = 50, default = 'NULL')
	cat_ar = models.CharField(max_length = 50, default = 'NULL')
	
	def __str__(self):
		return self.cat_az

		
		
	
class Catobj(models.Model):
	objid = models.ForeignKey(Objinfo, on_delete = models.CASCADE)
	catid = models.ForeignKey(Cats, on_delete = models.CASCADE)
	
	def __str__(self):
		return str(self.objid) + " - " + str(self.catid)
	
	
	
	
class Tags(models.Model):
	tagaz = models.CharField(max_length = 100, default = 'NULL')
	tagru = models.CharField(max_length = 100, default = 'NULL')
	tagen = models.CharField(max_length = 100, default = 'NULL')
	tagtr = models.CharField(max_length = 100, default = 'NULL')
	tagar = models.CharField(max_length = 100, default = 'NULL')
	
	def __str__(self):
		return self.tagaz
	


	
class Tagobj(models.Model):
	objid = models.ForeignKey(Objinfo, on_delete = models.CASCADE)
	tagid = models.ForeignKey(Tags, on_delete = models.CASCADE)
	
	def __str__(self):
		return str(self.objid) + " - " + str(self.tagid)
	


class Ustags(models.Model):
	object = models.ForeignKey(Objinfo, on_delete = models.CASCADE)
	user = models.ForeignKey(UserSocialAuth,on_delete = models.CASCADE)
	tag = models.CharField(max_length = 100)

	def __str__(self):
		return str(self.object) + " - " + self.tag
