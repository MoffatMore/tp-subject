from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple

from ..admin_site import tp_subject_admin
from ..forms import CommunityEngagementForm
from ..models import CommunityEngagement
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(CommunityEngagement, site=tp_subject_admin)
class CommunityEngagementAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form=CommunityEngagementForm

    additional_instructions = (
        'The following questions refer to the community engagement of '
        'the patient.')


admin.site.register(CommunityEngagement, CommunityEngagementAdmin)
