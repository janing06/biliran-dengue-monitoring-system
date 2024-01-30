from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.home, name='home'), 
    path('case_geojson/', views.case_geojson, name='case_geojson'),
    path('data_tables/', views.data_tables, name='data_tables'),
    path('total_cases_barangay/', views.total_cases_barangay, name='total_cases_barangay'),
    path('total_cases_municipal/', views.total_cases_municipal, name='total_cases_municipal'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cases_csv/', views.cases_csv, name='cases_csv'),
    path('forecast/<code>', views.forecast, name='forecast'),
    path('choropleth/', views.choropleth, name='choropleth'),
    path('barangay_api/<municipal_code>', views.barangay_api, name='barangay_api'),
    path('render_to_pdf/', views.render_to_pdf, name='render_to_pdf'),
    path('download_csv/', views.download_csv, name='download_csv'),
]   