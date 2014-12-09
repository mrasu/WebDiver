from django.contrib import admin

# Register your models here.
from viewer.models import WebPage, NewDiscoverLink, NewDiscover, VisitedLink, IgnoreLink

admin.site.register(WebPage)
admin.site.register(VisitedLink)
admin.site.register(NewDiscover)
admin.site.register(NewDiscoverLink)
admin.site.register(IgnoreLink)