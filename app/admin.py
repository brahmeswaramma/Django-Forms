from django.contrib import admin
from app.models import *

# Register your models here.
class customizeWebpage(admin.ModelAdmin):
    #list_display=['topic_name','name','url']
    #list_display_links=['name']
    #list_editable=['name']
    #list_filter=['name','topic_name']
    #list_max_show_all=1
    #list_per_page=3
    list_select_related=['topic_name']



admin.site.register(Topic)
admin.site.register(Webpage,customizeWebpage)
admin.site.register(AccessRecord)

