from django.core.validators import MinValueValidator
from django.db import models
from edc_constants.constants import YES, NO, DWTA, NOT_APPLICABLE
from edc_constants.choices import YES_NO
from tp_subject.custom_constants import EMPLOYMENT_TYPE_CHOICES
from tp_subject.custom_constants import EMPLOYMENT_SECTOR_CHOICES
from tp_subject.custom_constants import INCOME_CHOICES


class EducationModelMixin(models.Model):

    employment_status = models.CharField(
        verbose_name="Are you currently working?",
        max_length=5,
        choices=YES_NO)

    profession = models.CharField(
        verbose_name="In your main job what type of work do you do?",
        max_length=200,
        default=NOT_APPLICABLE,
        choices=EMPLOYMENT_TYPE_CHOICES)

    profession_other = models.CharField(
        verbose_name=('If above is other, what is your profession?'),
        null=True,
        max_length=100,
        help_text="Only applicable if previous answer is 'other'")

    work_description = models.CharField(
        verbose_name="Describe the work that you do or did"
                     "in your most recent job",
        max_length=200,
        default=DWTA,
        choices=EMPLOYMENT_SECTOR_CHOICES,
        help_text="If you have more than one profession, "
                  "choose the one you spend the most time doing.")

    income = models.CharField(
        verbose_name="In the past month, how much money did you earn from work"
                     " you did or received in payment?",
        max_length=50,
        default=DWTA,
        choices=INCOME_CHOICES)

    education_years = models.IntegerField(
        verbose_name='How many years of education did you complete?',
        validators=[MinValueValidator(0)])

    education_certificate = models.CharField(
        verbose_name='What is the your highest education '
        'certificate?',
        max_length=25)

    elementary = models.CharField(
        verbose_name=(
            'Did you go to elementary/primary school?'),
        max_length=5,
        choices=YES_NO)

    attendance_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    secondary = models.CharField(
        verbose_name='Did you go to secondary school?',
        max_length=5,
        choices=YES_NO)

    secondary_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    higher_education = models.CharField(
        verbose_name='Did you go to higher education?',
        max_length=5,
        choices=YES_NO)

    higher_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    class Meta:
        abstract = True
