from django.contrib import admin
from django.http.request import HttpRequest
from .models import *
from django.utils.html import format_html
from leaflet.admin import LeafletGeoAdmin
from .forms import ResidentAdminForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib import admin
from django.urls import reverse
from django.http import HttpResponseRedirect
from semantic_admin import SemanticModelAdmin, SemanticStackedInline, SemanticTabularInline
import pprint
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session


from django.contrib import admin
from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.urls import reverse
from django.utils.safestring import mark_safe


from django.contrib import admin
from django.contrib.admin.models import LogEntry

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportMixin, ImportExportMixin
from .models import Resident
from .resources import ResidentResource, CaseResource

from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)



class UserMunicipalInline(admin.StackedInline):

    model = UserMunicipal
    can_delete = False
    verbose_name_plural = 'User Municipality'
    

class CustomGroupAdmin(GroupAdmin):

    list_per_page = 7
admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)
        

class CustomUserAdmin(UserAdmin):
    inlines = [UserMunicipalInline]
    list_display = ['username','email','first_name','last_name','is_staff','assigned_municipal']
   
    search_fields = ['username','is_staff']
    def assigned_municipal(self, obj):
        return obj.usermunicipal

    assigned_municipal.short_description = 'Assigned Municipal'
    list_per_page = 7
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class MunicipalAdmin(SemanticModelAdmin, LeafletGeoAdmin):
    
    list_display = ['code', 'municipal','id']
    search_fields = ['municipal']
    list_per_page = 7

admin.site.register(Municipal, MunicipalAdmin)


class BarangayAdmin(LeafletGeoAdmin, SemanticModelAdmin):
    
    list_display = ['code', 'barangay', 'tmp_muni' ,'municipal']
    ordering = ['municipal']
    search_fields = ['barangay','municipal__municipal']
    list_per_page = 7

admin.site.register(Barangay, BarangayAdmin)

 
class SuperuserImportExportModelAdmin(ImportExportModelAdmin):
    def has_export_permission(self, request):
        return request.user.is_superuser


class ResidentAdmin(LeafletGeoAdmin, SemanticModelAdmin, SuperuserImportExportModelAdmin):

    resource_class = ResidentResource

    list_display = ['resident_id', 'first_name', 'last_name','municipal','barangay','created_at','updated_at']
    list_per_page = 7
    list_select_related = ['barangay', 'municipal']
    ordering = ['-updated_at']
    list_filter = ['municipal']
    search_fields = ['resident_id','first_name','last_name', 'barangay__barangay']

admin.site.register(Resident, ResidentAdmin)


class CaseAdmin(SuperuserImportExportModelAdmin, SemanticModelAdmin):
    
    resource_class = CaseResource
    list_per_page = 7
    autocomplete_fields = ['resident']
    list_filter = (('date', DateRangeFilterBuilder()),)
    list_display = ['resident','date', 'dengue_type','created_at','updated_at']
    search_fields = ['resident__resident_id', 'dengue_type', 'resident__barangay__barangay', 'date']
    ordering = ['-date']
    
admin.site.register(Case,CaseAdmin)


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_repr',  
        'action_flag',
    ]

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True
    
    def has_delete_permission(self, request, obj=None):
        return True

