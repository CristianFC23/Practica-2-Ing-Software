from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Patient, Laboratorist, LabResults
import json


# ========================== PATIENT ==========================
@method_decorator(csrf_exempt, name='dispatch')
class PatientView(View):
    def get(self, request, id=0):
        if id > 0:
            patients = list(Patient.objects.filter(id=id).values())
            if len(patients) > 0:
                datos = {"Message": "Success", "patient": patients[0]}
            else:
                datos = {"Message": "Patient not found"}
        else:
            patients = list(Patient.objects.values())
            datos = {"Message": "Success", "patients": patients}
        return JsonResponse(datos)

    def post(self, request):
        JsonData = json.loads(request.body)
        JsonData = json.loads(JsonData["body"])
        Patient.objects.create(
            name=JsonData["name"],
            lastname=JsonData["lastname"],
            documento=JsonData["documento"],
            cod_ing=JsonData["cod_ing"],
            direccion=JsonData["direccion"],
            telefono=JsonData["telefono"]
        )
        return JsonResponse({"Message": "Success"})

    def put(self, request, id):
        JsonData = json.loads(request.body)
        JsonData = json.loads(JsonData["body"])
        patients = list(Patient.objects.filter(id=id).values())
        if len(patients) > 0:
            patient = Patient.objects.get(id=id)
            patient.name = JsonData["name"]
            patient.lastname = JsonData["lastname"]
            patient.documento = JsonData["documento"]
            patient.cod_ing = JsonData["cod_ing"]
            patient.direccion = JsonData["direccion"]
            patient.telefono = JsonData["telefono"]
            patient.save()
            datos = {"Message": "Success"}
        else:
            datos = {"Message": "Patient not found"}
        return JsonResponse(datos)

    def delete(self, request, id):
        patients = list(Patient.objects.filter(id=id).values())
        if len(patients) > 0:
            Patient.objects.filter(id=id).delete()
            datos = {"Message": "Success"}
        else:
            datos = {"Message": "Patient not found"}
        return JsonResponse(datos)


# ========================== LABORATORIST ==========================
@method_decorator(csrf_exempt, name='dispatch')
class LaboratoristView(View):
    def get(self, request, id=0):
        if id > 0:
            labs = list(Laboratorist.objects.filter(id=id).values())
            if len(labs) > 0:
                datos = {"Message": "Success", "laboratorist": labs[0]}
            else:
                datos = {"Message": "Laboratorist not found"}
        else:
            labs = list(Laboratorist.objects.values())
            datos = {"Message": "Success", "laboratorists": labs}
        return JsonResponse(datos)

    def post(self, request):
        JsonData = json.loads(request.body)
        JsonData = json.loads(JsonData["body"])
        Laboratorist.objects.create(
            name=JsonData["name"],
            lastname=JsonData["lastname"],
            cod_int=JsonData["cod_int"],
            titulo=JsonData["titulo"],
            telefono=JsonData["telefono"]
        )
        return JsonResponse({"Message": "Success"})

    def put(self, request, id):
        JsonData = json.loads(request.body)
        JsonData = json.loads(JsonData["body"])
        labs = list(Laboratorist.objects.filter(id=id).values())
        if len(labs) > 0:
            lab = Laboratorist.objects.get(id=id)
            lab.name = JsonData["name"]
            lab.lastname = JsonData["lastname"]
            lab.cod_int = JsonData["cod_int"]
            lab.titulo = JsonData["titulo"]
            lab.telefono = JsonData["telefono"]
            lab.save()
            datos = {"Message": "Success"}
        else:
            datos = {"Message": "Laboratorist not found"}
        return JsonResponse(datos)

    def delete(self, request, id):
        labs = list(Laboratorist.objects.filter(id=id).values())
        if len(labs) > 0:
            Laboratorist.objects.filter(id=id).delete()
            datos = {"Message": "Success"}
        else:
            datos = {"Message": "Laboratorist not found"}
        return JsonResponse(datos)


# ========================== LAB RESULTS ==========================
@method_decorator(csrf_exempt, name='dispatch')
class LabResultsView(View):
    def get(self, request, id=0):
        if id > 0:
            results = list(LabResults.objects.filter(id=id).values())
            if len(results) > 0:
                datos = {"Message": "Success", "labresult": results[0]}
            else:
                datos = {"Message": "Result not found"}
        else:
            results = list(LabResults.objects.values())
            datos = {"Message": "Success", "labresults": results}
        return JsonResponse(datos)

    def post(self, request):
        JsonData = json.loads(request.body)
        JsonData = json.loads(JsonData["body"])
        LabResults.objects.create(
            cod_ing_r=JsonData["cod_ing_r"],
            col_tot=JsonData["col_tot"],
            col_hdl=JsonData["col_hdl"],
            col_ldl=JsonData["col_ldl"],
            trig=JsonData["trig"]
        )
        return JsonResponse({"Message": "Success"})

    def put(self, request, id):
        JsonData = json.loads(request.body)
        JsonData = json.loads(JsonData["body"])
        results = list(LabResults.objects.filter(id=id).values())
        if len(results) > 0:
            result = LabResults.objects.get(id=id)
            result.cod_ing_r = JsonData["cod_ing_r"]
            result.col_tot = JsonData["col_tot"]
            result.col_hdl = JsonData["col_hdl"]
            result.col_ldl = JsonData["col_ldl"]
            result.trig = JsonData["trig"]
            result.save()
            datos = {"Message": "Success"}
        else:
            datos = {"Message": "Result not found"}
        return JsonResponse(datos)

    def delete(self, request, id):
        results = list(LabResults.objects.filter(id=id).values())
        if len(results) > 0:
            LabResults.objects.filter(id=id).delete()
            datos = {"Message": "Success"}
        else:
            datos = {"Message": "Result not found"}
        return JsonResponse(datos)
