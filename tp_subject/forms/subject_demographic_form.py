#from tp_form_validators import DemographicFormValidator

from ..models import Demographic
from .form_mixins import SubjectModelFormMixin


class DemographicForm(SubjectModelFormMixin):

    #form_validator_cls = EducationFormValidator

    class Meta:
        model = Demographic
        fields = '__all__'
