from django.db import models
from django.contrib import admin
from datetime import datetime
from datetime import date

class DataWIFI(models.Model):
	node_id=models.IntegerField()
	ssid=models.CharField(max_length=40)
	bssid=models.CharField(max_length=40)
	rssi=models.IntegerField()
	channel=models.IntegerField()
	timestamp=models.IntegerField()
	
	
	def __unicode__(self):
		return str(self.node_id)+str(" ")+str(self.ssid)+" "+str(self.timestamp)

class DataWIFIAdmin(admin.ModelAdmin):
	list_display = ('node_id', 'ssid', 'bssid','rssi','channel','timestamp')
	search_fields = ('node_id', 'ssid', 'bssid','channel','rssi','timestamp')
	ordering = ('-timestamp',)
	list_filter = ('node_id','ssid',)
	

class DataTags(models.Model):
	microcontroller_id=models.IntegerField()
	tag_id=models.IntegerField()
	tag_rssi=models.IntegerField()
	timestamp=models.IntegerField()
	
	
	def __unicode__(self):        
		return str(self.microcontroller_id)+str(" ")+str(self.tag_id)+str(" ")+str(self.tag_rssi)+str(" ")+str(self.timestamp)
		
class DataTagsAdmin(admin.ModelAdmin):
	list_display = ('microcontroller_id', 'tag_id', 'tag_rssi','timestamp')
	search_fields = ('microcontroller_id', 'tag_id', 'tag_rssi','timestamp')
	ordering = ('-timestamp',)
	list_filter = ('microcontroller_id','tag_id',)
		
	
