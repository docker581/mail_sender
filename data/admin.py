from django.contrib import admin

from .models import Layout, Subscriber


class LayoutAdmin(admin.ModelAdmin):
    list_display = ('head', 'greeting', 'text', 'signature')
    search_fields = ('last_name',)


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')
    search_fields = ('head',)    


admin.site.register(Layout, LayoutAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
