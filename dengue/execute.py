import os
from .models import *
from django.contrib.gis.utils import LayerMapping
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# barangay_mapping = {
#     'barangay': 'Barangay',
#     'municipal': 'Municipal',
#     'geom': 'MULTIPOLYGON',
# }
barangay_mapping = {
    'barangay': 'barangay',
    'code': 'code',
    'tmp_muni': 'tmp_muni',
    'longitude': 'longitude',
    'latitude': 'latitude',
    'geom': 'MULTIPOLYGON',
}
# country_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/WB_countries_Admin0_10m.shp'))
my_shp = os.path.join(BASE_DIR, 'Barangay/barangay.shp')
def run(verbose=True):
    ours = LayerMapping(Barangay, my_shp, barangay_mapping, transform=False)
    ours.save(strict=True, verbose=verbose)