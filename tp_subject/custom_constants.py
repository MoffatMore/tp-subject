from edc_constants.constants import DWTA, NOT_APPLICABLE, OTHER
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, MISSED_VISIT

NOT_REQUIRED = 'Not required'
SINGLE = 'Single'
MARRIED = 'Married'

"""
    Choices for demographics
"""
MARITAL_CHOICES = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Widowed', 'Widowed'),
)

LIVING_WITH_CHOICES = (
        ('Alone', 'Alone'),
        ('Partner/Spouse', 'Partner or Spouse'),
        ('Siblings', 'Siblings'),
        ('Other', 'Other'),
        (DWTA, DWTA)
)


"""
    Choices for education
"""
EMPLOYMENT_TYPE_CHOICES = (
        ('Occasional', 'Occasional or Casual employment (piece job)'),
        ('Seasonal', 'Seasonal employment'),
        ('Wage-FT', 'Formal wage employment (full-time)'),
        ('Wage-PT', 'Formal wage employment (part-time)'),
        ('Se-AGR', 'Self-employed in agriculture'),
        ('Se-FT', 'Self-employed making money, full time'),
        ('Se-PT', 'Self-employed making money, part time'),
        (DWTA, DWTA),
        ('Other', 'Other')
)

EMPLOYMENT_SECTOR_CHOICES = (
    ('Farm', 'Farmer (own land)'),
    ('Farm-OL', 'Farm work on employers land'),
    ('Domestic work', 'Domestic worker'),
    ('B/H/GH/EV', 'Work in bar/ hotel/ guest house/ entertainment venue'),
    ('Fishing', 'Fishing'),
    ('mining', 'Mining'),
    ('TOURITourismSM', 'Tourism/ game parks'),
    ('Shop/SB', 'Working in shop / small business'),
    ('Inf-Selling', 'Informal selling'),
    ('CSW', 'Commercial sex work'),
    ('Transport', 'Transport (trucker/ taxi driver)'),
    ('Factory', 'Factory worker'),
    ('Security Guard', 'Guard (security company)'),
    ('Police/Soldier', 'Police/ Soldier'),
    ('Clerical', 'Clerical and office work'),
    ('Government', 'Government worker'),
    ('Teacher', 'Teacher'),
    ('Health Care', 'Health care worker'),
    ('DNA', 'Don\'t want to answer'),
    ('Other', 'Other Profession')
)

INCOME_CHOICES = (
    ('No Income', 'No Income'),
    ('1-199', '1 - 199 Pula'),
    ('200-499', '200 - 499 Pula'),
    ('500-999', '500 - 999 Pula'),
    ('1000-4999', '1000 - 4999 Pula'),
    ('5000-10,000', '5000 - 10,000 Pula'),
    ('>10,000', 'More than 10,000 Pula'),
    (DWTA, DWTA)
)


"""
    Choices for community engagement
"""
MAJOR_PROBLEMS_CHOICES = (
    ('HIV', 'HIV'),
    ('Schools', 'Schools'),
    ('Sewer', 'Sewer'),
    ('Unemployment', 'Unemployment'),
    ('Roads', 'Roads'),
    ('Water', 'Water'),
    ('Other', 'Other (Specify)'),
    ('House', 'House'),
    ('Malaria', 'Malaria'),
)

CE_ACTIVITY_CHOICES = (
    ('Very Active', 'Very Active'),
    ('Somewhat Active', 'Somewhat Active'),
    ('Not Active At All', 'Not Active At All'),
    (DWTA, DWTA)
)


"""
    Choices for requisition
"""
REASON_NOT_DRAWN = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('collection_failed', 'Tried, but unable to obtain sample from patient'),
    ('absent', 'Patient did not attend visit'),
    ('refused', 'Patient refused'),
    ('no_supplies', 'No supplies'),
    (NOT_REQUIRED, 'No longer required for this visit'),
    (OTHER, 'Other'),
)

INFO_SOURCE = (
    ('hospital_notes', 'Hospital notes'),
    ('outpatient_cards', 'Outpatient cards'),
    ('patient', 'Patient'),
    ('collateral_history',
     'Collateral History from relative/guardian'),
    (OTHER, 'Other'),
)

VISIT_REASON = (
    (SCHEDULED, 'Scheduled'),
    (UNSCHEDULED, 'Not scheduled'),
    (MISSED_VISIT, 'Missed'),
)

VISIT_UNSCHEDULED_REASON = (
    ('patient_unwell_outpatient', 'Patient unwell (outpatient)'),
    ('recurrence_symptoms', 'Recurrence of symptoms'),
    ('raised_icp_management', 'Raised ICP management'),
    ('art_initiation', 'ART initiation'),
    ('patient_hospitalised', 'Patient hospitalised'),
    (OTHER, 'Other'),
    (NOT_APPLICABLE, 'Not applicable'),
)

ID_TYPE = (
    ('country_id', 'Country ID number'),
    ('drivers', 'Driver\'s license'),
    ('passport', 'Passport'),
    ('hospital_no', 'Hospital number'),
    ('country_id_rcpt', 'Country ID receipt'),
    (OTHER, 'Other'),
)

