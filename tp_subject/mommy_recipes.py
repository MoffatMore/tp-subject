from django.contrib.sites.models import Site
from edc_base.utils import get_utcnow
from dateutil.relativedelta import relativedelta
from edc_constants.constants import NOT_APPLICABLE, YES, NO, MALE
from .custom_constants import SINGLE
from faker import Faker
from model_mommy.recipe import Recipe, seq
from .models import CommunityEngagement
from tp_screening.models import SubjectScreening
from .models import Education
from .models import Demographic
from .models import SubjectConsent

fake = Faker()

education = Recipe(Education)

demographic = Recipe(
    Demographic,
    marital_status=SINGLE,
    women_num_of_wives=None,
    men_num_of_wives=None,
    currently_living_with='Alone')

community_engagement = Recipe(
    CommunityEngagement,
    activity='Very Active',
    participation_in_election=YES,
    major_problems='Unemployment',
    adult_participation=YES)

subject_screening = Recipe(
    SubjectScreening,
    report_datetime=get_utcnow(),
    gender=MALE,
    age_in_years=25,
    guardian_present=NOT_APPLICABLE,
    citizen=YES,
    married_to_citizen=NOT_APPLICABLE,
    marriage_certificate_present=NOT_APPLICABLE,
    literate=YES,
    literate_witness_present=NOT_APPLICABLE)

subjectconsent = Recipe(
    SubjectConsent,
    assessment_score=YES,
    confirm_identity=seq('12315678'),
    consent_copy=YES,
    consent_datetime=get_utcnow(),
    consent_reviewed=YES,
    dob=get_utcnow() - relativedelta(years=25),
    first_name=fake.first_name,
    gender='M',
    identity=seq('12315678'),
    identity_type='country_id',
    initials='XX',
    is_dob_estimated='-',
    is_incarcerated=NO,
    is_literate=YES,
    last_name=fake.last_name,
    screening_identifier=None,
    study_questions=YES,
    subject_identifier=None)
