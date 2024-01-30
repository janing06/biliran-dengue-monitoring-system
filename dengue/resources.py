from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Resident, Barangay, Case, Municipal
from django.core.exceptions import ValidationError


class ResidentResource(resources.ModelResource):
    
    
    municipal = fields.Field(
        column_name='municipal',
        attribute='municipal',
        widget=ForeignKeyWidget(Municipal, field='municipal'))
    
    barangay = fields.Field(
        column_name='barangay_code',
        attribute='barangay',
        widget=ForeignKeyWidget(Barangay, field='code'))
    
    
    class Meta:
        model = Resident
        fields = ['id','resident_id','first_name', 'last_name','suffix','municipal','barangay','street','birth_date','sex','latitude','longitude']
  
        
    def before_import_row(self, row, **kwargs):
        # Check if the selected barangay belongs to the selected municipal
        municipal_id = row['municipal'].strip().title()
        barangay_id = row['barangay_code']
        
        print(municipal_id)
        print(barangay_id)
        
       
    

        try:
            
            if 'sex' in row:
                sex_value = row['sex'].strip().lower()
                if sex_value not in ('male', 'female'):
                    raise ValidationError('Invalid value for sex. It should be "Male" or "Female".')
                row['sex'] = row['sex'].title()
                

            if 'suffix' in row and row['suffix']:
                suffix_value = row['suffix'].lower()
                if suffix_value not in ('jr','sr','ii','iii','iv'):
                    raise ValidationError('Invalid value for suffix. It should be "Jr" or "Sr" or "II" or "III" or "IV".')
                row['suffix'] = row['suffix'].title()
            
            if 'first_name' in row and row['first_name']:
                row['first_name'] = row['first_name'].title()
            if 'last_name' in row and row['last_name']:
                row['last_name'] = row['last_name'].title()
            if 'municipal' in row and row['municipal']:
                row['municipal'] = row['municipal'].title()
            
                
            selected_barangay = Barangay.objects.get(code=barangay_id)
            selected_municipal = Municipal.objects.get(municipal=municipal_id)
            if selected_barangay.municipal.id != selected_municipal.id:  # Compare with the municipal field from the row
                print('Barangay does not belong to the selected municipal.')
                raise ValidationError('Barangay does not belong to the selected municipal.')
            
                
        except Barangay.DoesNotExist:
            print('Barangay does not belong to the selected municipal.')
            raise ValidationError('Invalid barangay selected.')

        # Add more custom validation rules as needed

    def import_row(self, row, instance_loader, **kwargs):
        # Perform any additional import processing here if needed
        return super().import_row(row, instance_loader, **kwargs)

class CaseResource(resources.ModelResource):
     
    resident = fields.Field(
        column_name='resident',
        attribute='resident',
        widget=ForeignKeyWidget(Resident, field='resident_id'))
    
    export_order = ('date', 'dengue_type')
    
    class Meta:
        model = Case
        fields = ['id','date','resident','dengue_type']
        
    def before_import_row(self, row, **kwargs):
    
        if 'dengue_type' in row:
            dengue_type_value = row['dengue_type'].lower()
            if dengue_type_value not in ('denv1','denv2','denv3','denv4'):
                raise ValidationError('Invalid value for dengue type. It should be "DENV1" or "DENV2" or "DENV3" or "DENV4".')
            row['dengue_type'] = row['dengue_type'].upper()
    
    def import_row(self, row, instance_loader, **kwargs):
        # Perform any additional import processing here if needed
        return super().import_row(row, instance_loader, **kwargs)