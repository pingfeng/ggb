from django.db import models

class Message(models.Model):
        title = models.CharField(max_length=50)
        subject = models.CharField(max_length=1000)
        def __unicode__(self): 
	          return self.subject 
