'''
Created on Jul 12, 2018

@author: moffat
'''
from django.test import TestCase,tag
from model_mommy import mommy
from edc_constants.constants import YES, NO
from tp_screening.models.subject_screening import SubjectScreening

@tag('tsce')
class TestSubjectCommunityEngagement(TestCase):
    
    def setUp(self):
        self.subject_community_engagement = mommy.prepare_recipe(
            'tp_subject.community_engagement'
            )
    
    def test_subject_community_engagement_active(self):
        self.assertEqual(self.subject_community_engagement.activity,'Very Active')
        
    def test_subject_community_engagement_not_active(self):
        options = self.subject_community_engagement
        options.activity = 'Not Active At All'
        self.assertNotEqual(options.activity,'Very Active')
        
    def test_subject_community_engagement_active_sometimes(self):
        options = self.subject_community_engagement
        options.activity = 'Active Sometimes'
        self.assertNotEqual(options.activity,'Active')
        
    
