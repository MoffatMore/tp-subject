'''
Created on 03 Oct 2018

@author: moffatmore
'''
from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple

from ..admin_site import tp_subject_admin
from ..forms import EducationForm
from ..models import Education
from .modeladmin_mixins import CrfModelAdminMixin
from ..models import EducationHoh


@admin.register(EducationHoh, site=tp_subject_admin)
class EducationHohAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = EducationForm

    additional_instructions = (
        'The following questions refer to the educational background of '
        'the patient.')

    fieldsets = (
        (None, {
            'fields': [
                'subject_visit',
                'report_datetime',
                'profession',
                'education_years',
                'education_certificate',
                'elementary',
                'attendance_years',
                'secondary',
                'secondary_years',
                'higher_education',
                'higher_years',
                'household_head']}
         ), audit_fieldset_tuple)

    radio_fields = {
        'elementary': admin.VERTICAL,
        'secondary': admin.VERTICAL,
        'higher_education': admin.VERTICAL}


admin.site.register(EducationHoh, EducationHohAdmin)
