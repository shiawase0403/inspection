from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


from django.contrib import admin
from .models import *

from import_export import resources
from .models import Dorminspect

from openpyxl import Workbook
from openpyxl.styles import Font

from .views import download

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

    # def getdatasforteachers(self,request,queryset):
    #     temp= []
    #     for d in queryset:
    #         t = [d.room,str(d.score)]
    #         temp.append(t)
    #     f = open('D://dataforteachers.txt','a')
    #     for t in temp:
    #         f.write(','.join(t)+'\r\n')
    #     f.close
    #     self.message_user(request,'数据导出成功！')
    # getdatasforteachers.short_description = '导出提交给老师的数据'


    def getdataforteachers(self,request,queryset):
        temp = []
        for d in queryset:
            t = [d.room,str(d.score)]
            temp.append(t)
        wb = Workbook()
        ws = wb.create_sheet('mytest', 0)
        start_col = 1
        haha = ['room', 'score']
        for hahaha in haha:
            ws.cell(row=1,column=start_col,value=hahaha)
            start_col += 1
        font = Font(bold=True)
        ws['A1'].font = font
        ws['B1'].font = font
        start_row = 2
        start_col = 1
        init_col = start_col
        for temp2 in temp:
            for each_temp in temp2:
                ws.cell(row=start_row, column=start_col, value=each_temp)
                start_col += 1
            start_row += 1
            start_col = init_col
        SAVE_DIR = BASE_DIR / 'index/static/给老师的数据.xlsx'
        wb.save(SAVE_DIR)
        wb.close
        self.message_user(request, '数据导出成功！')
        return download(request)
    getdataforteachers.short_description = '导出提交给老师的数据-excel'


    actions = ['getdatasforteachers','getdataforteachers']


@admin.register(PersonInfo)
class personinfoadmin(admin.ModelAdmin):
    list_display = ['id','name']