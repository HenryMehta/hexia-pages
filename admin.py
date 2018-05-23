from django.contrib import admin

from hexia_pages.models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name',]
    #readonly_fields = ['name']

    def get_actions(self, request):
        actions = super(PageAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
    #def has_delete_permission(self, request, obj=None):
        return False

    #def has_add_permission(self, request):
        return False
        
admin.site.register(Page, PageAdmin)