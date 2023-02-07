from django.contrib import admin

from .models import Student, ItemA, ItemB, MultiTable, StudentMultiTable


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    list_editable = ['age']


admin.site.register(ItemA)
admin.site.register(ItemB)
admin.site.register(StudentMultiTable)
admin.site.register(MultiTable)
