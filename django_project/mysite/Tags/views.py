from django.http import HttpResponse
from Tags.models import DataTags
from Tags.models import DataWIFI

from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import datetime

'''Allow Post Requests from cross origin'''
@csrf_exempt
def index(request):
	
	#Get the raw HTTP request
	a=str(request.raw_post_data)
	#Split the request by newline
	b=a.split("\n")
	for line in b:
		#Split each line by comma
		c=line.split(",")
		#If line has more than 3 attributes, i.e. line is not empty
		if len(c)>3:
			#If first attribute is 1, we have TAGS data, else we have WiFi data
			if int(c[0])==1:
				print a
				
				try:
					t=DataTags(microcontroller_id=int(c[1]),tag_id=int(c[2]),tag_rssi=int(c[3]),timestamp=int(c[4]))
					t.save()
				except:
					pass
			else:
				
				try:
					t=DataWIFI(node_id=int(c[1]),ssid=c[2],bssid=c[3],rssi=int(c[4]),channel=int(c[5]),timestamp=int(c[6]))
					t.save()
				except:
					pass
	return HttpResponse(" ")
