from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple

from ..admin_site import tp_subject_admin
from ..forms import DemographicForm
from ..models import Demographic
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(Demographic, site=tp_subject_admin)
class DemographicAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form=DemographicForm

    additional_instructions = (
        'The following questions refer to the demographic background of '
        'the patient.')


admin.site.register(Demographic, DemographicAdmin)
