from django.db import models
from edc_constants.choices import YES_NO_NA_DWTA
from ..custom_constants import CE_ACTIVITY_CHOICES, MAJOR_PROBLEMS_CHOICES
from edc_constants.constants import YES, NO, NOT_APPLICABLE, DWTA
from .model_mixins import CrfModelMixin


class CommunityEngagement(CrfModelMixin):

    activity = models.CharField(
        max_length=30,
        verbose_name='How active are you in community activities?',
        choices=CE_ACTIVITY_CHOICES,
        help_text="Community activities such as: burial society, Syndicate,"
                  "PTA, VDC(Village Developement Committee), Mophato and "
                  "development of the community that surrounds you?"
        )

    participation_in_election = models.CharField(
        max_length=5,
        choices=YES_NO_NA_DWTA,
        verbose_name='Did you vote in the last local government election?')

    major_problems = models.CharField(
        max_length=15,
        choices=MAJOR_PROBLEMS_CHOICES,
        verbose_name='What are the major problems in this neighbourhood?')

    adult_participation = models.CharField(
        max_length=5,
        choices=YES_NO_NA_DWTA,
        verbose_name='If there is a problem in this neighborhood, do the '
                     'adults work together in solving it?')
