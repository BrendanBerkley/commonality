from django.contrib import admin
from commonality.models import Need, TypeOfNeed

class NeedAdmin(admin.ModelAdmin):
	list_display = ('title', 'type_of_need', 'need_expires')

admin.site.register(Need, NeedAdmin)
admin.site.register(TypeOfNeed)