from django.contrib import admin
from . models import User


@admin.register(User)
class PersonAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('timestamp', 'ic_no', 'name')
        return self.readonly_fields
    pass


