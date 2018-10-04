from django.test import TestCase, tag
from edc_constants.constants import MALE, YES
from edc_form_validators.base_form_validator import NOT_APPLICABLE_ERROR

@tag('TSE')
class TestSubjectEducation(TestCase):

    """ Assert that subject currently employed has profession selected"""
    def test_eligible_for_education_with_employed_recipe_criteria(self):
        pass
#         subject_education = mommy.prepare_recipe(
#             'tp_subject.education',
#             employment_status=YES, profession='Wage-FT')
#         self.assertIsNotNone(subject_education.profession, False)
