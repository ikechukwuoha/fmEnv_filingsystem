from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File



REGISTRATION_CATEGORY_CHOICES = (
    ('eia', 'EIA'),
    ('esia', 'ESIA'),
    ('eshia', 'ESHIA'),
    ('emp', 'EMP'),
    ('esmp', 'ESMP'),
    ('eshmp', 'ESHMP'),
    ('esmf', 'ESMF'),
    ('rap', 'RAP'),
    ('sea', 'SEA'),
    ('escp', 'ESCP'),
    ('sep', 'SEP'),
    ('lmp', 'LMP'),
    ('rpf', 'RPF'),
    ('grm', 'GRM'),
    ('ipmp', 'IPMP'),

 )

PROJECT_LOCATION_CHOISES = (
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
    ('abia', 'ABIA'),
)


class Project(models.Model): 
    project_name = models.CharField(max_length=550)
    file_no = models.IntegerField()
    reg_cat = models.CharField(max_length=8, choices=REGISTRATION_CATEGORY_CHOICES, default='-------')
    
    