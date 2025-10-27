from django.http import JsonResponse
from django.views import View
from .models import Patient
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class PatientView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id= 0):
        if (id>0):
            patients= list(Patient.objects.filter(id=id).values())
            if len(patients) > 0:
                patient= patients[0]
                datos= {"Message" : "Succes" , "patient":patient}
            else:
                datos= {"Message" : "Patient not found :v"}
            return JsonResponse(datos)
                
        else:
            patients= list(Patient.objects.values())
            if len(patients) > 0:
                datos= {"Message" : "Success", "patients":patients}
            else:
                datos= {"Message" : "Patients not found"}
                
            return JsonResponse(datos)
    
    def post(self, request):
        JsonData= json.loads(request.body)
        JsonData= json.loads(JsonData["body"])
        Patient.objects.create( name= JsonData["name"],
            lastname= JsonData["lastname"],
            documento= JsonData["documento"],
            cod_ing= JsonData["cod_ing"],
            direccion= JsonData["direccion"],
            telefono= JsonData["telefono"])
        datos= {"Message" : "Success"}
        return JsonResponse(datos)
    
    # def put(self, request):
    def put(self, request, id):
        JsonData= json.loads(request.body)
        JsonData= json.loads(JsonData["body"])
        patients= list(Patient.objects.filter(id=id).values())
        if len(patients) > 0:
            patient= Patient.objects.get(id=id)
            patient.name= JsonData["name"]
            patient.lastname= JsonData["lastname"]
            patient.documento= JsonData["documento"]
            patient.cod_ing= JsonData["cod_ing"]
            patient.direccion= JsonData["direccion"]
            patient.telefono= JsonData["telefono"]
            patient.save()
            datos= {"Message" : "Succes"}
            
        else:
            datos= {"Message" : "Patiente not found :("}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        patients= list(Patient.objects.filter(id=id).values())
        if len(patients) > 0:
            Patient.objects.filter(id=id).delete()
            datos= {"Message" : "Succes"}
        else:
            datos= {"Message" : "No se encuentro"}
        return JsonResponse(datos)