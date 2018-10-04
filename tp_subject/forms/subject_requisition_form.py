from django import forms
from django.core.exceptions import ObjectDoesNotExist
from edc_constants.constants import YES, NO
#from edc_lab.forms import RequisitionFormMixin
from edc_metadata.constants import NOT_REQUIRED

from ..models import SubjectRequisition
from .form_mixins import SubjectModelFormMixin


class SubjectRequisitionForm(SubjectModelFormMixin): #RequisitionFormMixin):

#     requisition_identifier = forms.CharField(
#         label='Requisition identifier',
#         widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('reason_not_drawn') == NOT_REQUIRED:
            pass
        return cleaned_data

    class Meta:
        model = SubjectRequisition
        fields = '__all__'
