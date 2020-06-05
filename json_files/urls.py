from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.JsonOperations.as_view(),name = 'json_operations'),
    path('<id>', views.JsonUpdate.as_view(), name='updatejson_view'),
]