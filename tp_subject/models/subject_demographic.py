from django.db import models
from ..custom_constants import MARITAL_CHOICES, LIVING_WITH_CHOICES
from .model_mixins import CrfModelMixin

class Demographic(CrfModelMixin):

    marital_status = models.CharField(
        verbose_name='What is the subject\'s marital status',
        max_length=10,
        default="Single",
        choices=MARITAL_CHOICES)

    women_num_of_wives = models.IntegerField(
        verbose_name="Women: How many wives does your husband have?",
        null=True,
        help_text='Including traditional marriage, including yourself.'
                  'Applicable to married women only')

    men_num_of_wives = models.IntegerField(
        verbose_name="Men: How many wives does you have?",
        null=True,
        help_text='Including traditional marriage.'
                  'Applicable to married men only')

    currently_living_with = models.CharField(
        verbose_name="Who do you currently live with?",
        choices=LIVING_WITH_CHOICES,
        max_length=50)
