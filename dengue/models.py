from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import GEOSGeometry
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator



class Municipal(models.Model):
    municipal = models.CharField(max_length=80)
    code = models.CharField(max_length=11, unique=True)
    geom = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.municipal
    
class UserMunicipal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    municipal = models.ForeignKey(Municipal, on_delete=models.CASCADE, help_text="If not superuser", null=True, blank=True)
    
    def __str__(self):
        return str(self.municipal)


def validate_single_digit(value):
    if value < 0 or value > 9:
        raise ValidationError('Value must be a single digit (0-9).')
    
    
class Barangay(models.Model):
    barangay = models.CharField(max_length=80)
    municipal = models.ForeignKey(Municipal, on_delete=models.CASCADE)
    code = models.CharField(max_length=80)
    tmp_muni = models.CharField(max_length=80)
    longitude = models.FloatField()
    latitude = models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)
    is_auto_arima = models.BooleanField(default=True, verbose_name='Use Auto ARIMA', help_text="Checking this will use Auto ARIMA and ignore all the inputs below")
    ar = models.IntegerField(validators=[ MaxValueValidator(9),  MinValueValidator(0), validate_single_digit,], verbose_name='AR(p)', default=0)
    i = models.IntegerField(validators=[ MaxValueValidator(9),  MinValueValidator(0), validate_single_digit,], verbose_name='I(d)', default=0)
    ma = models.IntegerField(validators=[ MaxValueValidator(9),  MinValueValidator(0), validate_single_digit,], verbose_name='MA(q)', default=0)
    is_seasonal = models.BooleanField(default=False, verbose_name='Use Seasonal ARIMA', help_text="Checking this will use the Seasonal ARIMA")
    seasonal_ar = models.IntegerField(validators=[ MaxValueValidator(9),  MinValueValidator(0), validate_single_digit,], verbose_name='Seasonal AR(P)', default=0)
    seasonal_i = models.IntegerField(validators=[ MaxValueValidator(9),  MinValueValidator(0), validate_single_digit,], verbose_name='Seasonal I(D)', default=0)
    seasonal_ma = models.IntegerField(validators=[ MaxValueValidator(9),  MinValueValidator(0), validate_single_digit,], verbose_name='Seasonal MA(Q)', default=0)
    
    def __str__(self):
        return f"{self.barangay}, {self.municipal}"

class Resident(models.Model):
    resident_id = models.CharField(max_length=11, unique=True,verbose_name="Residence ID")
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20)
    suffix = models.CharField(max_length=3, choices=(
        ('Sr', 'Sr'),
        ('Jr', 'Jr'),
        ('II','II'),
        ('III','III'),
        ('IV','IV'),
    ),blank=True, null=True, help_text="(Optional)")
    municipal = models.ForeignKey(Municipal, on_delete=models.CASCADE, verbose_name='Municipal')
    barangay = models.ForeignKey(Barangay, on_delete=models.CASCADE,verbose_name='Barangay')
    street = models.CharField(max_length=100, null=True, blank=True,help_text="(Optional)")
    birth_date = models.DateField(help_text="Date format: YYYY-MM-DD example: (2000-01-06)")
    sex = models.CharField(max_length=6, choices= (
        ('Male', 'Male'),
        ('Female', 'Female'),
    ),verbose_name='Sex')
    latitude = models.FloatField(blank=True, null=True,help_text="Enter latitude here (e.g. 37.7749)(Optional)")
    longitude = models.FloatField(blank=True, null=True,help_text="Enter longitude here (e.g. 37.7749)(Optional)")
    geom = gis_models.PointField(srid=4326,blank=True, null=True, help_text="Note: If you want to use the Map make sure to empty the Longitude and Latitude!")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def clean(self):
        if not (self.latitude or self.longitude or self.geom):
            raise ValidationError('Please provide a location.')
        if self.latitude and not self.longitude:
            raise ValidationError('Please provide a longitude.')
        if not self.latitude and self.longitude:
            raise ValidationError('Please provide a latitude.')

        if len(self.resident_id) < 11:
            raise ValidationError('Resident ID must be 11 characters long')
        
        if self.barangay and self.barangay.municipal != self.municipal:
            raise ValidationError("Barangay does not belong to the selected municipal")
        
        
    def save(self, *args, **kwargs):
    
        self.first_name = self.first_name.title()
        
        self.last_name = self.last_name.title()
        
        if self.middle_name is not None:
            self.middle_name = self.middle_name.title()
        
        if self.street is not None:
            self.street = self.street.title()
        
        if self.geom is not None and self.latitude is None and self.longitude is None:
            self.latitude = self.geom.y
            self.longitude = self.geom.x
           
        elif self.latitude is not None and self.longitude is not None:
            point = Point(self.longitude, self.latitude)
            self.geom = GEOSGeometry(point.wkt)
        super(Resident, self).save(*args, **kwargs)
    
        
    def __str__(self):
        return f"{self.resident_id} ({self.first_name} {self.last_name})"
    


class Case(models.Model):
    date = models.DateField(verbose_name='Date', help_text="Date format: YYYY-MM-DD example: (2000-01-06)")
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='resident')
    dengue_type = models.CharField(max_length=5,choices= (
        ('DENV1', 'DENV1'),
        ('DENV2', 'DENV2'),
        ('DENV3', 'DENV3'),
        ('DENV4', 'DENV4'),
    ),verbose_name='Dengue Type')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.resident}"