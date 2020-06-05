from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.CsvOperations.as_view(),name = 'csv_operations'),
    path('<username>', views.UpdateOperation.as_view(), name='updatecsv_view'),
]