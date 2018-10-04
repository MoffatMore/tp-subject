from django.test import TestCase, tag
from edc_constants.constants import MALE, YES
from ..custom_constants import SINGLE,MARRIED
from edc_form_validators.base_form_validator import NOT_APPLICABLE_ERROR
from model_mommy import mommy


@tag('tsd')
class TestSubjectDemographic(TestCase):

    def test_subject_demographics_marital_status_single(self):
        subject_demographic = mommy.prepare_recipe(
            'tp_subject.demographic', marital_status=SINGLE)
        self.assertIsNone(subject_demographic.women_num_of_wives)
        self.assertIsNone(subject_demographic.men_num_of_wives)
        self.assertEqual(subject_demographic.marital_status, SINGLE)
        
    def test_subject_demographics_marital_status_married(self):
        subject_demographic = mommy.prepare_recipe(
            'tp_subject.demographic', marital_status=MARRIED, women_num_of_wives=1)
        self.assertEqual(subject_demographic.women_num_of_wives, 1)
        self.assertIsNone(subject_demographic.men_num_of_wives)
        self.assertEqual(subject_demographic.marital_status, MARRIED)