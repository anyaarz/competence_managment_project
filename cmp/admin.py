from django.contrib import admin
from .models import Employee,Job,Knowledge,Proficiency,Skills
'''
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('job','education', 'birth_date', 'department', 'date_applyied', 'date_retired','location')
    list_filter = ('job','education', 'birth_date', 'department',)
    search_fields = ('job','education','department')

class JobAdmin(admin.ModelAdmin):
    list_display = ('name','discription', 'is_active', 'knowledge', 'proficiency', 'skills')
    list_filter = ('name','is_active', 'knowledge', 'proficiency', 'skills')
    search_fields = ('name','knowledge', 'proficiency', 'skills')
class KnoweledgeAdmin(admin.ModelAdmin):
    list_display = ('name_zun','discription')
    list_filter = ('name_zun','discription')
    search_fields = ('name_zun','discription')
class ProficiencyAdmin(admin.ModelAdmin):
    list_display = ('name_zun','discription')
    list_filter = ('name_zun','discription')
    search_fields = ('name_zun','discription')
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name_zun','discription')
    list_filter = ('name_zun','discription')
    search_fields = ('name_zun','discription')
'''
admin.site.register(Employee)
admin.site.register(Job)
admin.site.register(Knowledge)
admin.site.register(Proficiency)
admin.site.register(Skills)

