from django.contrib import admin
from .models import User_Record

class UserRecordAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'gender')
    search_fields = ('username', )
    

admin.site.register(User_Record, UserRecordAdmin)