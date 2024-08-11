from django.contrib import admin
from .models import *

from import_export import resources
from .models import Dorminspect

admin.site.site_title = '纪检统分系统'
admin.site.site_header = '纪检统分系统后台'



# Register your models here.
@admin.register(Dorminspect)
class DorminspectAdmin(admin.ModelAdmin):
    list_display = ['id','person','room','add_date','score']
    list_filter = ['add_date']
    search_fields = ['room']
    readonly_fields = ['score']
    ordering = ['room']

    def getdatasforteachers(self,request,queryset):
        temp= []
        for d in queryset:
            t = [d.room,str(d.score)]
            temp.append(t)
        f = open('D://dataforteachers.txt','a')
        for t in temp:
            f.write(','.join(t)+'\r\n')
        f.close
        self.message_user(request,'数据导出成功！')
    getdatasforteachers.short_description = '导出提交给老师的数据'
    actions = ['getdatasforteachers']

@admin.register(PersonInfo)
class personinfoadmin(admin.ModelAdmin):
    list_display = ['id','name']