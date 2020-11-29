from rest_framework.authentication import get_authorization_header, BaseAuthentication
from .models import *
import jwt
from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_uid(request):
    auth = get_authorization_header(request).split()
    if not auth or auth[0].lower() != b'token':
        return None
    token = auth[1]
    payload = jwt.decode(token, "SECRET_KEY")
    uid = payload["uid"]
    return uid


@api_view()
def activation_status_view(request):
    """
    This and the following functions expect the Aadhar UID in the JWT token
    """
    uid = get_uid(request)
    activation_status = AadharActivationStatus.objects.get(uid=uid)

    return Response({'Activation Status': activation_status})


@api_view()
def address_detail_view(request):
    uid = get_uid(request)
    address_details = AddressDetails.objects.filter(uid__pk=uid)
    return Response(address_details)


@api_view()
def qualification_data_view(request):
    uid = get_uid(request)
    qualification_data = QualificationData.objects.filter(uid__pk=uid)
    return Response(qualification_data)


@api_view()
def bank_details_view(request):
    uid = get_uid(request)
    bank_details = BankDetails.objects.filter(uid__pk=uid)
    return Response(bank_details)


@api_view()
def personal_details_view(request):
    uid = get_uid(request)
    personal_details = PersonalDetails.objects.filter(uid__pk=uid)
    return Response(personal_details)


@api_view()
def job_exp_view(request):
    uid = get_uid(request)
    job_exp = JobExp.objects.filter(uid__pk=uid)
    return Response(job_exp)