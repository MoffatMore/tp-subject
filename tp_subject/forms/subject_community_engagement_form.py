#from tp_form_validators import DemographicFormValidator

from ..models import CommunityEngagement
from .form_mixins import SubjectModelFormMixin


class CommunityEngagementForm(SubjectModelFormMixin):

    #form_validator_cls = EducationFormValidator

    class Meta:
        model = CommunityEngagement
        fields = '__all__'
