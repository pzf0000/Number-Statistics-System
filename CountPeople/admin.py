from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pwd')


class classAdmin(admin.ModelAdmin):
    list_display = ('name',)


class itemAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'number')


admin.site.register(user, UserAdmin)
admin.site.register(item, itemAdmin)
admin.site.register(student_class, classAdmin)
admin.site.site_header = '系统管理'
admin.site.site_title = '系统管理'
