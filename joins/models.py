from django.db import models

class Join(models.Model):
	email = models.EmailField(unique=True)
	# ref_id = models.CharField(max_length=120, default='ABC', unique=True)
	ip_address = models.CharField(max_length=120, default='ABC')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)

	def __unicode__(self):
		return "%s" %(self.email)

	class Meta:
		unique_together = ["email"]
#1) Install south: pip install south, add south to settings.py in INSTALLED APPS
#2) Ensure Model is synced in the database
#3) Convert he model to south with: python manage.py convert_to_south appname
#4) Make changes to model (eg add new fields: ip_address = models.CharField(max_length=120, default='ABC'))
#5) Run schemamigration: python manage.py schemamigration appname --auto_now
#6) Run migrate: python manage.py migrate 