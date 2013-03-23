from Tags.models import DataTags
from Tags.models import DataTagsAdmin
from Tags.models import DataWIFI
from Tags.models import DataWIFIAdmin
from django.contrib import admin

admin.site.register(DataTags,DataTagsAdmin)
admin.site.register(DataWIFI,DataWIFIAdmin)

