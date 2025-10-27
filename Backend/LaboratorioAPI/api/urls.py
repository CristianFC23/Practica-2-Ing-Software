from django.urls import path
from .views import PatientView

urlpatterns = [
    # path("paciente/", PatientView.as_view(), name= "patients_list")
    path("paciente/", PatientView.as_view(), name="patients_list"),
    path("paciente/<int:id>", PatientView.as_view(), name="patients_process")
]